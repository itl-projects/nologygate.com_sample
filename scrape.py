import requests
from bs4 import BeautifulSoup
import json

list = []
dell = []
des = []
temp = {}
# final = {}
Result = []
count= 0
last ={}

url = 'https://www.nologygate.com/laptops'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
for i in soup.find_all('div'):
    z = (i.get('class'))
    if z is not None and z[0] == "mobile-nav":
        lis = i.find_all('a')
        for j in lis:
            k = j.get('href')
            list.append(k)
print("links found")
# for item in list:
response = requests.get(list[1])
soup = BeautifulSoup(response.text, 'html.parser')
for i in soup.find_all('div'):
    s = (i.get('class'))
    if s is not None and s[0] == 'product':
        new = i.find('a').get('href')
        dell.append(new)

print('starting finding data')
for u in dell:
    res = requests.get(u)
    soup = BeautifulSoup(res.text, 'html.parser')
    for n in soup.find_all('h1'):
        x = n.get("class")
        if x is not None and x == "product-nameed entry-title":
            name = n.text
    for c in soup.find_all('div'):
        f = c.get('class')
        if f is not None and f[0] == 'product-short-desc':
            for j in c.find_all('span'):
                desc = j.text
                des.append(desc)
    for i in soup.find_all('span'):
        b = i.get('itemprop')
        if b is not None and b == "brand":
            brand = i.text
    for i in soup.find_all('div'):
        b = i.get('itemprop')
        if b is not None and b == "description":
            data = i.text
    count += 1

    temp.update({'screen_size': des[0], 'processor': des[1], 'Graphic_processor': des[2], 'Ram': des[3]})
    des.clear()

    final = {"id": count, "Name": n.text, "Specifications": temp, "Description": data}
    Result.append(final)
    # print(Result)

last.update({brand: Result})
r = json.dumps(last)

with open("sample.json", "w") as outfile:
    outfile.write(r)
print("Done")


