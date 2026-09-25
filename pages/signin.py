import json
import os

TITLE = "Sign In"

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ACCOUNTS_FILE = os.path.join(ROOT, "accounts.json")
SESSION_FILE = os.path.join(ROOT, "session.json")


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


def load_session():
    if not os.path.exists(SESSION_FILE):
        return {}
    with open(SESSION_FILE, encoding="utf-8") as f:
        try:
            data = json.load(f)
            if isinstance(data, dict):
                return data
        except json.JSONDecodeError:
            pass
    return {}


def save_session(data):
    with open(SESSION_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def build():
    session = load_session()
    return {
        "logged_in": bool(session.get("logged_in")),
        "user_name": session.get("full_name", ""),
    }


def handle(form):
    email = (form.get("email", "") or "").strip().lower()
    password = (form.get("password", "") or "").strip()

    if not email or not password:
        return "กรุณากรอกอีเมลและรหัสผ่าน"

    accounts = load_accounts()
    for account in accounts:
        if (account.get("email", "") or "").lower() == email and account.get("password", "") == password:
            save_session(
                {
                    "logged_in": True,
                    "email": email,
                    "full_name": account.get("full_name", ""),
                    "address": account.get("address", {}),
                }
            )
            return "เข้าสู่ระบบสำเร็จ"

    return "อีเมลหรือรหัสผ่านไม่ถูกต้อง"
