"""pages/page1.py — shirt catalog page."""

TITLE = "Page 1"


def build():
    products = [
        {
            "id": 1,
            "name": "สินค้าที่ 1",
            "price": 390,
            "price_label": "฿390",
            "color": "Gray",
            "size": "L",
            "tag": "Hand-painted",
            "image": "/static/images/shirt1.jpg",
        },
        {
            "id": 2,
            "name": "สินค้าที่ 2",
            "price": 590,
            "price_label": "฿590",
            "color": "Black",
            "size": "L",
            "tag": "Saint Sinner",
            "image": "/static/images/shirt2.jpg",
        },
        {
            "id": 3,
            "name": "สินค้าที่ 3",
            "price": 490,
            "price_label": "฿490",
            "color": "White",
            "size": "L",
            "tag": "Full Pattern",
            "image": "/static/images/shirt3.jpg",
        },
        {
            "id": 4,
            "name": "สินค้าที่ 4",
            "price": 390,
            "price_label": "฿390",
            "color": "Black",
            "size": "L",
            "tag": "Skull Detail",
            "image": "/static/images/shirt4.jpg",
        },
        {
            "id": 5,
            "name": "สินค้าที่ 5",
            "price": 490,
            "price_label": "฿490",
            "color": "Gray",
            "size": "XL",
            "tag": "Cybersigilism",
            "image": "/static/images/shirt5.jpg",
        },
        {
            "id": 6,
            "name": "สินค้าที่ 6",
            "price": 390,
            "price_label": "฿390",
            "color": "White",
            "size": "XL",
            "tag": "Handmade",
            "image": "/static/images/shirt6.jpg",
        },
    ]

    return {
        "products": products,
        "catalog_intro": "สามารถเลือกซื้อเสื้อยืดลายสวย ๆ ได้ที่นี่",
    }
