from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

users = {'user1': 'hello',
         'user2': 'hi',
         'edwin': "I'm an author of this"}


class User(Resource):
    def get(self, user_id):
        if user_id not in users:
            return {"message": "User not found"}, 404
        return users[user_id]

    def post(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("age")
        args = parser.parse_args()

        if user_id in users:
            return {"message": "User already exists"}, 400

        users[user_id] = {"name": args["name"], "age": args["age"]}
        return users[user_id], 201

    def put(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("age")
        args = parser.parse_args()

        if user_id not in users:
            return {"message": "User not found"}, 404

        users[user_id] = {"name": args["name"], "age": args["age"]}
        return users[user_id]

    def delete(self, user_id):
        if user_id not in users:
            return {"message": "User not found"}, 404
        del users[user_id]
        return {"message": "User deleted"}


api.add_resource(User, "/user/<string:user_id>")

if __name__ == "__main__":
    app.run(debug=True)
