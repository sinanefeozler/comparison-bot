import requests
from bs4 import BeautifulSoup
headers = {
    "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0"
}
def str_to_int(str):
    a = ""
    for i in str:
        if i.isdecimal():
            a += i
    return int(a)
s = input("Enter key word: ")
#defines
res1 = requests.get(f"https://www.n11.com/arama?q={s}",headers=headers).content
res2 = requests.get(f"https://www.hepsiburada.com/ara?q={s}",headers=headers).content
soup1 = BeautifulSoup(res1,"html.parser")
soup2 = BeautifulSoup(res2,"html.parser")
#first site
ul1 = soup1.find("ul",{"id":"listingUl"})
print(requests.get(f"https://www.n11.com/arama?q={s}",headers=headers).text)
arr1 = []
for li in ul1.find_all("li"):
    if li.get("class") != ["column"]:
        continue
    name = li.find("h3",{"class":"productName"}).text
    price = str_to_int(li.find("ins").text)
    arr1.append((name,price))
arr1.sort(key=lambda x:x[1])
#second site
ul2 = soup2.find("ul",{"id":'1'})
arr2 = []
for li in ul2.find_all("li",{"class":"productListContent-zAP0Y5msy8OHn5z7T_K_"}):
    name = li.find("h3").text
    price = str_to_int(li.find("div",{"data-test-id":"price-current-price"}).text[:-6])
    arr2.append((name,price))
arr2.sort(key=lambda x:x[1])
site1,site2 = 0,0
while True:
    print(f"First site, item:{arr1[site1][0]} price:{arr1[site1][1]}")
    print(f"Second site, item:{arr2[site2][0]} price:{arr2[site2][1]}")
    s = input("1) First site next item\n2) Second site next item\n3-Exit\nChoice:")
    if s == '1':
        if site1 == len(arr1)-1:
            print("You are in last item")
            continue
        site1 += 1
    elif s == '2':
        if site2 == len(arr2)-1:
            print("You are in last item")
            continue
        site2 += 1
    elif s == '3':
        break
    else:
        print("Invalid choice")
