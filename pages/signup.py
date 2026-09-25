import json
import os

TITLE = "Sign Up"

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ACCOUNTS_FILE = os.path.join(ROOT, "accounts.json")


def load_accounts():
    if not os.path.exists(ACCOUNTS_FILE):
        return []
    with open(ACCOUNTS_FILE, encoding="utf-8") as f:
        try:
            data = json.load(f)
            if isinstance(data, list):
                return data
        except json.JSONDecodeError:
            pass
    return []


def save_accounts(accounts):
    with open(ACCOUNTS_FILE, "w", encoding="utf-8") as f:
        json.dump(accounts, f, ensure_ascii=False, indent=2)


def build():
    return {
        "headline": "Create your account",
        "subtext": "Register to save your shipping address and order details.",
    }


def handle(form):
    full_name = (form.get("full_name", "") or "").strip()
    email = (form.get("email", "") or "").strip().lower()
    password = (form.get("password", "") or "").strip()
    phone = (form.get("phone", "") or "").strip()
    address = (form.get("address", "") or "").strip()
    district = (form.get("district", "") or "").strip()
    province = (form.get("province", "") or "").strip()
    postal_code = (form.get("postal_code", "") or "").strip()

    if not full_name or not email or not password:
        return "กรุณากรอกชื่อ อีเมล และรหัสผ่านให้ครบ"

    if "@" not in email or "." not in email:
        return "รูปแบบอีเมลไม่ถูกต้อง"

    if len(password) < 6:
        return "รหัสผ่านต้องมีอย่างน้อย 6 ตัวอักษร"

    accounts = load_accounts()
    for account in accounts:
        if (account.get("email", "") or "").lower() == email:
            return "อีเมลนี้มีคนสมัครแล้ว"

    accounts.append(
        {
            "full_name": full_name,
            "email": email,
            "password": password,
            "phone": phone,
            "address": {
                "street": address,
                "district": district,
                "province": province,
                "postal_code": postal_code,
            },
            "created_at": "now",
        }
    )
    save_accounts(accounts)
    return "สมัครสมาชิกสำเร็จ"
