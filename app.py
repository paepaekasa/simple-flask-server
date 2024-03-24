from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return {'message': 'Hello guys this is a server'}

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    if 'a' in data and 'b' in data:
        a = data['a']
        b = data['b']
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            result = a + b
            return jsonify({'message': f'The sum of {a} and {b} is {result}'})
        else:
            return jsonify({'error': 'Both values should be numbers'}), 400
    else:
        return jsonify({'error': 'Both values should be provided as "a" and "b"'}), 400

if __name__ == '__main__':
    app.run(port=3000, debug=True)
