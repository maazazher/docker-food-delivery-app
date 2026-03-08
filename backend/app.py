from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
import os
import time

app = Flask(__name__)
CORS(app)

# Database connection (PostgreSQL)
def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        database=os.getenv("DB_NAME", "fooddb"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "postgres")
    )

# Wait until database is ready
db = None
while db is None:
    try:
        db = get_db_connection()
        print("Database connected")
    except Exception as e:
        print("Waiting for database...")
        time.sleep(2)

cursor = db.cursor()

# Routes
@app.route("/foods", methods=["GET"])
def get_foods():
    cursor.execute("SELECT id, name, price FROM foods;")
    foods = cursor.fetchall()

    food_list = []
    for food in foods:
        food_list.append({
            "id": food[0],
            "name": food[1],
            "price": food[2]
        })

    return jsonify(food_list)

@app.route("/order", methods=["POST"])
def place_order():
    data = request.json
    return jsonify({
        "message": "Order placed successfully!",
        "order": data
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
