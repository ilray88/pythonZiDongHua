import requests
import re
headers = {'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
url = 'https://www.cnblogs.com'
response = requests.get(url=url, headers=headers)
result = response.text
print(result)
source = '<a class="post-item-title" href=".*?" target="_blank">(.*?)</a>'
title = re.findall(source, result, re.S)
print(title)
