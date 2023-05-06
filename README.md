# Function description:
- `cook()`: returns a tuple of 2 very large primes `p` and `q`
- `prepare()`: generate `p` and `q` from `cook()` and return two objects public_key: `(N,e)` and private_key: `(ϕ, d)`. 
- `encrypt(public_key, message)`: takes in a message and return the encrypted message using the RSA algorithm
- `decrypt(public_key, private_key, encrypted_message)`: takes in an encrypted message and decrypt it using the two keys
- `brute_force_decrypt(public_key, encrypted_message)`: attempt to decrypt the message using only public key.

# How to run the project:
- 