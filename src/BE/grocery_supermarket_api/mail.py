from flask import Flask,Blueprint,request,render_template,jsonify,Response,send_file
from constant import response_status as rs_sts
from entity import api_objects
app = Flask(__name__)

@app.route('/api', methods=['GET'])
def apiHome():
    r = request.method
    response = api_objects.Response()
    response.status = rs_sts.SUCCESS
    response.message = "Welcome to Flask API"
    return response.__json__()

@app.errorhandler(Exception)
def handle_general_exception(e):
    response = api_objects.Response(status=rs_sts.FAILED, message=str(e))
    return response.__json__()

if __name__ == '__main__':
    app.run(debug=True,host='localhost',port=5000)