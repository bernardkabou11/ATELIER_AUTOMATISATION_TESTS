import requests
import time

class APIClient:
    """
    Client HTTP robuste pour tester une API publique.
    Gère timeout, retry, latence, erreurs 429/5xx.
    """

    def __init__(self, base_url, timeout=3, retries=1):
        self.base_url = base_url
        self.timeout = timeout
        self.retries = retries

    def get(self, endpoint=""):
        url = self.base_url + endpoint

        for attempt in range(self.retries + 1):
            start = time.time()

            try:
                response = requests.get(url, timeout=self.timeout)
                latency = time.time() - start

                # Gestion 429 (rate limit)
                if response.status_code == 429:
                    time.sleep(1)  # backoff simple
                    continue

                # Gestion erreurs serveur
                if response.status_code >= 500:
                    if attempt < self.retries:
                        continue

                return {
                    "ok": True,
                    "status": response.status_code,
                    "json": response.json() if "application/json" in response.headers.get("Content-Type", "") else None,
                    "latency": latency,
                    "error": None
                }

            except Exception as e:
                if attempt == self.retries:
                    return {
                        "ok": False,
                        "status": None,
                        "json": None,
                        "latency": None,
                        "error": str(e)
                    }

        # Si on sort de la boucle sans succès
        return {
            "ok": False,
            "status": None,
            "json": None,
            "latency": None,
            "error": "Max retries reached"
        }

