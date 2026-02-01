import requests
import json

URL = "https://k1n6gb06ip-dsn.algolia.net/1/indexes/*/queries"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/126.0.0.0 Safari/537.36"
    ),
    "Content-Type": "application/json",
    "x-algolia-agent": (
        "Algolia for JavaScript (5.46.0); Lite (5.46.0); Browser; "
        "instantsearch.js (4.86.1); react (19.3.0-canary-f93b9fd4-20251217); "
        "react-instantsearch (7.22.1); react-instantsearch-core (7.22.1); "
        "next.js (16.1.6); JS Helper (3.27.0)"
    ),
    "x-algolia-api-key": "ZGExZGNkYWNlMzY1YzAwNWUyNTEwY2FkMDMzN2IzMDc4MTQzZmNlZTJmNWI4NGI3ODU0Nzc3MWE1M2NjNDZkM2ZpbHRlcnM9Tk9UJTIwbm90VmlzaWJsZUJ5UmVhc29uQ29kZSUzQUQyQyZydWxlQ29udGV4dHM9cmVhc29uQ29kZS1EMkMmdXNlclRva2VuPTE2Zjk5NWIxLThiYWEtNDAyMy1iY2QyLWM3ZDk4YTE2YzI2OSZ2YWxpZFVudGlsPTE3NzAwMDE0ODg=",
    "x-algolia-application-id": "K1N6GB06IP"
}

DATA = {
    "requests": [
        {
            "indexName": "prod_en-US_products",
            "clickAnalytics": True,
            "userToken": "16f995b1-8baa-4023-bcd2-c7d98a16c269"
        }
    ]
}


def extract_price(hit):
    price = hit.get("price")
    if isinstance(price, dict):
        return price.get("value") or price.get("USD")
    return price

def extract_label(hit):
    label = hit.get("stickers")
    if isinstance(label, list) and len(label) > 0:
        return label[0].get("label")
    return label

def main():
    response = requests.post(URL, headers=HEADERS, json=DATA, timeout=30)

    print("Status:", response.status_code)
    print("Response preview:", response.text[:300])

    if response.status_code != 200:
        return

    payload = response.json()
    products = []

    for result in payload.get("results", []):
        for hit in result.get("hits", []):
            products.append({
                "url": hit.get("url"),
                "modelName": hit.get("modelName"),
                "modelCode": hit.get("modelCode"),
                "price": extract_price(hit),
                "imageUrl": hit.get("image") or hit.get("imageUrl"),
                "isInStock": hit.get("isInStock"),
                "label": extract_label(hit),
                "inStockPercentage": hit.get("inStockPercentage")
            })

    for p in products:
        print(f"PRODUCT_NAME={p['modelName']}")
        print(f"PRODUCT_IMAGE={p['imageUrl']}")
        print(f"MODEL_NUMBER={p['modelCode']}")
        print(f"SALE_PRICE={p['price']}")
        print(f"AVAILABILITY={p['isInStock']}")
        print(f"PRODUCT_URL={p['url']}")
        print(f"CONDITION={p['label']}")
        print(f"SKU={p['inStockPercentage']}%")

        

    with open("products.json", "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
