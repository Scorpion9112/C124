from flask import Flask,jsonify, request

app= Flask(__name__)
task1=[
    {
        "id":1,
        "title":u"Buy groceries",
        "description":u"Buy Milk",
        "done":False
    },
    {
        "id":2,
        "title":u"Go to school",
        "description":u"Attend Classes",
        "done":False
    }
]
@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400)
    task2={
        "id":task1[-1]["id"]+1,
        "title":request.json["title"],
        "description":request.json.get("description"," "),
        "done":False
    } 
    task1.append(task2)
    return jsonify({
        "status":"sucess",
        "message":"task added sucessfully"
    })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":task1
    })
if(__name__=="__main__"):
    app.run(debug=True)