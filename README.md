# The RSA Algorithm: Implementation and Technical Analysis

## Project overview
This project is an implementation of the RSA algorithm in Python, using cryptographic libraries to work with ciphertext and large primes. The Flask framework is used to host a server that exposes four APIs: one to get the public key, one to get the private key with password authentication, one to encrypt a message using the public key, and one to decrypt a message using the private key. The client is implemented using Vanilla JavaScript consumes these APIs.

This readme provides technical instructions on the project's structure, the functionality of each file and function, and how to test these functions. Additionally, in the root directory of this project, a short paper about the RSA algorithm that covers the algorithm's history, proof of correctness, and asymptotic analysis is included for further reading.
## Function description:
- `cook()`: returns a tuple of 2 very large primes `p` and `q`
- `prepare()`: generate `p` and `q` from `cook()` and return two objects public_key: `(N,e)` and private_key: `(ϕ, d)`. 
- `encrypt(public_key, message)`: takes in a message and return the encrypted message using the RSA algorithm
- `decrypt(public_key, private_key, encrypted_message)`: takes in an encrypted message and decrypt it using the two keys
- `brute_force_decrypt(public_key, encrypted_message)`: attempt to decrypt the message using only public key.

## Project Demo: 
[Loom Video](https://www.loom.com/share/e338555d144a4e61ab0cb492d411e928)
## Project structure
```
├── client
│   ├── index.html
│   └── script.js
|   └── styling.css
├── algo.py
├── main.py
└── test.py
```
## How to run the project:
- 