from flask import Flask
from monitor import test_api

app = Flask(__name__)

@app.route("/")
def home():
    return "ATELIER METRIQUES — Bernard"

@app.route("/metrics")
def metrics():
    result = test_api()

    return (
        f"# HELP api_status API status\n"
        f"# TYPE api_status gauge\n"
        f"api_status {1 if result['status_ok'] else 0}\n\n"

        f"# HELP api_json JSON validity\n"
        f"# TYPE api_json gauge\n"
        f"api_json {1 if result['json_ok'] else 0}\n\n"

        f"# HELP api_duration_seconds Response time\n"
        f"# TYPE api_duration_seconds gauge\n"
        f"api_duration_seconds {result['duration']}\n"
    )

if __name__ == "__main__":
    app.run()
