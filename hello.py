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

# ドライバーの場所を指定
driver = webdriver.Chrome(R'C:\Users\xfukushima\Desktop\test_py\sample_dir\chromedriver')

# 起動したいサイトのURLを入力
driver.get('https://www.google.co.jp')

# 開いたページの要素を取得
search_bar = driver.find_element_by_name("q")
search_bar.send_keys("python")

# 検索ボタンを実行
search_bar.submit()

# 検索されたページの要素を取得
for elem_h3 in driver.find_elements_by_xpath('//a/h3'):
    elem_a = elem_h3.find_element_by_xpath('..')  
    print(elem_h3.text)
    print(elem_a.get_attribute('href'))
    

