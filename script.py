from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_student_number():
    return jsonify({"student_number": "200537749"})

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # Process the request data from Dialogflow
    # Here, you can add your logic to handle Dialogflow requests and generate a response
    response_text = "This is the response from the webhook endpoint."
    return jsonify({"fulfillmentText": response_text})

if __name__ == '__main__':
    app.run(debug=True)
