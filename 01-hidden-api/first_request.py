import requests

params = {
    'limit': '100',
    'order': 'desc:trending',
    'productType': 'in:game',
    'page': '1',
    'countryCode': 'US',
    'locale': 'en-US',
    'currencyCode': 'USD',
}

response = requests.get('https://catalog.gog.com/v1/catalog', params=params)

data = response.json()
print(data["productCount"], "games,", data["pages"], "pages")
for game in data["products"][:5]:
    print(game["title"], game["price"]["final"])