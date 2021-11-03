import requests
import re
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
user = '***@qq.com'
code = 'thoh****vbbb****'
to = '****@qq.com'
while True:
    def dangdang(page):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
        url = 'http://search.dangdang.com/?key=python&act=input&page_index=' + str(page)
        response = requests.get(url=url, headers=headers).text
        p_name = '<p class="name".*?title="(.*?)"'
        p_comments = '<span class="search_star_black">.*?<a href=".*?".*?>(.*?)</a>'
        p_link = '<p class="name".*?href="(.*?)"'
        name = re.findall(p_name, response, re.S)
        comments = re.findall(p_comments, response, re.S)
        link = re.findall(p_link, response, re.S)
        data = {'书名': name, '评论数': comments, '链接': link}
        data = pd.DataFrame(data)
        return data
    all_data = pd.DataFrame()
    for i in range(1, 3):
        all_data = all_data.append(dangdang(i))
    all_data.to_excel('F:\\代码文件\\第10章\\python.xlsx', index=False)
    message = MIMEMultipart()
    attachment = MIMEText(open('F:\\代码文件\\第10章\\python.xlsx', 'rb').read(), 'base64', 'utf-8')
    attachment['Content-Type'] = 'application/octet-stream'
    attachment.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', 'python.xlsx'))
    message.attach(attachment)
    message['Subject'] = '邮件主题'
    message['From'] = user
    message['To'] = to
    server = smtplib.SMTP_SSL('smtp.qq.com', 465)
    server.login(user, code)
    server.send_message(message)
    server.quit()
    print('邮件发送成功！')
    time.sleep(3600)
