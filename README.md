# Password Strength Analyzer

A simple password strength analyzer written in Python.

This project checks a password using several basic security rules and gives it a score from 0 to 6.

## Features

The analyzer checks whether the password:

- Is not a common password
- Has at least 8 characters
- Contains a digit
- Contains an uppercase letter
- Contains a lowercase letter
- Contains a special character

Each passed check gives the password 1 point.

## Strength Levels

| Score | Strength |
|-------|----------|
| 0–2   | Weak     |
| 3–4   | Medium   |
| 5–6   | Strong   |

## Example

```text
Enter password: Example123!

correct
correct
has number
Has uppercase
Has lowercase
correct

result = 6/6
strength = Strong