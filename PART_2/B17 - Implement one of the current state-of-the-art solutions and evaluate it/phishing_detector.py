import re
from typing import List, Tuple


SUSPICIOUS_KEYWORDS = [
    "urgent",
    "immediately",
    "verify your account",
    "account suspended",
    "click here",
    "login now",
    "confirm your password",
    "one-time passcode",
    "otp",
    "bank",
    "security alert",
    "payment failed",
    "update your details",
    "limited time",
]

SAFE_DOMAINS = [
    "google.com",
    "microsoft.com",
    "github.com",
    "uwa.edu.au",
]


def extract_urls(text: str) -> List[str]:
    """
    Extract URLs from text using a simple regular expression.
    """
    return re.findall(r"https?://[^\s]+", text)


def is_suspicious_url(url: str) -> bool:
    """
    Check if a URL looks suspicious.
    A URL is suspicious if:
    - it uses an IP address
    - it contains a lot of hyphens
    - it is not from a known safe domain
    """
    if re.search(r"https?://\d+\.\d+\.\d+\.\d+", url):
        return True

    if url.count("-") >= 2:
        return True

    for domain in SAFE_DOMAINS:
        if domain in url:
            return False

    return True


def analyse_message(message: str) -> Tuple[str, int, List[str]]:
    """
    Analyse a message and return:
    - result label
    - risk score
    - reasons
    """
    score = 0
    reasons = []
    lower_message = message.lower()

    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in lower_message:
            score += 1
            reasons.append(f"Contains suspicious phrase: '{keyword}'")

    urls = extract_urls(message)
    if urls:
        for url in urls:
            if is_suspicious_url(url):
                score += 2
                reasons.append(f"Suspicious URL found: {url}")
            else:
                reasons.append(f"URL found but appears safer: {url}")

    if message.count("!") >= 2:
        score += 1
        reasons.append("Uses excessive urgency or punctuation")

    if score >= 4:
        result = "Likely Phishing"
    elif score >= 2:
        result = "Suspicious"
    else:
        result = "Probably Safe"

    return result, score, reasons


def run_demo() -> None:
    """
    Demo using sample messages.
    """
    sample_messages = [
        "Urgent! Your bank account has been suspended. Click here immediately to verify your account: http://192.168.1.1/login",
        "Hi, here is the GitHub link for our project update: https://github.com/example/repo",
        "Security alert! Confirm your password now at http://secure-bank-login-update.com",
        "Your UWA class has been moved to another room. Please check official university announcements.",
    ]

    for i, message in enumerate(sample_messages, start=1):
        result, score, reasons = analyse_message(message)

        print("=" * 60)
        print(f"Message {i}:")
        print(message)
        print(f"\nResult: {result}")
        print(f"Risk Score: {score}")
        print("Reasons:")
        for reason in reasons:
            print(f"- {reason}")
        print()


def main() -> None:
    """
    Allow either demo mode or user input mode.
    """
    print("Simple Phishing Detector")
    print("1. Run demo")
    print("2. Check your own message")
    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "1":
        run_demo()
    elif choice == "2":
        user_message = input("\nPaste the message to analyse:\n")
        result, score, reasons = analyse_message(user_message)

        print("\nResult:", result)
        print("Risk Score:", score)
        print("Reasons:")
        for reason in reasons:
            print(f"- {reason}")
    else:
        print("Invalid option. Please run the program again and choose 1 or 2.")


if __name__ == "__main__":
    main()