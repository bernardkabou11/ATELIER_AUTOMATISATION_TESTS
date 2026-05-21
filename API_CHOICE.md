# API_CHOICE.md

## Étudiant : Bernard Daniel Kabou  
## API choisie : Agify  
## URL base : https://api.agify.io  
## Documentation officielle : https://agify.io  
## Auth : Aucune (API publique)

---

## Endpoints testés :

- GET /?name=michael  
- GET /?name=bernard  
- GET /?name= (cas invalide)  
- GET /invalid (endpoint invalide)

---

## Hypothèses de contrat :

| Champ | Type | Description |
|-------|------|-------------|
| name | string | Nom demandé |
| age | int | Âge estimé |
| count | int | Nombre d’occurrences |

**Codes attendus :**
- 200 → requête valide  
- 400 → paramètres invalides  
- 404 → endpoint inexistant  

**Content-Type attendu :** application/json

---

## Limites / rate limiting :

- Pas de limite officielle documentée  
- Peut renvoyer 429 si trop de requêtes  
- Recommandation : max 20 requêtes par run

---

## Risques :

- `age` peut être null  
- API non garantie 24/7  
- Pas de SLA  
- Pas de versioning
