from algo import *
import random
import string

def generate_random_string(length):
    # Define the possible characters for the random string
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    
    # Use random.choices() to select random characters from the letters string
    random_string = ''.join(random.choices(letters, k=length))
    return random_string

def test_ascii_conversion():
    # Test the ascii conversion functions 10 times
    for i in range(10):        
        random_string = generate_random_string(10)
        m = string_to_ascii(random_string)
        assert ascii_to_string(m) == random_string
        print("Test ascii conversion passed against random string: " + random_string)
    
def test_encrypt_decrypt():
    # Test the encrypt and decrypt functions 10 times
    for i in range(10):
        random_string = generate_random_string(10)
        m = string_to_ascii(random_string)
        public_key, private_key = prepare()
        c = encrypt(public_key, m)
        assert decrypt(public_key, private_key, c) == m
        print("Test encrypt and decrypt passed against random string: " + random_string)

# Run the tests
test_ascii_conversion()    
test_encrypt_decrypt()

    