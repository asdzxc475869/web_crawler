#%%
import requests
from bs4 import BeautifulSoup

url = 'https://github.com/'

headers = {}

res = requests.get(url, headers = headers)
# %%
