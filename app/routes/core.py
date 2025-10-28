from flask import Blueprint, jsonify

core_bp = Blueprint("core", __name__)

@core_bp.get("/")
def health():
    return jsonify({
        "app": "CipherVault",
        "status": "ok",
        "next": [
            "Add Alembic migrations",
            "Add register/login routes",
            "Wire Argon2id + AES-GCM",
        ],
    })
