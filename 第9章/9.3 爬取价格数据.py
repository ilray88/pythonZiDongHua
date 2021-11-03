from selenium import webdriver
import pandas as pd
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(options=chrome_options)
browser.get('http://zdscxx.moa.gov.cn:8080/nyb/pc/frequency.jsp')
time.sleep(2)
browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div[1]').click()
browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div[2]/ul/li[1]').click()
all_data = pd.DataFrame()
for page in range(7):
    time.sleep(2)
    data = browser.page_source
    table = pd.read_html(data)[0]
    all_data = all_data.append(table)
    browser.find_element_by_link_text('下一页').click()
browser.quit()
all_data.to_excel('农产品批发价格.xlsx', index=False)