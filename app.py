from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import os
import requests
app = Flask(__name__)
api = Api(app)


class PrankTexts(Resource):
    def get(self):
        return {'Prank Texts': 'Active'}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'phone', type=str, help='phone number is a rewuired field.', required=True)
        parser.add_argument(
            'msg', type=str, help='message is a required field.', required=True)
        parser.add_argument(
            'count', type=int, help='number of messages that need to be said is required', required=True)
        requested_data = parser.parse_args(strict=True)
        count = requested_data['count']
        while count > 0:
            requests.post(os.environ['TILL_URL'], json={
                "phone": [requested_data['phone']],
                "text": requested_data['msg']
            })
            count = count-1
        return 200


api.add_resource(PrankTexts, '/prank')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("PORT", 5000))
