#%%
import requests
from bs4 import BeautifulSoup
# %%
#爬威秀電影節目名稱
for i in range(4):
    print(f'====PAGE {i} ====')
    res = requests.get(f'https://www.vscinemas.com.tw/vsweb/film/index.aspx?p={i}')

    # 確保請求成功
    if res.status_code == 200:
        # 使用res.text獲取解碼後的文本內容
        html = res.text

        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(html, 'html.parser')

        # 打印格式化後的HTML內容
        # print(soup.prettify())

        # 示例：提取所有電影標題
        # for movie_title in soup.find_all('section', class_='infoArea'):
        #     print(movie_title.find('a').text)
    else:
        print(f"Failed to retrieve the page. Status code: {res.status_code}")
# %%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

# 使用 Chrome 浏览器
driver = webdriver.Chrome()
driver.get('https://uma.komoejoy.com/character.html')
html = driver.page_source
# %%
#下載賽馬娘
soup = BeautifulSoup(html, 'html.parser')
imgs = soup.find_all('img')
for img in imgs:
    try:
        url = 'http:' + img['data-src']
        filename = img['alt']
        resp = requests.get(url)
        img = resp.content
        print(f'{filename} - {url}')
        #儲存照片
        os.makedirs('test', exist_ok = True)
        with open(f'test/{filename}.png', 'wb') as f:
            f.write(img)
    except:
        pass
# %%
