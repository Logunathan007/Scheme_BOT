from flask import Flask,render_template,request,jsonify
from flask_cors import CORS
app = Flask(__name__, template_folder='./templates')

CORS(app) 

question_set = {
    general : [
        {
            question_id : "qno1",
            question : "What is your Name ?",
            suggestion : ["Ram","Sam","Gopal"],
            key : "name",
            value : "",
            category:"general",
            placeholder:"Enter your name ..."
        },
        {
            question_id : "qno2",
            question : "What is your Age ?",
            suggestion : ["18","20","21"],
            key : "age",
            value : "",
            category:"general",
            placeholder:"Enter your Age ..."
        },
        {
            question_id : "qno3",
            question : "What is your Occupation ?",
            suggestion : ["Student","Electriction","Engineer","Doctor"],
            key : "age",
            value : "",
            category:"general",
            placeholder:"Enter your Age ..."            
        }
    ],
    student:[
        {
            question_id : "qno1",
            question : "What is your Qualification ?",
            suggestion : ["Student","Electriction","Engineer","Doctor"],
            key : "age",
            value : "",
            category:"general",
            placeholder:"Enter your Age ..."            
        }
    ]
}


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


    