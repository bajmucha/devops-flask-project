from flask import Flask, jsonify
from .db import SessionLocal
from .models import User

# Tworzymy aplikację Flask
app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"message": "pong"}), 200


@app.route("/users", methods=["GET"])
def list_users():
    session = SessionLocal()
    try:
        users = session.query(User).all()
        return jsonify([u.to_dict() for u in users]), 200
    finally:
        session.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
