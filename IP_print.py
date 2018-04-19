from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
@app.route('/get_ip', methods=['GET'])

def get_ip():

    return request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

if __name__ =='__main__':

    app.run(host='0.0.0.0',port=8000)