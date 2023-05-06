from flask import Flask, jsonify, request
from algo import *
from flask_cors import CORS
password = "yasuo"

app = Flask(__name__)
CORS(app)
public_key, private_key = prepare()
@app.route('/api/public_key/', methods=['GET'])
def get_public_key():
    return jsonify(public_key)

@app.route('/api/private_key/', methods=['GET'])
def get_private_key():
    password_param = request.args.get('password')
    if password_param != password:
        return jsonify({'error': 'Invalid password'}), 401
    return jsonify(private_key)

@app.route('/api/encrypt/', methods=['GET'])
def get_encrypted_message():
    message = request.args.get('message')
    ascii_message = string_to_ascii(message)
    encrypted = encrypt(public_key, ascii_message)
    return jsonify(encrypted)

@app.route('/api/decrypt/', methods=['GET'])
def get_decrypted_message():
    encrypted = int(request.args.get('encrypted_message'))
    decrypted = decrypt(public_key, private_key, encrypted)
    return jsonify(ascii_to_string(decrypted))


if __name__ == '__main__':
    app.run(debug=True)