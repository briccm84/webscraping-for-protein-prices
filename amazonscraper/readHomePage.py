import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
}

r = requests.get('http://us.myprotein.com/sports-nutrition/impact-whey-protein/10852500.html', headers = headers)
##print(r.text)

soup = BeautifulSoup(r.text, 'lxml')
ma = soup.find('main')
"""for m in soup.find_all('p', class_ = 'productPrice_price'):
    print(m.text)
tr = ma.find('div', class_ = 'athenaProductPage_topRow')
pd = tr.find('div', class_ = 'athenaProductPage_productDetails_lg')
price = pd.find('div', class_ = 'athenaProductPage_productPrice')
print(price.p.text)
"""
text = ma.find(id = 'athena-product-variation-dropdown-5')
print(text.text)

r.close()

