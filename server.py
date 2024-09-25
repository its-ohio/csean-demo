from pprint import pprint
from flask import Flask, request

from models.utils import logger

app = Flask(__name__)


@app.route('/mark_reply', methods=['POST'])
def mark_reply():
    logger.info("Webhook Received")
    payload = request.json

    print(payload["from_email"])
    print(payload["body"])

    return [200]


if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server
    app.run(host='0.0.0.0', port=8080)
