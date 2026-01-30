# Caesar Cipher in Python
A simple and educational implementation of the Caesar Cipher written in Python.

## What Is a Caesar Cipher?
The Caesar Cipher is a substitution cipher where each letter in the text is shifted by a fixed number of positions in the alphabet.

Shift = 3

A → D

B → E

Z → C

It works for both uppercase and lowercase letters, while leaving symbols and spaces untouched.

## Features

Encrypt text with a custom shift value

Decrypt text when the shift is known
 
Brute-force decryption when the shift is unknown
 
Supports uppercase & lowercase letters
 
Beginner-friendly and easy to modify

 ## How to Run
### Encryption

python encrypt.py

You’ll be asked for:

Original text

Shift value

### Decryption (Known Shift)

python decrypt.py

You’ll be asked for:

Encrypted text

Shift value

### Brute Force Decryption
python brute_force_decrypt.py

Tries all 25 possible shifts

Useful when the shift value is unknown

Prints every possible decrypted output

### Concepts Used

ASCII values (ord() and chr())

Modulo arithmetic

Loops and conditionals

String manipulation

### Future Improvements
Support for file encryption

Combine multiple ciphers into one toolkit

### License

This project is open-source and free to use for learning and experimentation.
