# Atbash Cipher – Python Implementation

The Atbash Cipher is a classical substitution cipher where each letter of the alphabet is replaced by its opposite counterpart.

This project implements the Atbash cipher in Python, supporting both uppercase and lowercase letters, while preserving spaces, numbers, and symbols.

## Features

Same function encrypts and decrypts
Supports uppercase & lowercase alphabets
Leaves spaces, digits, and special characters unchanged
Efficient logic using ASCII values
Clean, readable, beginner-friendly code

## How the Atbash Cipher Works

Instead of storing mappings in a dictionary, the final version uses ASCII arithmetic:

<img width="585" height="268" alt="image" src="https://github.com/user-attachments/assets/de4a9361-1ba8-4006-816f-e5296f9654a6" />

Because of this symmetry, encrypting twice gives you the original text back.

## Base Prototype (Dictionary Approach)

Before the final version, a dictionary-based prototype was created where each letter was manually mapped to its opposite.

Why it was improved:

Required explicit mappings
Only handled uppercase letters
Less scalable

The final version replaces this with dynamic ASCII-based logic, making the solution:

Shorter
Smarter
More flexible

<img width="904" height="298" alt="Screenshot From 2026-01-28 18-44-42" src="https://github.com/user-attachments/assets/344f026b-2400-40fe-8148-dc80ea8bc63c" />

## Learning Outcomes

Understanding classical cryptography
Practical use of ord() and chr()
Character range checks in Python
Writing reversible algorithms

## Possible Enhancements

Add file encryption support
Extend for full Unicode alphabets
Combine with other classical ciphers

## License

This project is open for learning and experimentation.
Use it, break it, improve it
