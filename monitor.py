import requests
import time

API_URL = "https://api.chucknorris.io/jokes/random"

def test_api():
    start = time.time()
    try:
        r = requests.get(API_URL, timeout=5)
        duration = time.time() - start

        status_ok = r.status_code == 200
        json_ok = "value" in r.json()

        return {
            "status_ok": status_ok,
            "json_ok": json_ok,
            "duration": duration
        }

    except Exception:
        return {
            "status_ok": False,
            "json_ok": False,
            "duration": -1
        }

