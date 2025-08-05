from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/status')
def status():
    return jsonify({
        'status': 'ok',
        'service': 'flask-demo',
        'environment': app.config.get('ENV', 'production')
    })

@app.route('/api/data')
def data():
    return jsonify({
        'message': 'This is a multi-stage Flask application',
        'items': [
            {'id': 1, 'name': 'Item 1'},
            {'id': 2, 'name': 'Item 2'},
            {'id': 3, 'name': 'Item 3'}
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)