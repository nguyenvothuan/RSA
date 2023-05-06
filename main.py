from flask import Flask, jsonify, request
from algo import *

password = "yasuo"

app = Flask(__name__)

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
    print(ascii_message)
    return jsonify(encrypt(public_key, ascii_message))

@app.route('/api/decrypt/', methods=['GET'])
def get_decrypted_message():
    encrypted = int(request.args.get('encrypted_message'))
    decrypted = decrypt(public_key, private_key, encrypted)
    return jsonify(ascii_to_string(decrypted))


if __name__ == '__main__':
    app.run(debug=True)