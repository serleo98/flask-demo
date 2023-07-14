from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/ping', methods=['GET', 'POST', 'PUT', 'DELETE'])
def ping():
    if request.method == 'GET':
        return 'GET request received'
    elif request.method == 'POST':
        return 'POST request received'
    elif request.method == 'PUT':
        return 'PUT request received'
    elif request.method == 'DELETE':
        return 'DELETE request received'

if __name__ == '__main__':
  app.run(port=5000, debug=True)
