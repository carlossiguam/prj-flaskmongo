from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://192.168.18.31:27017/dbcomments"
mongoIDB = PyMongo(app)

db = mongoIDB.db.comments

if __name__ == "__main__":
    app.run(debug=True)
