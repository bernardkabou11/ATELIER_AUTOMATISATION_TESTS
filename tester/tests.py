from tester.client import APIClient

# API cible
API_URL = "https://api.chucknorris.io/jokes/random"

client = APIClient(API_URL)

def test_status_ok():
    """HTTP 200 attendu"""
    r = client.get()
    return r["status"] == 200

def test_content_type_json():
    """Content-Type JSON attendu"""
    r = client.get()
    return r["json"] is not None

def test_required_fields():
    """Champs obligatoires présents dans le JSON"""
    r = client.get()
    if not r["json"]:
        return False

    data = r["json"]
    required = ["id", "value", "url"]

    return all(field in data for field in required)

def test_field_types():
    """Types attendus pour certains champs"""
    r = client.get()
    if not r["json"]:
        return False

    data = r["json"]

    return (
        isinstance(data.get("id"), str)
        and isinstance(data.get("value"), str)
        and isinstance(data.get("url"), str)
    )

def test_invalid_endpoint():
    """Cas d’erreur : endpoint invalide → 404 attendu"""
    bad_client = APIClient("https://api.chucknorris.io/jokes/doesnotexist")
    r = bad_client.get()
    return r["status"] == 404

