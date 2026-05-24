from typing import Dict, List


KNOWN_MALICIOUS_IPS = {
    "185.243.115.84": "Known malicious IP linked to phishing activity",
    "103.21.244.10": "Suspicious IP reported in scam campaigns",
    "45.67.89.200": "Example malicious command-and-control style IP"
}

KNOWN_MALICIOUS_DOMAINS = {
    "secure-login-check.com": "Fake login website",
    "verify-account-now.net": "Phishing-style domain",
    "bank-alert-update.com": "Suspicious banking scam domain"
}

SUSPICIOUS_KEYWORDS = {
    "verify your account": "Common phishing phrase",
    "urgent action required": "Urgency-based scam wording",
    "confirm your password": "Credential theft phrase",
    "one-time passcode": "Sensitive code request",
    "account suspended": "Fear-based phishing phrase"
}


def check_ip(indicator: str) -> str:
    """
    Check whether an IP address exists in the malicious IP list.
    """
    if indicator in KNOWN_MALICIOUS_IPS:
        return f"Known Malicious IP: {KNOWN_MALICIOUS_IPS[indicator]}"
    return "No match found in malicious IP database"


def check_domain(indicator: str) -> str:
    """
    Check whether a domain exists in the malicious domain list.
    """
    if indicator in KNOWN_MALICIOUS_DOMAINS:
        return f"Known Malicious Domain: {KNOWN_MALICIOUS_DOMAINS[indicator]}"
    return "No match found in malicious domain database"


def check_keywords(text: str) -> List[str]:
    """
    Check text for suspicious phishing-style keywords.
    """
    matches = []
    lower_text = text.lower()

    for keyword, reason in SUSPICIOUS_KEYWORDS.items():
        if keyword in lower_text:
            matches.append(f"Suspicious Keyword Detected: '{keyword}' - {reason}")

    return matches


def analyse_indicator(user_input: str) -> None:
    """
    Analyse user input against the threat intelligence lists.
    """
    print("\nThreat Intelligence Result")
    print("-" * 40)

    ip_result = check_ip(user_input)
    domain_result = check_domain(user_input)
    keyword_results = check_keywords(user_input)

    found_match = False

    if "Known Malicious" in ip_result:
        print(ip_result)
        found_match = True

    if "Known Malicious" in domain_result:
        print(domain_result)
        found_match = True

    if keyword_results:
        for result in keyword_results:
            print(result)
        found_match = True

    if not found_match:
        print("Indicator appears safe or unknown based on the current threat database.")


def run_demo() -> None:
    """
    Run demo examples.
    """
    examples = [
        "185.243.115.84",
        "secure-login-check.com",
        "Urgent action required. Verify your account immediately.",
        "github.com"
    ]

    for example in examples:
        print("\n" + "=" * 50)
        print(f"Input: {example}")
        analyse_indicator(example)


def main() -> None:
    """
    Main menu.
    """
    print("Simple Threat Intelligence Module")
    print("1. Run demo examples")
    print("2. Check your own indicator or message")

    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "1":
        run_demo()
    elif choice == "2":
        user_input = input("\nEnter an IP, domain, or message to analyse:\n").strip()
        analyse_indicator(user_input)
    else:
        print("Invalid option. Please run the program again.")


if __name__ == "__main__":
    main()