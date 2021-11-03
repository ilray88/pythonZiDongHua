from selenium import webdriver
import re
import pandas as pd
import time
def extract_data(html_code):
    p_job = '<p class="t">.*?<span title="(.*?)".*?</span>'
    p_salary = '<p class="info">.*?<span class="sal">(.*?)</span>'
    p_needs = '<p class="info">.*?<span class="d at">(.*?)</span>'
    p_link = '<div class="e_icons ick">.*?<a href="(.*?)"'
    p_company = '<div class="er">.*?title="(.*?)".*?</a>'
    job = re.findall(p_job, html_code, re.S)
    salary = re.findall(p_salary, html_code, re.S)
    needs = re.findall(p_needs, html_code, re.S)
    link = re.findall(p_link, html_code, re.S)
    company = re.findall(p_company, html_code, re.S)
    data_dt = {'职位名称': job, '月薪': salary, '招聘需求': needs, '职位申请链接': link, '公司名称': company}
    return pd.DataFrame(data_dt)
def get_pages(keyword, start, end):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(options=chrome_options)
    browser.maximize_window()
    url = 'https://www.51job.com/'
    browser.get(url)
    browser.find_element_by_xpath('//*[@id="kwdselectid"]').clear()
    browser.find_element_by_xpath('//*[@id="kwdselectid"]').send_keys(keyword)
    browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/button').click()
    time.sleep(10)
    all_data = pd.DataFrame()
    for page in range(start, end + 1):
        browser.find_element_by_xpath('//*[@id="jump_page"]').clear()
        browser.find_element_by_xpath('//*[@id="jump_page"]').send_keys(page)
        browser.find_element_by_class_name('og_but').click()
        time.sleep(10)
        all_data = all_data.append(extract_data(browser.page_source))
    browser.quit()
    all_data.to_excel('职位.xlsx', index=False)
get_pages('python', 1, 3)
