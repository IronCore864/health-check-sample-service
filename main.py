import random
from flask import Flask


app = Flask(__name__)

healthy = True
done_first_check = False


@app.route("/")
def home_page():
    return "This is my home page", 200


@app.route("/health")
def health_check():
    global healthy, done_first_check

    if not healthy:
        app.logger.warning("Service unhealthy")
        return "Health check failed", 500

    if not done_first_check:
        done_first_check = True
        return "Health check passed", 200

    if random.randint(0, 9) < 2:  # 20% chance of failure
        healthy = False
        app.logger.warning("Service unhealthy")
        return "Health check failed", 500

    return "Health check passed", 200


if __name__ == "__main__":
    app.run(debug=True)
