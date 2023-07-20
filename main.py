from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

@app.route('/ping', methods=['GET', 'POST', 'PUT', 'DELETE'])
def ping():
    if request.method == 'GET':
        return jsonify({'hola': 'chau'})
    elif request.method == 'POST':
        return jsonify({'hola': 'chau'})
    elif request.method == 'PUT':
        return jsonify({'hola': 'chau'})
    elif request.method == 'DELETE':
        return jsonify({'hola': 'chau'})

if __name__ == '__main__':
  app.run(port=5000, debug=True)
