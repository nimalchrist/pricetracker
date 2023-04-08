from urllib import request
from flask import Flask, jsonify
import GetScrappedProducts as getter
from flask_cors import CORS
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="fency@07",
  database="login"
)

# creating a Flask app
app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def welcome():
    return "Hello"


@app.route('/products/<string:product_name>', methods=['GET'])
def products(product_name):
    print("method called")
    res = getter.getScrappedProducts(product_name)
    response = jsonify(res)

    return response


@app.route('/register', methods=['POST'])
def register():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']

    cursor = mydb.cursor()
    sql = "INSERT INTO accounts (username, email, password) VALUES (%s, %s, %s)"
    val = (username, email, password)
    cursor.execute(sql, val)
    mydb.commit()

    return jsonify({'success': True})
    

# driver function
if __name__ == '__main__':

    app.run(debug=True)
