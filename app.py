from flask import Flask, render_template, jsonify, request,make_response
from db_config import dbconnect


app = Flask(__name__)

conn    = dbconnect()
cursor = conn.cursor(dictionary=True)
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add-todo', methods=["POST"])
def addtodo():
    todo    = request.form.get('todo')
    query   = "INSERT INTO todos(todo) VALUES(%s)"
    args    = (todo,)
    
    cursor.execute(query, args)
    result = True if cursor.lastrowid else False
    conn.commit()
        
    return jsonify(result=result)

@app.route('/get-todo')
def gettodo():
    
    cursor.execute("SELECT * FROM todos ORDER BY id DESC")
    todos = cursor.fetchall()
    return make_response(jsonify(result=todos), 200)


@app.route('/delete-todo', methods=['POST'])
def deletetodo():
    id    = request.form.get('id')
    
    query = "DELETE FROM todos WHERE id = %s"
    cursor.execute(query, (id,))
    
    conn.commit()
    
    return make_response(jsonify(result=True), 200)

@app.route('/status-change-todo', methods=['POST'])
def statuschangetodo():
    id      = request.form.get('id')
    status  = request.form.get('status')
    
    query = "UPDATE todos SET status = %s WHERE id = %s"
    cursor = conn.cursor()
    cursor.execute(query, (status, id))
    conn.commit()
    
    return make_response(jsonify(result=True), 200)
    
if __name__ == '__main__':
    app.run(debug=True)