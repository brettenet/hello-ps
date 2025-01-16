from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/api/message', methods=['GET'])
def get_message():
    try:
        response = requests.get('http://server:5001/api/get-string')
        response.raise_for_status()
        data = response.json()
        return jsonify({"message": data["message"]})
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
