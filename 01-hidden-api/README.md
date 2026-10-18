# Find the Hidden API Behind Any Website

Code from the SnakeByte video "Find the Hidden API Behind Any Website".

The GOG store page loads its games from a JSON API: `https://catalog.gog.com/v1/catalog`.
These scripts call that API directly instead of parsing HTML.

- `first_request.py`: one request, the total number of games and the first five with prices.
- `gog_catalog.py`: every page of the catalog, saved to `games.xlsx`, biggest discounts first.

## Run it

```bash
pip install requests pandas openpyxl
python first_request.py
python gog_catalog.py
```

`gog_catalog.py` waits half a second between requests, so the whole catalog takes about two minutes.

## Find an API like this yourself

1. Open the site, press F12, go to **Network** and click **Fetch/XHR**.
2. Clear the list and make the page load new data: the next page, a filter or a search.
3. Click the new requests and check **Preview** until you see your data.
   Faster: press Ctrl+F in the Network tab and search for a value you can see on the page.
4. Right-click the request → **Copy** → **Copy as cURL**, paste it into [curlconverter.com](https://curlconverter.com/) and pick Python + Requests.
   The copied command can include your cookies, so never share it.
5. Delete the headers one by one and keep only what the API really needs.

## Shortcuts

- Shopify stores: `/products.json` for the whole store, `/products/<handle>.js` for one product (prices in cents).
- WordPress sites: `/wp-json/wp/v2/posts`.
- Product pages: view the source and search for `ld+json`.

## Be polite

Public data only: no personal data, nothing behind a login or a paywall.
Keep the speed low and check the site's robots.txt and terms.
This is an unofficial API, so it can change at any time.