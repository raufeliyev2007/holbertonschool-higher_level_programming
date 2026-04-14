#!/usr/bin/python3
"""
Flask API with Basic Authentication and JWT-based Token Authentication.
Includes Role-Based Access Control (RBAC).
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Конфигурация JWT
app.config["JWT_SECRET_KEY"] = "super-secret-key"  # В реальном проекте используй env
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# Хранилище пользователей
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# --- Настройка Basic Auth ---

@auth.verify_password
def verify_password(username, password):
    """Проверка учетных данных для Basic Auth."""
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username
    return None

# --- Обработчики ошибок JWT (строго 401 по условию) ---

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

# --- Эндпоинты ---

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Доступ через Basic Authentication."""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """Логин и выдача JWT токена."""
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        # Добавляем роль в payload токена
        additional_claims = {"role": user['role']}
        access_token = create_access_token(
            identity=username,
            additional_claims=additional_claims
        )
        return jsonify(access_token=access_token)

    return jsonify({"error": "Invalid credentials"}), 401


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Доступ через JWT Authentication."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Доступ только для пользователей с ролью admin."""
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
