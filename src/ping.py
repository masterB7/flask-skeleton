from flask_restful import Resource

# ping handler
class Ping(Resource):
    def get(self):
        return {
            "version":"v1.0",
            "key":"ping"
        }