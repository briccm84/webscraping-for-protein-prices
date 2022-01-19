from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from protein import *
import time

protein_list = []

#setup driver
options = Options()
options.add_argument('--headless')
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service =s)##, options=options)

driver.get("https://us.myprotein.com/")
##driver.title # => "Google"
driver.implicitly_wait(2)

def highlight_element(element):
        driver.execute_script("arguments[0].setAttribute('style', 'background: yellow; border: 2px solid red;');", element)
    
open_search_button = driver.find_element(By.CSS_SELECTOR, "#nav > div.westendHeader > div.westendHeader_container > div.westendHeader_headerSearch > div > button > svg.headerSearch_spyglass")

try:
    close_button = driver.find_element(By.CSS_SELECTOR, '#home > div.emailReengagement.show > div > div.emailReengagement_form_container > button > svg')
    close_button.click()
except:
    pass

try:
    close_button = driver.find_element(By.CSS_SELECTOR, '#home > div.emailReengagement.show > div > div.emailReengagement_form_container > button')
    close_button.click()
except:
    pass
open_search_button.click()

search_box = driver.find_element(By.CSS_SELECTOR, "#header-search-input")
search_button = driver.find_element(By.CSS_SELECTOR, "#nav > div.westendHeader > div.westendHeader_container > div.westendHeader_headerSearch > div > form > div > button.headerSearch_button > svg")###nav > div.westendHeader > div.westendHeader_container > div.westendHeader_headerSearch > div > form > div > button.headerSearch_button > svg

search_box.send_keys("whey protein powder")
search_button.click()

search_result_url = driver.current_url

##print(search_result_url)

ul = driver.find_element(By.CSS_SELECTOR, "#mainContent > div.productListProducts > ul")
product_list = ul.find_elements(By.CLASS_NAME, "productListProducts_product ")
amount_of_products = len(product_list)
print(amount_of_products)

try:
    close_pop_up = WebDriverWait(driver,5).until(EC.text_to_be_present_in_element(By.CSS_SELECTOR, "body > div.emailReengagement.show > div > div.emailReengagement_form_container > button"))
    ##driver.find_element(By.CSS_SELECTOR, "body > div.emailReengagement.show > div > div.emailReengagement_form_container > button")
    close_pop_up.click()
except:
    pass
##sub_ele = ele.find_element(By.XPATH, './div')
##print(sub_ele.text)
i = 0 
while i < amount_of_products:
    print(i)
    ul = driver.find_element(By.CSS_SELECTOR, "#mainContent > div.productListProducts > ul")
    product_list = ul.find_elements(By.CLASS_NAME, "productListProducts_product ")
    product = product_list[i]
    highlight_element(product)
    product_name_element = product.find_element(By.XPATH, "./div/a/div/h3")##/html/body/div[4]/div[1]/main/div[3]/ul/li[1]/div
    highlight_element(product_name_element)

    product_name = product_name_element.text.lower()
    relevent = 'protein' in product_name or 'whey' in product_name
    if(not relevent):
        i += 1
        continue
    else:
        ##print("relevent: {}".format(relevent))
    product_name_element.click()

    size_variations = driver.find_elements(By.CLASS_NAME, "athenaProductVariations_listItem")
    size_index = 0
    amount_of_sizes = len(size_variations)
    while size_index < amount_of_sizes:
        size_variations = driver.find_elements(By.CLASS_NAME, "athenaProductVariations_listItem")
        size = size_variations[size_index]
        if('2.2' in size.text):
            highlight_element(size)
            size.click()
            break
        size_index += 1
    time.sleep(1)
    top_row_element = driver.find_element(By.CSS_SELECTOR, "#mainContent > div.athenaProductPage_topRow")
    
    price_element = top_row_element.find_element(By.CLASS_NAME, "productPrice_price ")
    price = price_element.text
    print(price_element.text)

    first_column = top_row_element.find_element(By.CLASS_NAME, "athenaProductPage_firstColumn")
    last_column = top_row_element.find_element(By.CLASS_NAME, "athenaProductPage_lastColumn")
    ##/html/body/main/div[5]/div[1]/div[2]/div[2]/div[2]
    product_menu = first_column.find_element(By.CLASS_NAME, "athenaProductPage_productDescriptionFull")                            
    highlight_element(product_menu)
    product_list = product_menu.find_elements(By.CLASS_NAME, 'productDescription_accordionControl')
    product_list_length = len(product_list)
    ##print(product_list_length)
    product_list_index = 0
    menu_options = []
    while(product_list_index < product_list_length):
        ##print(product_list[product_list_index].text.lower())
        menu_options.append(product_list[product_list_index].text.lower())
        product_list_index +=1
    for option in menu_options:
        if 'nutrition' in option:
            ##print("found nutrition!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            product_list_index = menu_options.index(option)
            product_list_index += 1
            break

    ##print("./div/div/div[{}]/button/div".format(product_list_index))
    nutrition_path = "./div/div/div[{}]/button/div".format(product_list_index)
    if product_list_index == 0:
       nutrition_path = "./div/div/div/button/div"
    nutrition_button = product_menu.find_element(By.XPATH, nutrition_path)
    highlight_element(nutrition_button)
    clicked = 0
    try:
        nutrition_button.click()
        clicked = 1
    except:
        pass
        
    try:
        close_button = driver.find_element(By.CSS_SELECTOR, '#sports > div.emailReengagement.show > div > div.emailReengagement_form_container > button')
        close_button.click()
    except:
        pass
    if(clicked == 0):
        nutrition_button.click()
    ##/html/body/main/div[5]/div[1]/div[2]/div[2]/div[2]/
    ##/html/body/main/div[5]/div[1]/div[2]/div[2]/div[2]/div/div/div[6]/div/div/div/div/table/thead[4]/tr[10]/td[2]
    serving_size_element = product_menu.find_element(By.XPATH, "./div/div/div[{}]/div/div/div/div/table/thead[2]/tr/td".format(product_list_index))
    first_index = serving_size_element.text.find("(")+1
    second_index = serving_size_element.text.rfind("g")
    serving_size = serving_size_element.text[first_index:second_index]

    cal_element = product_menu.find_element(By.XPATH, "./div/div/div[{}]/div/div/div/div/table/thead[4]/tr[1]/td[2]".format(product_list_index))
    cals = cal_element.text
    print("cals: {}".format(cals))

    ##/html/body/main/div[5]/div[1]/div[2]/div[2]/div[2]/div/div/div[6]/div/div/div/div/table/thead[4]/tr[2]/td[2]
    fat_element = product_menu.find_element(By.XPATH, "./div/div/div[{}]/div/div/div/div/table/thead[4]/tr[2]/td[2]".format(product_list_index))
    index_g = fat_element.text.find('g')
    fat = fat_element.text[:index_g]
    fat = fat.replace("<", "")
    print("fat: {}".format(fat))
    
    carbs_element = product_menu.find_element(By.XPATH, "./div/div/div[{}]/div/div/div/div/table/thead[4]/tr[7]/td[2]".format(product_list_index))
    index_g = carbs_element.text.rfind('g')
    carbs = carbs_element.text[:index_g]
    carbs = carbs.replace("<", "")
    carbs = carbs.strip()
    print("carbs: {}".format(carbs))

    protein_element = product_menu.find_element(By.XPATH, "./div/div/div[{}]/div/div/div/div/table/thead[4]/tr[10]/td[2]".format(product_list_index))
    index_g = protein_element.text.find('g')
    protein = protein_element.text[:index_g]
    protein = protein.replace("<", "")
    print("protein: {}".format(protein))

    protein = Protein(product_name, price, Nutrition(float(serving_size),float(cals),float(fat),float(carbs),float(protein)))
    print('{}:     {}:price : {}'.format(i,product_name,price))
    driver.back()
    i += 1
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
