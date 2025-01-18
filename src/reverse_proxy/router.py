from flask import Flask, request, Response
import requests

app = Flask(__name__)

SITE_NAME = "http://localhost:5001/"

# Handle GET requests
@app.route('/<path:path>', methods=['GET'])
def proxy(path):
    if request.method == 'GET':
        print(f"Forwarding GET request to: {SITE_NAME}{path}")

        # Reverse proxy is requesting web server here
        resp = requests.get(f'{SITE_NAME}{path}')

        exclude_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for name, value in resp.raw.headers.items() if name.lower() not in exclude_headers]

        # Forwards response to client
        response = Response(resp.content, resp.status_code, headers)
        return response

# Handle POST requests
@app.route('/<path:path>', methods=['POST'])
def postproxy(path):
    if request.method == 'POST':
        print(f"Forwarding POST request to: {SITE_NAME}{path}")
        resp = requests.post(f'{SITE_NAME}{path}', json=request.get_json())

        exclude_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for name, value in resp.raw.headers.items() if name.lower() not in exclude_headers]

        response = Response(resp.content, resp.status_code, headers)
        return response

# Handle PUT requests
@app.route('/<path:path>', methods=['PUT'])
def putproxy(path):
    if request.method == 'PUT':
        print(f"Forwarding PUT request to: {SITE_NAME}{path}")
        resp = requests.put(f'{SITE_NAME}{path}', json=request.get_json())

        exclude_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for name, value in resp.raw.headers.items() if name.lower() not in exclude_headers]

        response = Response(resp.content, resp.status_code, headers)
        return response

# Handle DELETE requests
@app.route('/<path:path>', methods=['DELETE'])
def deleteproxy(path):
    if request.method == 'DELETE':
        print(f"Forwarding DELETE request to: {SITE_NAME}{path}")
        
        # Ensure no content type is set unless needed
        resp = requests.delete(f'{SITE_NAME}{path}', json=request.get_json() if request.get_json() else None)

        exclude_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for name, value in resp.raw.headers.items() if name.lower() not in exclude_headers]

        response = Response(resp.content, resp.status_code, headers)
        return response

# Handle PATCH requests
@app.route('/<path:path>', methods=['PATCH'])
def patchproxy(path):
    if request.method == 'PATCH':
        print(f"Forwarding PATCH request to: {SITE_NAME}{path}")
        resp = requests.patch(f'{SITE_NAME}{path}', json=request.get_json())

        exclude_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for name, value in resp.raw.headers.items() if name.lower() not in exclude_headers]

        response = Response(resp.content, resp.status_code, headers)
        return response

if __name__ == '__main__':
    app.run(debug=False, port=8100)
