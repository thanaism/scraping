"""
Seleniumの備忘録

事前準備:
  パッケージのインストール
    $ pip install selenium webdriver_manager
  OSへのChromeインストールはしておくこと
    !! WSLならUbuntu側にChromeをインストールしておく
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# headlessは途中のウィンドウサイズ変更はできないので立上時の設定必須
# デフォルトは800x600で狭い(フロート要素がカブってclick失敗の懸念あり)
chrome_options = webdriver.chrome.options.Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--window-size=3840,2160')
# optchrome_optionsions.add_argument('--disable-extensions')
# chrome_options.add_argument('--proxy-server="direct://"')
# chrome_options.add_argument('--proxy-bypass-list=*')
# chrome_options.add_argument('--start-fullscreen')

# wbdriver_managerを使えば環境のChromeに合わせたwebdriverとなる
driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

# driver.implicitly_wait(100)

url = 'https://google.co.jp/'

driver.get(url)

# element = driver.find_element_by_name('')
# element = driver.find_element_by_id('main')

save_path=''
# 画面全体のスクリーンショット(ウィンドウサイズに注意)
driver.save_screenshot(save_path)

# 特定要素のスクリーンショットも可能
element = driver.find_element_by_tag_name('img')
png = element.screenshot_as_png

with open(save_path, 'wb') as f:
    f.write(png)
    
# element = driver.find_element_by_partial_link_text('')
# element = driver.find_element_by_class_name('')
# element = driver.find_elements_by_xpath('')

# element.send_keys('')
# element.submit()

# アラートのポップアップへのフォーカス移動
# 不安定なのでセッションを渡してrequestsなどで遷移した方がベターか
# driver.switch_to.alert.accept()

# page_width = driver.execute_script('return document.body.scrollWidth')
# page_height = driver.execute_script('return document.body.scrollHeight')
# driver.set_window_size(page_width, page_height)

driver.quit
