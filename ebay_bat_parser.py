import requests
from bs4 import BeautifulSoup
import json

keyword = 'baseball bat'
headers = {
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:79.0) Gecko/20100101 Firefox/79.0'
}

results = []

for i in range(11):

    r = requests.get('https://www.ebay.com/sch/i.html?_nkw='+keyword+'&_pgn='+str(i+1), headers=headers)

    print('Status Code = ', r.status_code)
    print('Page Number = ', str(i+1))
    soup = BeautifulSoup(r.text, 'html.parser')

    boxes = soup.select('li.s-item--watch-at-corner.s-item')

    for box in boxes:

        result = {}

        titles = box.select('li.s-item--watch-at-corner.s-item > .clearfix.s-item__wrapper > .clearfix.s-item__info > .s-item__link > .s-item__title--has-tags.s-item__title')
        for title in titles:
            result['Title'] = title.text

        prices = box.select('.s-item__price')
        for price in prices:
            result['Price'] = price.text

        secondary_info = box.select('.SECONDARY_INFO')
        for wear in secondary_info:
            result['Wear'] = wear.text

        results.append(result)

    print('len(results)=',len(results))

j = json.dumps(results)
with open('items.json', 'w') as f:
    f.write(j)