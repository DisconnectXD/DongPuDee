"""pages/page1.py — SAINT SINNER storefront catalog."""

import storage

TITLE = "Shop"


def default_products():
    return [
        {
            "name": "Midnight Riot Tee",
            "category": "Tops",
            "price": 990,
            "tag": "HAND-PAINTED",
            "sizes": ["S", "M", "L", "XL", "XXL"],
            "image": "/static/images/shirt1.jpg",
            "picked": False,
            "qty": 1,
        },
        {
            "name": "Chrome Reaper Tee",
            "category": "Tops",
            "price": 1290,
            "tag": "SAINT SINNER",
            "sizes": ["S", "M", "L", "XL", "XXL"],
            "image": "/static/images/shirt2.jpg",
            "picked": False,
            "qty": 1,
        },
        {
            "name": "Satellite Bloom Tee",
            "category": "Tops",
            "price": 1150,
            "tag": "FULL PATTERN",
            "sizes": ["S", "M", "L", "XL", "XXL"],
            "image": "/static/images/shirt3.jpg",
            "picked": False,
            "qty": 1,
        },
        {
            "name": "Blackout Ritual Tee",
            "category": "Tops",
            "price": 1080,
            "tag": "LIMITED DROP",
            "sizes": ["S", "M", "L", "XL", "XXL"],
            "image": "/static/images/shirt4.jpg",
            "picked": False,
            "qty": 1,
        },
        {
            "name": "Circuit Saint Tee",
            "category": "Tops",
            "price": 1190,
            "tag": "CYBERPUNK",
            "sizes": ["S", "M", "L", "XL", "XXL"],
            "image": "/static/images/shirt5.jpg",
            "picked": False,
            "qty": 1,
        },
        {
            "name": "Gray Static Tee",
            "category": "Tops",
            "price": 1010,
            "tag": "NEW SEASON",
            "sizes": ["S", "M", "L", "XL", "XXL"],
            "image": "/static/images/shirt6.jpg",
            "picked": False,
            "qty": 1,
        },
    ]


def build():
    items = storage.load()
    if not items:
        items = default_products()
        storage.save(items)

    products = []
    for item in items:
        if not item.get("sizes"):
            item["sizes"] = ["S", "M", "L", "XL", "XXL"]
        if not item.get("image"):
            item["image"] = "/static/images/shirt1.jpg"
        item["no"] = len(products)
        item["price_label"] = "฿" + str(item.get("price", 0))
        item["short_tag"] = item.get("tag", "SAINT SINNER")
        products.append(item)

    return {
        "products": products,
        "count": len(products),
        "hero_title": "SAINT SINNER",
        "hero_text": "Streetwear for the after-hours crowd.",
    }


def handle(form):
    items = storage.load()
    action = form.get("action", "")
    no = form.get("no", "")

    if action not in ("add", "buy") or not no.isdigit():
        return "กรุณาเลือกสินค้า"

    index = int(no)
    if index < 0 or index >= len(items):
        return "ไม่พบสินค้าในคอลเลกชัน"

    item = items[index]
    item["picked"] = True
    item["qty"] = max(1, int(item.get("qty", 1)))
    storage.save(items)

    if action == "buy":
        return "✅ ใส่ตะกร้าแล้ว พร้อมชำระเงิน"
    return "✅ เพิ่มสินค้าในตะกร้าแล้ว"
