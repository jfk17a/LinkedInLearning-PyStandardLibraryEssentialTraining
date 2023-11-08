# Using cryptographic-appropriate methods to generate random data
# that may be sensitive. secrets module introduced in Python 3.6
import os
import secrets


# TODO: the urandom() function in the OS module produces random numbers that
# are cryptographically safe to use for sensitive purposes
result = os.urandom(8)
# print([hex(b) for b in result])

# TODO: secrets.choice is the same as random.choice but more secure
moves = ["rock", "paper", "scissors"]
# print(secrets.choice(moves))

# TODO: secrets.token_bytes generates random bytes
results = secrets.token_bytes(8)
print(results)

# TODO: secrets.token_hex creates a random string in hexadecimal
results = secrets.token_hex(8)
print(results)

# TODO: secrets.token_urlsafe generates characters that can be in URLs
results = secrets.token_urlsafe()
print(results)