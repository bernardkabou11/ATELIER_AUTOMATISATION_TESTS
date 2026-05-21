from flask import Flask, render_template
from tester.runner import run_tests
from storage import save_run, list_runs

app = Flask(__name__)

@app.get("/")
def consignes():
    return render_template("consignes.html")

@app.get("/run")
def run():
    """
    Lance une campagne de tests API et stocke le résultat.
    """
    result = run_tests()      # dict avec métriques
    save_run(result)          # enregistrement SQLite
    return "Run exécuté — consulte /dashboard"

@app.get("/dashboard")
def dashboard():
    """
    Affiche l’historique des runs.
    """
    runs = list_runs()        # liste de dicts
    return render_template("dashboard.html", runs=runs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
