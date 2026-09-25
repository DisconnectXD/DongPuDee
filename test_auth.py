import json
import os

import app as webapp

HERE = os.path.dirname(os.path.abspath(__file__))
ACCOUNTS_FILE = os.path.join(HERE, "accounts.json")
SESSION_FILE = os.path.join(HERE, "session.json")


def setup_function():
    for file_name in [ACCOUNTS_FILE, SESSION_FILE]:
        if os.path.exists(file_name):
            os.remove(file_name)


def test_signup_and_signin_flow():
    client = webapp.app.test_client()

    signup = client.post(
        "/signup",
        data={
            "full_name": "สมชาย ใจดี",
            "email": "somchai@example.com",
            "password": "123456",
            "phone": "0812345678",
            "address": "123/45",
            "district": "เมือง",
            "province": "อุบลราชธานี",
            "postal_code": "34000",
        },
        follow_redirects=True,
    )
    signup_text = signup.data.decode("utf-8")
    assert signup.status_code == 200
    assert "สมัครสมาชิกสำเร็จ" in signup_text or "Sign up" in signup_text

    with open(ACCOUNTS_FILE, encoding="utf-8") as f:
        accounts = json.load(f)
    assert len(accounts) == 1
    assert accounts[0]["email"] == "somchai@example.com"

    signin = client.post(
        "/signin",
        data={
            "email": "somchai@example.com",
            "password": "123456",
        },
        follow_redirects=True,
    )
    signin_text = signin.data.decode("utf-8")
    assert signin.status_code == 200
    assert "เข้าสู่ระบบสำเร็จ" in signin_text or "Sign in" in signin_text

    with open(SESSION_FILE, encoding="utf-8") as f:
        session = json.load(f)
    assert session["email"] == "somchai@example.com"
