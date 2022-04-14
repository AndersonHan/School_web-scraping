import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
}

r = requests.get('http://www.hcsh.tp.edu.tw/content?a=T0RESU9ERTJOVEl5TXpBPXlJek53Z1ROeGNsVGludGVseQ==', headers=headers)
if r.status_code == 200:
    print(f'請求成功：{r.status_code}')

    soup = BeautifulSoup(r.text, 'html.parser')
    Coronavirus_Prevention  = soup.select_one(".paragraph_odd")
    items = Coronavirus_Prevention.select(".content")
    
    for item in items:
        item_name = item.select_one("a")
        if item_name == None:break
        else:
            print(item_name.prettify())
            #<a title= 後面即是標題內容 
else:
    print(f'請求失敗：{r.status_code}')

