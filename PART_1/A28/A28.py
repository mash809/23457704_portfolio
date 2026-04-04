import re
from typing import List, Tuple


COMMON_WEAK_PASSWORDS = {
    "password",
    "password123",
    "123456",
    "12345678",
    "qwerty",
    "admin",
    "welcome",
    "iloveyou",
    "abc123",
    "letmein",
}


def evaluate_password(password: str) -> Tuple[str, List[str]]:
    """
    Evaluate the strength of a password and return:
    - strength label
    - list of feedback messages
    """
    feedback: List[str] = []
    score = 0

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters, preferably 12 or more.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    if re.search(r"[!@#$%^&*()_\-+=\[\]{};:'\",.<>/?\\|`~]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    if password.lower() in COMMON_WEAK_PASSWORDS:
        feedback.append("This password is too common and easy to guess.")
        return "Very Weak", feedback

    if len(password.strip()) != len(password):
        feedback.append("Avoid leading or trailing spaces unless intentional.")

    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Moderate"
    elif score == 5:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength, feedback


def main() -> None:
    """
    Run the password strength checker in the terminal.
    """
    print("Password Strength Checker")
    print("-" * 30)

    password = input("Enter a password to test: ")

    strength, feedback = evaluate_password(password)

    print(f"\nPassword strength: {strength}")

    if feedback:
        print("\nSuggestions:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("\nThis password meets all major strength checks.")


if __name__ == "__main__":
    main()
