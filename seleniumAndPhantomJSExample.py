from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import IPython

options = Options()
options.add_argument('--headless')
##options.add_argument('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36')  # Last I checked this was necessary.

s=Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service =s)##, options=options)

driver.get("https://us.myprotein.com/")

driver.title # => "Google"

driver.implicitly_wait(1000)

open_search_button = driver.find_element(By.CSS_SELECTOR, "#nav > div.westendHeader > div.westendHeader_container > div.westendHeader_headerSearch > div > button > svg.headerSearch_spyglass")
open_search_button.click()

search_box = driver.find_element(By.CSS_SELECTOR, "#header-search-input")
search_button = driver.find_element(By.CSS_SELECTOR, "#nav > div.westendHeader > div.westendHeader_container > div.westendHeader_headerSearch > div > form > div > button.headerSearch_button > svg")

search_box.send_keys("whey protein powder")
search_button.click()

search_result_url = driver.current_url

##print(search_result_url)

ul = driver.find_element(By.CSS_SELECTOR, "#mainContent > div.productListProducts > ul")
product_list = ul.find_elements(By.CLASS_NAME, "productListProducts_product ")
print(len(product_list))
##sub_ele = ele.find_element(By.XPATH, './div')
##print(sub_ele.text)
i = 0 
for product in product_list:
    product_name = product.find_element(By.XPATH, "./div/a/div/h3")##/html/body/div[4]/div[1]/main/div[3]/ul/li[1]/div
    print('{}:     {}'.format(i,product_name.text))
    product_name.click()
    i = i + 1

##driver.quit()


"""
driver.quit()
search_box = driver.find_element(By.NAME, "q")
search_button = driver.find_element(By.NAME, "btnK")

search_box.send_keys("Selenium")
search_button.click()

driver.find_element(By.NAME, "q").get_attribute("value") # => "Selenium"

driver.quit()
"""
