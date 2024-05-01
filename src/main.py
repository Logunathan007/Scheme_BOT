from flask import Flask,render_template,request,jsonify
from flask_cors import CORS
app = Flask(__name__, template_folder='./templates')

CORS(app) 

class PyObject:
    def __init__(self):
        self.question_set = {
            "general": [
                {
                    "question_id": "qno1",
                    "question": "What is your Name ?",
                    "suggestion": [],
                    "key": "name",
                    "value": "",
                    "consider_as_a_category": False,
                    "placeholder": "Enter your name ..."
                },
                {
                    "question_id": "qno2",
                    "question": "What is your Age ?",
                    "suggestion": [],
                    "key": "age",
                    "value": "",
                    "consider_as_a_category": False,
                    "placeholder": "Enter your Age ..."
                },
                {
                    "question_id": "qno3",
                    "question": "What is your Occupation ?",
                    "suggestion": ["Student", "Electriction", "Engineer", "Doctor", "Former"],
                    "key": "occupation",
                    "value": "",
                    "consider_as_a_category": True,
                    "placeholder": "Enter your Occupation ..."
                }
            ],
            "student": [
                {
                    "question_id": "qno1",
                    "question": "What is your Qualification ?",
                    "suggestion": ["10th", "12th", "BE", "BTech", "MTech", "ME", "BSC"],
                    "key": "qualification",
                    "value": "",
                    "consider_as_a_category": True,
                    "placeholder": "Enter your Age ..."
                }
            ],
            "be": [
                {
                    "question_id": "qno1",
                    "question": "What is your Major ?",
                    "suggestion": ["ECE", "MECT", "CSE", "EEE"],
                    "key": "major",
                    "value": "",
                    "consider_as_a_category": False,
                    "placeholder": "Enter your Major ..."
                }
            ],
            "former": [
                {
                    "question_id": "qno1",
                    "question": "Either you are Siru Former or Kuru Former",
                    "suggestion": ["Siru", "Kuru"],
                    "key": "Types of Former",
                    "value": "",
                    "consider_as_a_category": False,
                    "placeholder": "Enter your Category ..."
                }
            ]
        }
        self.list_category = ["general"]
        self.list_index = 0;
        self.questions = [];
        self.question_number = 0;
    
    def question_order_generator(self):
        while self.list_index < len(self.list_category):
            for i in list(self.question_set[str(self.list_category[self.list_index])]):
                self.questions.append(i);
            self.list_index+=1;
                
po = PyObject();

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/data',methods=["POST"])
def responseData():
    if(request.method == "POST"):
        obj = request.json
        print('inside',obj)
        if(len(obj) == 0):
            print("if")
            po.question_order_generator();
            jsontype = jsonify(po.questions[po.question_number])
            po.question_number += 1;
            return jsontype;
        else:
            print("else")
            if(obj['consider_as_a_category']):
                if(obj['value'].lower() in [i.lower() for i in obj['suggestion']]):
                    if(obj['value'].lower() not in po.list_category):
                        po.list_category.append(obj['value'].lower());
            print("cat",po.list_category)
            if(len(po.questions)  > po.question_number):
                jsontype = jsonify(po.questions[po.question_number])
                po.question_number += 1;
            else:
                po.question_order_generator();
                if(len(po.questions) <= po.question_number):
                    jsontype = jsonify({'end_of_conversation' : True})
                else:
                    jsontype = jsonify(po.questions[po.question_number])
                    po.question_number += 1;
            return jsontype;
        
if __name__ == '__main__':
    app.run(debug=True)


    