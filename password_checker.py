import math
import string
import os


def load_common_passwords():
    file_path = os.path.join(
        os.path.dirname(__file__),
        "common_passwords.txt"
    )

    try:
        with open(file_path, "r") as file:
            return {
                line.strip().lower()
                for line in file
                if line.strip()
            }
    except FileNotFoundError:
        return set()


def calculate_entropy(password):
    pool = 0

    if any(c.islower() for c in password):
        pool += 26

    if any(c.isupper() for c in password):
        pool += 26

    if any(c.isdigit() for c in password):
        pool += 10

    if any(c in string.punctuation for c in password):
        pool += 32

    if pool == 0:
        return 0

    entropy = len(password) * math.log2(pool)

    return round(entropy, 2)


def check_password(password):

    score = 0
    feedback = []

    # 1. Check password length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        feedback.append("Use at least 12 characters.")
    else:
        feedback.append("Increase password length to at least 12 characters.")

    # 2. Check lowercase letters
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letters (a-z).")

    # 3. Check uppercase letters
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters (A-Z).")

    # 4. Check digits
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add numbers (0-9).")

    # 5. Check special characters
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Add special characters (@, #, $, !).")

    # 6. Check common passwords
    common_passwords = load_common_passwords()

    if password.lower() in common_passwords:
        score = 0
        feedback.append("This is a commonly used password. Avoid it.")

    # 7. Calculate entropy
    entropy = calculate_entropy(password)

    # 8. Classify password strength
    if password.lower() in common_passwords:
        strength = "Weak"
    elif score <= 2 or entropy < 40:
        strength = "Weak"
    elif score <= 4 or entropy < 60:
        strength = "Moderate"
    elif score <= 5 or entropy < 80:
        strength = "Strong"
    else:
        strength = "Exceptional"

    # 9. Return results
    return {
        "score": score,
        "entropy": entropy,
        "strength": strength,
        "feedback": feedback
    }  