ROLES = {
    "student": ["view own grades", "view timetable"],
    "lecturer": ["view own grades", "view timetable", "enter grades", "edit course material"],
    "administrator": ["view own grades", "view timetable", "enter grades", "edit course material", "manage users", "view all records"]
}


def check_access(role, action):
    """
    Check if a given role is allowed to perform a given action.
    """
    allowed_actions = ROLES.get(role.lower(), [])
    return action.lower() in allowed_actions


def show_permissions():
    """
    Display the available roles and their permissions.
    """
    print("\nAvailable roles and permissions:")
    for role, actions in ROLES.items():
        print(f"\n{role.title()}:")
        for action in actions:
            print(f"- {action}")


def main():
    print("Simple Role-Based Access Control System")
    show_permissions()

    role = input("\nEnter a role (student, lecturer, administrator): ").strip().lower()
    action = input("Enter an action to test: ").strip().lower()

    if check_access(role, action):
        print("\nAccess Granted")
        print(f"The role '{role}' is allowed to perform '{action}'.")
    else:
        print("\nAccess Denied")
        print(f"The role '{role}' is not allowed to perform '{action}'.")


if __name__ == "__main__":
    main()