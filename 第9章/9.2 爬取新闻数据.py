from selenium import webdriver
import re
def sina_news(company):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(options=chrome_options)
    url = f'https://search.sina.com.cn/?q={company}&c=news&sort=time'
    browser.get(url)
    data = browser.page_source
    browser.quit()
    p_title = '<div class="box-result clearfix".*?<a href=".*?" target="_blank">(.*?)</a>'
    p_href = '<div class="box-result clearfix".*?<a href="(.*?)" target="_blank">'
    p_date = '<span class="fgray_time">(.*?)</span>'
    title = re.findall(p_title, data, re.S)
    href = re.findall(p_href, data, re.S)
    date = re.findall(p_date, data, re.S)
    for i in range(len(title)):
        title[i] = re.sub('<.*?>', '', title[i])
        date[i] = date[i].split(' ')[1]
        print(f'{i + 1}.{title[i]} | {date[i]}')
        print(href[i])
companies = ['阿里巴巴', '京东', '万科', '腾讯']
for i in companies:
    try:
        sina_news(i)
        print(f'【{i}】的信息爬取成功')
    except:
        print(f'【{i}】的信息爬取失败')
