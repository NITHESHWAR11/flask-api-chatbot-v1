from flask import Flask, jsonify, request
from flask_restful import Api, Resource

import trainer

app = Flask(__name__)
api = Api(app)

class ChatBot(Resource):
    def post(self):
        user_input = request.json['user_input']
        response =  jsonify({'bot': str(trainer.response(user_input))})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
api.add_resource(ChatBot, "/api/bot/")

if __name__ == '__main__':
    app.run(debug=True, port=8000)
