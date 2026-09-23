"""pages/page3.py — shopping cart summary."""

import storage

TITLE = "Cart"


def build():
    items = storage.load()
    picked = []
    count = 0
    subtotal = 0

    index = 0
    for item in items:
        item["no"] = index
        index = index + 1
        if item.get("picked", False):
            qty = max(1, int(item.get("qty", 1)))
            item["qty"] = qty
            picked.append(item)
            count = count + qty
            subtotal = subtotal + qty * int(item.get("price", 0))

    shipping = 0
    if subtotal > 0 and subtotal < 2500:
        shipping = 120
    elif subtotal >= 2500:
        shipping = 0

    total = subtotal + shipping
    return {
        "items": picked,
        "count": count,
        "subtotal": subtotal,
        "shipping": shipping,
        "total": total,
    }


def handle(form):
    items = storage.load()
    action = form.get("action", "")
    no = form.get("no", "")

    if action == "clear":
        for item in items:
            item["picked"] = False
            item["qty"] = 1
        storage.save(items)
        return "ล้างตะกร้าแล้ว"

    if action in ("remove", "plus", "minus") and no.isdigit():
        index = int(no)
        if 0 <= index < len(items):
            item = items[index]
            if action == "remove":
                item["picked"] = False
                item["qty"] = 1
                storage.save(items)
                return "เอาสินค้าออกจากตะกร้าแล้ว"
            qty = max(1, int(item.get("qty", 1)))
            if action == "plus":
                qty = qty + 1
            elif action == "minus" and qty > 1:
                qty = qty - 1
            item["qty"] = qty
            storage.save(items)
            return "อัปเดตจำนวนสินค้าแล้ว"

    return "ไม่เข้าใจคำสั่ง"
