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

search_terms = ['whey']

for term in search_terms:
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

    search_box.send_keys(term)
    search_button.click()

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
        #highlight_element(product_menu)
        product_list = product_menu.find_elements(By.CLASS_NAME, 'productDescription_accordionControl')
        product_list_length = len(product_list)
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
        #highlight_element(nutrition_button)
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

        nutrition_information_element = driver.find_element(By.ID,"product-description-content-lg-8")
        table_element = nutrition_information_element.find_element(By.TAG_NAME, 'table')
        highlight_element(table_element)
        nut_text = nutrition_information_element.text #table_element.text
        

        """
        highlight_element(table_element)
        theads_elements = table_element.find_elements(By.CLASS_NAME,"thick-start")

        for ele in theads_elements:
            print(ele.get_attribute('innerhtml'))

        #/html/body/main/div[5]/div[1]/div[2]/div[2]/div[2]/
        #/html/body/main/div[5]/div[1]/div[2]/div[2]/div[2]/div/div/div[6]/div/div/div/div/table/thead[4]/tr[10]/td[2]
        serving_size_element = nutrition_information_element.find_element(By.CSS_SELECTOR, 'td[colspan="5"]')
        #highlight_element(serving_size_element)
        print(serving_size_element.get_attribute('innerhtml'))
        first_index = serving_size_element.text.find("(")+1
        second_index = serving_size_element.text.rfind("g")
        serving_size = serving_size_element.text[first_index:second_index]

        cal_element = product_menu.find_element(By.CSS_SELECTOR, 'td[style="height:18px; width:125px"]')
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
        print("protein: {}".format(protein))"""

        a = nut_text
        a = a.lower()
        cut = a.find('vitamin')
        a = a[:cut]

        r = a.rindex('g')
        r += 1
        a = a[:r]
        try:
            with open('nutritionfacts.txt', 'w') as f:
                f.write(a)
        except:
            print('failed to save element')
        size_index_f = a.find('1 scoop (')+len('1 scoop (')
        size = a[size_index_f:size_index_f+2]
        serving_size = size.replace("<", "")
        serving_size = float(size.replace(".", ""))
        print('size: {}'.format(serving_size))

        try:
            cal_index = a.find('calories ') + len('calories ')
            cal_indexl = a.find(' calories from fat')
            cals = a[cal_index:cal_indexl]
            cals = float(cals.replace("<", ""))
        except:
            cals = 0
        print('cals: {}'.format(cals))

        f_index = a.find('total fat ') + len('Total Fat ')
        f_indexl = a.find('saturated')
        s = a[f_index:f_indexl]
        s = s.strip()
        l = s.find(' g')
        if l == -1:
            l = s.find('g')
        fats = s[:l]
        fat = float(fats.replace("<", ""))
        print('fats: {}'.format(fat))
        a = a[f_indexl:]

        ca = a.find('total carbohydrate ')
        if ca == -1:
            ca = a.find('total carbohydrates ')
        print('ca = {}'.format(ca))
        c_index = ca + len('Total Carbohydrate ')
        c_indexl = a.find('dietary fiber')
        cs = a[c_index:c_indexl]
        cs = cs.strip()
        cl = cs.find(' g')
        if cl == -1:
            cl = cs.find('g')
        carbs = cs[:cl]
        carbs = carbs.replace("<", "")
        carbs = float(carbs)
        print('carbs: {}'.format(carbs))

        p_index = a.find('protein ') + len('protein ')
        p_indexl = a.find('vitamin')
        ps = a[p_index:p_indexl]
        ps = ps.strip()
        pl = ps.find(' g')
        if pl == -1:
            pl = ps.find('g')
        protein = ps
        if pl != -1:
            protein = ps[:pl]    
        protein = float(protein.replace("<", ""))
        print('protein: {}'.format(protein))



        price = price[1:]
        price = float(price)
        nutrition_facts = Nutrition(float(serving_size),float(cals),float(fat),float(carbs),float(protein))
        protein_class = Protein(product_name, price, nutrition_facts,driver.current_url)
        repeat = (1 == 0)
        for item in protein_list:
            if(protein_class.name == item.name):
                repeat = (1==1)
                break

        if not repeat:
            protein_list.append(protein_class)
        print('{}:     {}:price : {}'.format(i,product_name,price))

        
        
        driver.back()
        i += 1
print('writing to file')
write(protein_list)
driver.quit()

