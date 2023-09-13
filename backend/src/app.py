from flask import Flask, request
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://192.168.18.31:27017/dbcomments"
mongoIDB = PyMongo(app)

db = mongoIDB.db.comments

@app.route('/')
def index():
    return '<h1>HELO WORLD</h1>'

@app.route('/comments', methods=['POST'])
def createComment():
    print(request.json)
    return 'received'

@app.route('/comments', methods=['GET'])
def getComments():
    return 'received'


@app.route('/comment/<id>', methods=['GET'])
def getComment():
    return 'received'



if __name__ == "__main__":
    app.run(debug=True)
