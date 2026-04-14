#!/usr/bin/python3
"""
A simple Flask API with user management.
Supports GET and POST requests for user data.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Хранилище пользователей в памяти
# Согласно NOTE: не оставляем тестовые данные при сдаче
users = {}


@app.route("/")
def home():
    """Root endpoint returning a welcome message."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Returns a list of all usernames stored in the API."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Returns the status of the API."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Returns the full object for a specific username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Adds a new user to the users dictionary from POST JSON data."""
    # Проверка на валидность JSON
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # Проверка наличия username
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Проверка на дубликат
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Добавление пользователя
    users[username] = data
    response = {
        "message": "User added",
        "user": data
    }
    return jsonify(response), 201


if __name__ == "__main__":
    app.run()
