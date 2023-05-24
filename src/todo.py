from flask import Flask
from flask_restful import reqparse, abort, Resource

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}

def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

## 定义请求参数
parser = reqparse.RequestParser()
# location 代表该参数从哪里进行获取默认是 json 请求体方式进行解析
# 如果想从表单中获取则可以用 form
# 详细可参考 https://flask-restful.readthedocs.io/en/latest/reqparse.html
parser.add_argument('task')

# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    ## http get 方法
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201

# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        ## args 代表请求参数 ，默认参数是 
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        ## 返回的第一个参数是返回值，是 json 格式
        ## 返回的第二个参数是 http code 
        return TODOS[todo_id], 201
