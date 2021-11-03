from selenium import webdriver
import time
import re
browser = webdriver.Chrome()
url = 'http://www.cninfo.com.cn/new/fulltextSearch?notautosubmit=&keyWord=理财'
browser.get(url)
time.sleep(3)
data = browser.page_source
p_count = '<span class="total-box" style="">约(.*?)条'
count = re.findall(p_count, data)[0]
pages = int(int(count) / 10)
datas = []
datas.append(data)
for i in range(pages):
    browser.find_element_by_xpath('//*[@id="fulltext-search"]/div/div[1]/div[2]/div[4]/div[2]/div/button[2]').click()
    time.sleep(3)
    data = browser.page_source
    datas.append(data)
    time.sleep(3)
alldata = ''.join(datas)
browser.quit()
p_title = '<span title="" class="r-title">(.*?)</span>'
p_href = '<a target="_blank" href="(.*?)".*?<span title='
title = re.findall(p_title, alldata)
href = re.findall(p_href, alldata)
for i in range(len(title)):
    title[i] = re.sub('<.*?>', '', title[i])
    href[i] = 'http://www.cninfo.com.cn' + href[i]
    href[i] = re.sub('amp;', '', href[i])
    print(str(i + 1) + '.' + title[i])
    print(href[i])
for i in range(len(href)):
    browser = webdriver.Chrome()
    browser.get(href[i])
    try:
        browser.find_element_by_xpath('//*[@id="sub-line"]/span[1]').click()
        time.sleep(3)
        browser.quit()
        print(str(i+1) + '.' + title[i] + '下载完毕')
    except:
        print(title[i] + '没有PDF文件')
