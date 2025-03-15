from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Flask API with PostgreSQL is running!"

@app.route("/db-status")
def db_status():
    """Check PostgreSQL connection status"""
    try:
        conn = psycopg2.connect(
            dbname="mydb",
            user="postgres",
            password="postgres",
            host="db"
        )
        conn.close()
        return "✅ PostgreSQL is connected!"
    except Exception as e:
        return f"❌ Database connection failed: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
