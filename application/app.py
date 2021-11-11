from flask import Flask, request
from flask_expects_json import expects_json
from pymongo import MongoClient
import json

app = Flask(__name__)

client = MongoClient('mongodb://mongo:27017/')
db = client['reminders']

reminder_schema = {
    'type': 'object',
    'properties': {
        'time': {'type': 'string'},
        'message': {'type': 'string'},
    },
    'required': ['time', 'message']
}


@app.route('/api/reminders', methods=['GET', 'POST'])
@expects_json(reminder_schema, ignore_for=['GET'])
def reminders():
    """
    Add or retrieve reminders api
    """
    if request.method == 'POST':
        reminder = request.get_json()
        db['reminders'].insert_one(reminder)

        return 'Reminder created\n', 201, {'ContentType':'text/html'}

    reminders = db['reminders'].find({}, {'_id': False})

    return json.dumps(list(reminders), indent=2)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)