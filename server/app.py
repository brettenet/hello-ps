from flask import Flask, jsonify
import psycopg2
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="postgres",
        database=os.getenv("POSTGRES_DB", "postgres"),
        user=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD", "password")
    )
    return conn

@app.route('/api/get-string', methods=['GET'])
def get_string():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT content FROM messages LIMIT 1;")
        result = cur.fetchone()
        cur.close()
        conn.close()
        if result:
            return jsonify({"message": result[0]})
        else:
            return jsonify({"error": "No data found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
