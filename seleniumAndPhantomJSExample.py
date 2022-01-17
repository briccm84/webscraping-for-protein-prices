from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument('--headless')
##options.add_argument('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36')  # Last I checked this was necessary.

s=Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service =s)##, options=options)

driver.get("https://us.myprotein.com/")

driver.title # => "Google"

driver.implicitly_wait(10000)

open_search_button = driver.find_element(By.CSS_SELECTOR, "#nav > div.westendHeader > div.westendHeader_container > div.westendHeader_headerSearch > div > button > svg.headerSearch_spyglass")
open_search_button.click()

search_box = driver.find_element(By.CSS_SELECTOR, "#header-search-input")
search_button = driver.find_element(By.CSS_SELECTOR, "#nav > div.westendHeader > div.westendHeader_container > div.westendHeader_headerSearch > div > form > div > button.headerSearch_button > svg")###nav > div.westendHeader > div.westendHeader_container > div.westendHeader_headerSearch > div > form > div > button.headerSearch_button > svg

search_box.send_keys("whey protein powder")
print(dir(search_button))
search_button.click()

search_result_url = driver.current_url

##print(search_result_url)

ul = driver.find_element(By.CSS_SELECTOR, "#mainContent > div.productListProducts > ul")
product_list = ul.find_elements(By.CLASS_NAME, "productListProducts_product ")
amount_of_products = len(product_list)
print(amount_of_products)
##sub_ele = ele.find_element(By.XPATH, './div')
##print(sub_ele.text)
i = 0 
while i < amount_of_products:
    ul = driver.find_element(By.CSS_SELECTOR, "#mainContent > div.productListProducts > ul")
    product_list = ul.find_elements(By.CLASS_NAME, "productListProducts_product ")
    product = product_list[i]
    product_name_element = product.find_element(By.XPATH, "./div/a/div/h3")##/html/body/div[4]/div[1]/main/div[3]/ul/li[1]/div
    product_name = product_name_element.text
    product.click()
    top_row_element = driver.find_element(By.CSS_SELECTOR, "#mainContent > div.athenaProductPage_topRow")
    price_element = top_row_element.find_element(By.CLASS_NAME, "productPrice_price")
    price = price_element.text
    print('{}:     {}:price: {}'.format(i,product_name,price))
    driver.back()
    i += 1
print("start sleep")
time.sleep(100.0)
print("end wait")
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
