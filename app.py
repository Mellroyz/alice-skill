from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/alice', methods=['POST'])
def alice():
    command = request.json['request']['command']
    return jsonify({
        'response': {
            'text': f'Вы сказали: {command}',
            'end_session': False
        },
        'version': '1.0'
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)