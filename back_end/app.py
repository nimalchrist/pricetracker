from flask import Flask, jsonify
import GetScrappedProducts as getter
from flask_cors import CORS
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


# driver function
if __name__ == '__main__':

    app.run(debug=True)
