from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Task

api_bp = Blueprint("api", __name__)

# -------------------------
# GET ALL TASKS (READ)
# -------------------------
@api_bp.route("/tasks", methods=["GET"])
@jwt_required()
def get_tasks():
    user_id = get_jwt_identity()
    tasks = Task.get_tasks_by_user(user_id)

    result = []
    for t in tasks:
        result.append({
            "id": t.id,
            "title": t.title,
            "user": t.user_id,
            "created_at": str(t.created_at)
        })

    return jsonify(result), 200


# -------------------------
# CREATE TASK
# -------------------------
@api_bp.route("/tasks", methods=["POST"])
@jwt_required()
def create_task():
    user_id = get_jwt_identity()
    data = request.get_json()
    title = data.get("title")

    if not title:
        return jsonify({"error": "Title required"}), 400

    Task.create_task(user_id, title)
    return jsonify({"message": "Task created"}), 201


# -------------------------
# DELETE TASK
# -------------------------
@api_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
@jwt_required()
def delete_task(task_id):
    user_id = get_jwt_identity()

    Task.delete_task(task_id, user_id)
    return jsonify({"message": "Task deleted"}), 200