from bs4 import BeautifulSoup
import requests
import pandas

link = "https://www.flipkart.com/search?q=tv&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_8_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_8_0_na_na_na&as-pos=8&as-type=TRENDING&suggestionId=tv&requestId=9c9fa553-b7e5-454b-a65b-bbb7a9c74a29"

page = requests.get(link)
soup = BeautifulSoup(page.content, "html.parser")

name = []
price = []

for i in soup.findAll("div", class_="_3pLy-c row"):
    product_name = i.find("div", attrs={"class" : "_4rR01T"})
    product_price = i.find("div", attrs={"class" : "_30jeq3 _1_WHN1"})
    name.append(product_name.text)
    price.append(product_price.text)

data = pandas.DataFrame({"product name":name,"Product price":price})
print(data.head())
data.to_csv("result.csv")