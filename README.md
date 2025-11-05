# Password-generator
This project is a Secure Password Generator built using Python to create strong, random, and customizable passwords. It is designed to help users protect their accounts and sensitive data by generating passwords that are difficult to guess or crack.

The program uses Python’s secrets and SystemRandom modules, which provide cryptographically secure randomization, ensuring that each password is unique and unpredictable. Users can control various aspects of the password such as its length, inclusion of uppercase letters, lowercase letters, digits, and symbols. It also provides options to exclude similar-looking characters (like I, l, 1, O, 0, etc.) or specific characters manually, and to avoid repeating consecutive characters for added complexity.

The tool includes a command-line interface (CLI), allowing users to easily generate passwords with their preferred settings using simple arguments. It also calculates the entropy of each password, providing a measure of its randomness and classifying it as weak, fair, strong, or very strong based on industry standards.

Additionally, this project comes with automated test cases using pytest to verify password length, strength, randomness, and rule enforcement, ensuring reliability and correctness.

Overall, this project demonstrates secure coding practices, proper random number generation for cryptography, and modular Python design — making it an excellent tool for personal use, academic learning, or integration into larger security focused applications.
