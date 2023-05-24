from flask import Flask
from flask_restful import Api
import ping
import todo

app = Flask(__name__)
api = Api(app)

##  
## add router
## 这三个为示例的 router
api.add_resource(ping.Ping,'/ping')
api.add_resource(todo.TodoList, '/todos')
api.add_resource(todo.Todo, '/todos/<todo_id>')

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8080,
        debug=True
    )