import time

import pandas as pd
import requests

URL = "https://catalog.gog.com/v1/catalog"
PARAMS = {
    "limit": 100,
    "order": "desc:trending",
    "productType": "in:game",
    "countryCode": "US",
    "locale": "en-US",
    "currencyCode": "USD",
}


def get_page(page):
    response = requests.get(URL, params={**PARAMS, "page": page}, timeout=10)
    response.raise_for_status()
    return response.json()


def main():
    first = get_page(1)
    games = first["products"]
    for page in range(2, first["pages"] + 1):
        time.sleep(0.5)  # be polite: one request every half second
        games += get_page(page)["products"]
        print(f"Page {page}/{first['pages']}: {len(games)} games")

    rows = []
    for game in games:
        price = game["price"]
        if not price:  # not for sale yet, nothing to save
            continue
        rows.append({
            "title": game["title"],
            "price": float(price["finalMoney"]["amount"]),
            "full_price": float(price["baseMoney"]["amount"]),
            "discount %": int((price["discount"] or "0%").strip("-%")),
            "link": game["storeLink"],
        })

    df = pd.DataFrame(rows).sort_values("discount %", ascending=False)
    df.to_excel("games.xlsx", index=False)
    print(f"Saved {len(df)} games to games.xlsx ({len(games) - len(df)} without a price)")


if __name__ == "__main__":
    main()