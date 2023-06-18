from flask import Flask ,request

app = Flask(__name__)

@app.route('/api/v1/login', methods=['POST' ])
def login():
    payload = request.get_json()
    print(payload)
    if((payload.get("username")=="shubham") and (payload.get("passward")=="qwertyuiop")):

        data = {
       " message ": "login ok"
        }
        return data

    return {
        "message":"invalid"
    }
    

app.run(host='0.0.0.0' ,port=8080, debug= True)
