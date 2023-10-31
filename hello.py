# import time
# import requests
# from bs4 import BeautifulSoup

# # ①「教員プロフィール」からテキスト情報を読み込む
# url1 = "https://www.flet.keio.ac.jp"
# response1 = requests.get(url1)
# soup1 = BeautifulSoup(response1.text, 'html.parser')

# # クロール範囲のリスト化（例: リンクのリスト）
# links = [a['href'] for a in soup1.find_all('a')]
# # ②「研究者データベース」で氏名検索
# url2 = "https://www.k-ris.keio.ac.jp/"
# driver = webdriver.Chrome()  # Chromeドライバーのパスを指定
# driver.get(url2)
# print(driver)


from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(R'C:\Users\xfukushima\Desktop\test_py\sample_dir\chromedriver')

driver.get('https://www.google.co.jp')

