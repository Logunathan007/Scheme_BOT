from flask import Flask,render_template,request,jsonify
from flask_cors import CORS
app = Flask(__name__, template_folder='./templates')

CORS(app) 

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/data',methods=["POST"])
def responseData():
    if(request.method == "POST"):
        print(request.json)
        response_data = {"state":True}
        return jsonify(response_data)
    else:
        response_data = {"state":False}
        return jsonify(response_data)
        

if __name__ == '__main__':
    app.run(debug=True)


    