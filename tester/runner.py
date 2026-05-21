import time
import statistics
from tester.tests import (
    test_status_ok,
    test_content_type_json,
    test_required_fields,
    test_field_types,
    test_invalid_endpoint
)
from tester.client import APIClient

API_URL = "https://api.chucknorris.io/jokes/random"
client = APIClient(API_URL)

def run_tests():
    """
    Exécute une campagne de tests :
    - tests fonctionnels (contrat)
    - mesures QoS (latence avg/p95)
    - taux d’erreur
    - disponibilité
    """

    # 1) Tests fonctionnels
    functional_tests = {
        "status_ok": test_status_ok(),
        "content_type_json": test_content_type_json(),
        "required_fields": test_required_fields(),
        "field_types": test_field_types(),
        "invalid_endpoint": test_invalid_endpoint()
    }

    # 2) Mesure QoS : 10 appels pour latence moyenne + p95
    latencies = []
    errors = 0

    for _ in range(10):
        r = client.get()
        if r["ok"] and r["latency"] is not None:
            latencies.append(r["latency"])
        else:
            errors += 1

    # Si aucun appel n’a réussi
    if len(latencies) == 0:
        avg_latency = None
        p95_latency = None
    else:
        avg_latency = sum(latencies) / len(latencies)
        p95_latency = statistics.quantiles(latencies, n=20)[18]  # approx p95

    # 3) Disponibilité
    success_rate = 1 - (errors / 10)

    # 4) Résultat final
    result = {
        "functional": functional_tests,
        "avg_latency": avg_latency,
        "p95_latency": p95_latency,
        "errors": errors,
        "success_rate": success_rate,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    return result

