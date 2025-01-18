from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample web services/application
@app.route('/status', methods=['GET'])
def status():
    return 'Flask application is up and running!'

@app.route('/greet', methods=['GET'])
def greet_user():
    return jsonify(message='Hey, Cohere! My name is Brian.')

@app.route('/ping', methods=['GET'])
def ping_server():
    return jsonify(ping='pong')

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify(data), 201

@app.route('/update-message', methods=['PUT'])
def update_message():
    data = request.get_json()
    return jsonify(updated_message=f"Updated to: {data.get('message')}"), 200

@app.route('/delete-item/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    return jsonify(message=f"Item with ID {item_id} deleted successfully"), 200

@app.route('/form-submit', methods=['POST'])
def form_submit():
    form_data = request.form
    return jsonify(form_data=form_data.to_dict()), 200

@app.route('/query-test', methods=['GET'])
def query_test():
    param = request.args.get('param', 'default_value')
    return jsonify(query_param=param)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
