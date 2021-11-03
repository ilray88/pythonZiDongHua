import requests
import re
import pandas as pd
def dangdang(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    url = 'http://bang.dangdang.com/books/bestsellers/1-' + str(page)
    response = requests.get(url=url, headers=headers).text
    p_rank = '<div class="list_num.*?">(.*?).</div>'
    p_picture = '<div class="pic">.*?<img src="(.*?)".*?></a>'
    p_name = '<div class="name".*?title="(.*?)">.*?</a>'
    p_comments = '<div class="star">.*?target="_blank">(.*?)</a>'
    p_price_discount = '<div class="price">.*?<span class="price_n">&yen;(.*?)</span>.*?</span>'
    p_price = '<div class="price">.*?<span class="price_r">&yen;(.*?)</span>'
    rank = re.findall(p_rank, response)
    picture = re.findall(p_picture, response)
    name = re.findall(p_name, response)
    comments = re.findall(p_comments, response)
    price_discount = re.findall(p_price_discount, response, re.S)
    price = re.findall(p_price, response, re.S)
    data = {'排名': rank, '图书封面': picture, '书名': name, '评论数': comments, '折扣价': price_discount, '原价': price}
    data = pd.DataFrame(data)
    return data
all_data = pd.DataFrame()
for i in range(1, 6):
    all_data = all_data.append(dangdang(i))
all_data.to_excel('当当网图书畅销榜.xlsx', index=False)
