from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_student_number():
    return jsonify({"student_number": "200537749"})

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    fulfillmentText = 'xxx'
    query_result = req.get('queryResult')
    if query_result.get('action') == 'get.address':
        ### Perform set of executable code
        ### if required
        ### ...

        fulfillmentText = "Hi .. i am in"
    return {
            "fulfillmentText": fulfillmentText,
            "source": "webhookdata"
        }

if __name__ == '__main__':
    app.run(debug=True)
