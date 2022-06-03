from flask import Flask
from flask import jsonify
from flask import request
import json

app = Flask(__name__)

employee = [{}]
#employee = [{ 'sapid': '1','name': 'raja','designation': 'devops', 'emailid': 'raja@gmail.com', 'phone': '8148381809' },
#{ 'sapid': '2','name': 'deva','designation': 'devops', 'emailid': 'deva@gmail.com', 'phone': '6784900034' },
#{ 'sapid': '3','name': 'navin','designation': 'lead', 'emailid': 'navin@gmail.com', 'phone': '34567234567' }]

#json_object = json.dumps(employee, indent = 5)
#with open("emp_data.json", "w") as outfile:
   #outfile.write(json_object)
with open('emp_data.json', 'r') as openfile:
   json_object = json.load(openfile)

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'message' : 'Employee Records'})

@app.route('/employee/get', methods=['GET'])
def returnAll():
    #return jsonify({'employee' : employee})
    return jsonify({'Emp_info':json_object})

@app.route('/employee/get/<string:sapid>', methods=['GET'])
def returnOne(sapid):
    # read from file to store in the dict 
    with open('emp_data.json', 'r') as openfile:
        json_object = json.load(openfile)
    employee = json_object
    theOne = employee[0]
    for i,q in enumerate(employee):
      if q['sapid'] == sapid:
        theOne = employee[i]
    return jsonify({'employee' : theOne})


@app.route('/employee/add', methods=['POST'])
def addOne():
    # Read from file 
    with open('emp_data.json', 'r') as openfile:
        json_object = json.load(openfile)
    employee = json_object

    new_employee = request.get_json()
    employee.append(new_employee)
    
    #write to file new data 
    json_object = json.dumps(employee, indent = 5)
    with open("emp_data.json", "w") as outfile:
        outfile.write(json_object)
    #return jsonify({'Emp_info':json_object})
    return json_object


@app.route('/employee/update/<string:sapid>', methods=['PUT'])
def editOne(sapid):
        # Read from file 
    with open('emp_data.json', 'r') as openfile:
        json_object = json.load(openfile)
    employee = json_object


    new_employee = request.get_json()
    for i,q in enumerate(employee):
      if q['sapid'] == sapid:
        employee[i] = new_employee    
    qs = request.get_json()
    
    #update to file new data 
    json_object = json.dumps(employee, indent = 5)
    with open("emp_data.json", "w") as outfile:
        outfile.write(json_object)
    return jsonify({'Emp_info':json_object})

    #return jsonify({'employee' : employee})

@app.route('/employee/delete/<string:sapid>', methods=['DELETE'])
def deleteOne(sapid):

    # Read from file 
    with open('emp_data.json', 'r') as openfile:
        json_object = json.load(openfile)
    employee = json_object


    for i,q in enumerate(employee):
      if q['sapid'] == sapid:
        del employee[i]  
    #return jsonify({'employee' : employee})

    #updating
    json_object = json.dumps(employee, indent = 5)
    with open("emp_data.json", "w") as outfile:
        outfile.write(json_object)
    #return jsonify({'Emp_info':json_object})
    return jsonify({'Emp_info':json_object})


if __name__ == "__main__":
    app.run(debug=True)
