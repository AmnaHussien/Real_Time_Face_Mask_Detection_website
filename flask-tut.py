from flask import Flask, jsonify, request, abort

app = Flask(__name__)

#todos defined in form of array of dictionary
todos = [
    {
    'id':1,
    'title':'flask',
    'description':'learn from youtube',
    'done':False
    },
    {
    'id':2,
    'title':'python',
    'description':'also from youtube',
    'done':True
    }
]


@app.route("/todos", methods=['GET'])
def get_todos():
    return jsonify({'todos':todos})

@app.route("/todos/<int:todo_id>", methods=['GET'])
def get_todo(todo_id):
    todo = [todo for todo in todos if todo["id"] == todo_id]
    if len(todo) == 0:
        abort(404)
    return jsonify({'todo':todo[0]})
@app.route("/todos", methods=['POST'])
def create_todo():
    if not request.json or not 'title' in request.json:
        abort(400)
    todo = {
        'id':todos[-1]['id'] + 1,
        'title':request.json.get('title'),
        'description':request.json.get('description'),
        'done':False
    }
    todos.append(todo)

    return jsonify({"todos":todos})
@app.route("/todos/todo_id", methods=['POST'])
def update_todo(todo_id):
    todo = [todo for todo in todos if todo['id'] == todo_id]
    if len(todo) == 0 :
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != str:
        abort(400)
    if 'description' in request.json and type(request.json['description']) != str:
        abort(400)
    if 'done' in request.json and type(request.json['done']) != str:
        abort(400)
    todo[0]['title'] = request.json.get('title', todo[0]['title'])
    todo[0]['description'] = request.json.get('description', todo[0]['description'])
    todo[0]['done'] = request.json.get('done', todo[0]['done'])
    todo[todo_id] = todo[0]
    return jsonify({'todos':todo[0]})
if __name__ == "__main__":
    app.run(debug=True)