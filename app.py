from flask import Flask, jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient
import json

app = Flask(__name__)

# MongoDB Atlas connection (replace <your_connection_string>)
client = MongoClient("mongodb+srv://satyaprakashchiramchetty_db_user:<Ko4aN92bgilyMHNF>@cluster0.dvbxqub.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["mydatabase"]
collection = db["students"]

# API route: returns JSON from backend file
@app.route("/api", methods=["GET"])
def api_data():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Home route with form
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        try:
            collection.insert_one({"name": name, "age": int(age)})
            return redirect(url_for("success"))
        except Exception as e:
            return render_template("index.html", error=str(e))
    return render_template("index.html")

# Success page
@app.route("/success")
def success():
    return "Data submitted successfully"

if __name__ == "__main__":
    app.run(debug=True)

