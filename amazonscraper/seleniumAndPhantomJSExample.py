from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from IPython import get_ipython
ipython = get_ipython()
options = Options()
##options.add_argument('--headless')
options.add_argument('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36')  # Last I checked this was necessary.

s=Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service =s)##, options=options)

driver.get("https://www.google.com")

driver.save_screenshot('testing.png')

driver.title # => "Google"

driver.implicitly_wait(10000)

search_box = driver.find_element(By.NAME, "q")
search_button = driver.find_element(By.NAME, "btnK")##
ipython.embed()
driver.implicitly_wait(10000)

search_box.send_keys("Selenium")

driver.implicitly_wait(10000)

search_button.click()



driver.find_element(By.NAME, "q").get_attribute("value") # => "Selenium"
#genesis-mobile-nav-primary > span.hamburger-box > span
driver.quit()

r"""
import sys

new_path = r'C:\Users\msbri\AppData\Local\Programs\Python\Python39\amazonscraper\venv\Lib\site-packages'
sys.path.append(new_path)
""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

options = Options()
options.add_argument('--headless')
options.add_argument('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36')  # Last I checked this was necessary.

s=Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service =s, options=options)

driver.set_window_size(1024, 768)
driver.get('https://google.com/')

driver.save_screenshot('testing.png')

element = driver.find_element_by_name(By.XPATH,'/html/body/ntp-app//div/ntp-realbox//div/input')
""
elemnt.send_keys('testing' )
elemnt.send_keys(Keys.ENTER)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.PhantomJS(executable_path=r'C:\PhantomJs\bin\phantomjs\bin\phantomjs.exe')
driver.set_window_size(1024, 768)
driver.get('https://google.com/')

element = driver.find_element_by_xpath()
elemnt.send_keys('testing.png' )
elemnt.send_keys(Keys.ENTER)
"""
