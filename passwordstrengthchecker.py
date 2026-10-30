def check_password_strength(password):
    """Checks a password and returns a list of problems found."""
    issues = []

    # Length check
    if len(password) < 8:
        issues.append("Make it at least 8 characters long.")

    # Character type checks
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        else:
            has_special = True

    if not has_upper:
        issues.append("Add at least one uppercase letter (A-Z).")
    if not has_lower:
        issues.append("Add at least one lowercase letter (a-z).")
    if not has_digit:
        issues.append("Add at least one number (0-9).")
    if not has_special:
        issues.append("Add at least one special character (e.g. @, #, $, !, %).")

    return issues


def main():
    print("=== Password Strength Checker ===")
    password = input("Enter a password to check: ")

    issues = check_password_strength(password)

    if not issues:
        print("\n Strong password! Good job.")
    else:
        print("\n Weak password. Here's how to improve it:")
        for i, tip in enumerate(issues, start=1):
            print(f"  {i}. {tip}")


if __name__ == "__main__":
    main()