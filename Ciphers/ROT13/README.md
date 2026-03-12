# ROT13 Cipher in Python
A simple Python implementation of the ROT13 (Rotate by 13 places) cipher with both encryption and decryption functions.

ROT13 is a classic substitution cipher that shifts each alphabet letter 13 positions forward in the alphabet. If the shift goes past Z, it wraps back to A.

Because the English alphabet has 26 letters, applying ROT13 twice returns the original text.

```
ROT13(ROT13(text)) = Original Text
```
## Features

- Encrypt text using ROT13
- Decrypt ROT13 encoded text
- Supports uppercase and lowercase characters
- Keeps numbers, spaces, and symbols unchanged
- Lightweight and beginner-friendly Python implementation

## Technologies Used

- Python 3
- Built-in functions:
  - ord()
  - chr()
- modulo arithmetic

