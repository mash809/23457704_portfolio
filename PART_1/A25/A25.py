import json
from typing import Dict, Any, List


def mask_email(email: str) -> str:
    """
    Mask an email address while keeping it readable enough for identification.
    Example: mashudulbiswas@example.com -> m*************s@example.com
    """
    if "@" not in email:
        return "[invalid email]"

    local, domain = email.split("@", 1)

    if len(local) <= 2:
        masked_local = local[0] + "*" * max(len(local) - 1, 0)
    else:
        masked_local = local[0] + "*" * (len(local) - 2) + local[-1]

    return f"{masked_local}@{domain}"


def mask_phone(phone: str) -> str:
    """
    Mask a phone number while keeping the last 2 digits visible.
    Example: 0412345678 -> ********78
    """
    digits_only = "".join(ch for ch in phone if ch.isdigit())

    if len(digits_only) <= 2:
        return "*" * len(digits_only)

    return "*" * (len(digits_only) - 2) + digits_only[-2:]


def extract_first_name(full_name: str) -> str:
    """
    Keep only the first name to reduce unnecessary data exposure.
    """
    parts = full_name.strip().split()
    return parts[0] if parts else ""


def extract_general_location(location: str) -> str:
    """
    Keep only a general location rather than a full address.
    """
    return location.strip()


def privacy_preserve_user_record(record: Dict[str, Any]) -> Dict[str, Any]:
    """
    Apply privacy-preserving transformations:
    - Keep only minimum necessary fields
    - Mask sensitive identifiers
    - Remove unnecessary personal details
    """
    preserved = {
        "first_name": extract_first_name(record.get("full_name", "")),
        "email_masked": mask_email(record.get("email", "")),
        "phone_masked": mask_phone(record.get("phone", "")),
        "general_location": extract_general_location(record.get("location", "")),
        "organisation": record.get("organisation", ""),
    }

    return preserved


def privacy_preserve_dataset(records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Process a list of user records.
    """
    return [privacy_preserve_user_record(record) for record in records]


def main() -> None:
    """
    Demo input data for the assignment.
    """
    sample_users = [
        {
            "full_name": "Mashudul Biswas",
            "email": "mashudulbiswas@example.com",
            "phone": "0412345678",
            "location": "Perth, Australia",
            "organisation": "University of Western Australia",
            "date_of_birth": "2002-01-15",
            "notes": "Student contact profile."
        },
        {
            "full_name": "Tasnia Rahman",
            "email": "tasniarahman@example.com",
            "phone": "0498765432",
            "location": "London, Canada",
            "organisation": "",
            "date_of_birth": "1999-08-20",
            "notes": "User profile for communication."
        }
    ]

    protected_users = privacy_preserve_dataset(sample_users)

    print("Original data:\n")
    print(json.dumps(sample_users, indent=4))

    print("\nPrivacy-preserved data:\n")
    print(json.dumps(protected_users, indent=4))


if __name__ == "__main__":
    main()
