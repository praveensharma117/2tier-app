from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "password")
DB_HOST = os.getenv("DB_HOST", "mysql")
DB_NAME = os.getenv("DB_NAME", "testdb")

app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name} for u in users])

@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    user = User(name=data["name"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User added"}), 201

if __name__ == "__main__":
    db.create_all()
    app.run(host="0.0.0.0", port=5000)
