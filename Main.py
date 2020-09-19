import requests
import bs4
url = "https://www.snapdeal.com/products/mobiles-mobile-phones/filters/Form_s~Smartphones?sort=plrty&q=Form_s%3ASmartphones%7C"
requests.get(url)
response = requests.get(url)
#print(type(response))
#print(response.text)
filename = "temp.html"
bs= bs4.BeautifulSoup(response.text,"html.parser")
formatted_text=bs.prettify()
#print(formatted_text)

#with open(filename,"w+") as f:
    #f.write(formatted_text)

list_imgs = bs.find_all('img')    
print(list_imgs)
no_of_imgs = len(list_imgs)

list_as = bs.find_all('a')
no_of_as = len(list_as)
print(formatted_text)
try:
     with open(filename,"w+") as f:
        f.write(formatted_text)
except Exception as e:
    print(e)

print(str(no_of_as))
print(str(no_of_imgs))
    
print("number of img tags",no_of_imgs )
print("number of anchor tags",no_of_as )

