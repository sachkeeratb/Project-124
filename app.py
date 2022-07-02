from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = [{
    'id':1, 'Name':'Joe', 'Contact':'6476276322', 'done':False},
{
    'id':2, 'Name':'Donald', 'Contact':'6476276323', 'done':False}
]

@app.route("/add-data", methods=["POST"])
def add_task(): 
    if(not request.json):
        return(jsonify({
            "status":"Error", "message":"Please Provide The Data"
        }, 400
    ))
    contact = {"id":tasks[-1]['id'] + 1, 
    'Name':request.json['Name'], 
    'Contact':request.json.get('Contact', ""), 
    'done':False}
    tasks.append(contact)
    return(jsonify({"status":"Sucess", "message":"Task Added Sucessfully"}
    ))

@app.route("/get-data")
def getData():
    return(jsonify({
        "data":tasks
    }))

if(__name__ == '__main__'):
    app.run()