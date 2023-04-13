from flask import Flask, jsonify, request
import GetScrappedProducts as getter
from flask_cors import CORS
import mysql.connector
import cheap_product as cheap


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="fency@07",
    database="pt_tracter"
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
    #response = jsonify(res)

    if request.method == 'GET' and 'cheapest_product' in request.args:
        cheapest_product = cheap.get_cheapest_product(res)
        response = jsonify(cheapest_product)
    else:
        response = jsonify(res)

    #return response


@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data['email']
        password = data['password']

        cursor = mydb.cursor()
        sql = "SELECT * FROM users WHERE email = %s"
        val = (email,)
        cursor.execute(sql, val)
        user = cursor.fetchone()
        print(user)
        if user is None:
            return jsonify({'msg': 'Email not found'}), 400

        if password != user[3]:
            return jsonify({'msg': 'Incorrect password'}), 400

        return jsonify({'msg': 'Logged in successfully'}), 200

    except Exception as e:
        print(e)
        return jsonify({'msg': 'Error occurred while logging in'}), 500


@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        username = data['username']
        email = data['email']
        password = data['password']

        cursor = mydb.cursor()
        sql = "SELECT * FROM users WHERE email=%s"
        val = (email,)
        cursor.execute(sql, val)
        result = cursor.fetchone()

        if result is not None:
            return jsonify({'msg': "Email already exists"}), 400

        sql = "INSERT INTO users(user_name, email, password) VALUES (%s, %s, %s)"
        val = (username, email, password)
        cursor.execute(sql, val)
        mydb.commit()

        return jsonify({'msg': "Registered Successfully"}), 200
    except Exception as e:
        print(e)
        return jsonify({'msg': "Error occurred while registering"}), 500


# driver function
if __name__ == '__main__':

    app.run(debug=True)
