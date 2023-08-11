from flask import Flask,Blueprint,request,render_template,jsonify,Response,send_file
from service import ItemService
from model import Item
from constant import response_status as rs_sts
from model import api
import json

from service.FakeService import FakeService

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def apiHome():
    r = request.method
    response = api.Response()
    response.status = rs_sts.SUCCESS
    response.message = "Welcome to Flask API"
    return response.__json__()

@app.route('/api/grocery/init', methods=['GET'])
def query():
    return FakeService().get_grocery_init_data()


@app.errorhandler(Exception)
def handle_general_exception(e):
    response = api.Response(status=rs_sts.FAILED, message=str(e))
    return response.__json__()

if __name__ == '__main__':
    app.run(debug=True,host='localhost',port=5010)