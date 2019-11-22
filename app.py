from flask import Flask, request
import requests
import sys
app = Flask(__name__)
ip=sys.argv[1]
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>',methods=['GET', 'POST','PUT','DELETE'])
def catch_all(path):
    if(request.method == 'POST'):
        
        r = requests.post(f'http://{ip}:5000/{path}',  json=request.get_json(force=True))
    elif(request.method == 'GET'):
        r = requests.get(f'http://{ip}:5000/{path}')
    elif(request.method == 'PUT'):
        r = requests.put(f'http://{ip}:5000/{path}', json=request.get_json(force=True))
    elif(request.method == 'DELETE'):
        r = requests.put(f'http://{ip}:5000/{path}')
    return r.text

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)