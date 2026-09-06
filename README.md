# Password Strength Analyzer

A simple command-line password strength analyzer written in Python.

The program checks a password using several basic security rules and gives it a score from **0 to 6**.

## Features

The analyzer checks whether the password:

* Is not in the common password list
* Has at least 8 characters
* Contains a digit
* Contains an uppercase letter
* Contains a lowercase letter
* Contains a special character

Each passed check gives the password **1 point**.

## Strength Levels

| Score | Strength |
| ----: | -------- |
|   0–2 | Weak     |
|   3–4 | Medium   |
|   5–6 | Strong   |

## Example

```text
enter password: Example123!

correct
correct
has number
Has uppercase
Has lowercase
correct

result = 6/6
strength = Strong
```

## How It Works

The program performs six checks:

### 1. Common Password Check

Checks whether the entered password exists in the built-in list of common passwords.

### 2. Length Check

Checks whether the password has at least 8 characters.

### 3. Digit Check

Checks whether the password contains at least one number.

### 4. Uppercase Check

Checks whether the password contains at least one uppercase letter.

### 5. Lowercase Check

Checks whether the password contains at least one lowercase letter.

### 6. Special Character Check

Checks whether the password contains at least one non-alphanumeric character.

After all checks are completed, the program calculates the total score and determines the password strength.

## Requirements

* Python 3.x

No external libraries are required.

## Installation

Clone the repository:

```bash
git clone https://github.com/amiralikazemi1321/password-strength-analyzer.git
```

Enter the project directory:

```bash
cd password-strength-analyzer
```

## Usage

Run the program with:

```bash
python main.py
```

Enter a password when prompted.

## Project Structure

```text
password-strength-analyzer/
├── main.py
├── README.md
└── LICENSE
```

## Project Status

**Version 1.0**

This is a simple command-line project built with Python to practice:

* Functions
* Conditional statements
* String methods
* Lists
* Boolean values
* Basic password-strength checking

## Security Note

This project is an educational password checker and should not be considered a professional password security analyzer.

Passing all six checks does not necessarily mean that a password is secure. Real-world password security involves many additional factors.

**Never enter a real password into a program or service that you do not trust.**

## Future Improvements

Possible improvements for future versions:

* Detect repeated characters
* Detect sequential patterns such as `123456`
* Improve common-password detection
* Add password entropy estimation
* Improve the scoring system
* Add automated tests
* Add command-line arguments

## License

This project is licensed under the MIT License.
