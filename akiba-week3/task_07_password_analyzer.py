
def check_minimum_length(password, minimum_length=8):
    """Check whether the password meets the minimum length."""
    return len(password) >= minimum_length


def check_uppercase(password):
    """Check whether the password contains an uppercase letter."""
    for character in password:
        if character.isupper():
            return True

    return False


def check_lowercase(password):
    """Check whether the password contains a lowercase letter."""
    for character in password:
        if character.islower():
            return True

    return False


def check_digit(password):
    """Check whether the password contains a digit."""
    for character in password:
        if character.isdigit():
            return True

    return False


def check_special_character(password):
    """Check whether the password contains a special character."""
    special_characters = "!@#$%^&*()-_=+[]{};:',.<>?/\\|`~\""

    for character in password:
        if character in special_characters:
            return True

    return False


def analyze_password(password, minimum_length=8):
    """Return a structured report of all password requirements."""

    checks = {
        "Minimum length": check_minimum_length(
            password, minimum_length
        ),
        "Uppercase letter": check_uppercase(password),
        "Lowercase letter": check_lowercase(password),
        "Digit": check_digit(password),
        "Special character": check_special_character(password)
    }

    missing_requirements = []

    for requirement, passed in checks.items():
        if not passed:
            missing_requirements.append(requirement)

    result = {
        "password_length": len(password),
        "minimum_length": minimum_length,
        "checks": checks,
        "missing_requirements": missing_requirements,
        "valid": len(missing_requirements) == 0
    }

    return result


def display_report(password, result):
    """Display the returned analysis in a readable format."""

    print("\nPassword:", password)
    print("-" * 40)

    for requirement, passed in result["checks"].items():
        status = "PASS" if passed else "FAIL"
        print(f"{requirement}: {status}")

    if result["valid"]:
        print("Result: Password meets all requirements.")
    else:
        print("Result: Password does not meet all requirements.")
        print("Missing requirements:")

        for requirement in result["missing_requirements"]:
            print("-", requirement)


def main():
    # Fictional passwords for testing only.
    test_passwords = [
        "Hello123!",
        "hello",
        "HELLO123!",
        "HelloWorld!",
        "12345678",
        "Abc12345"
    ]

    minimum_length = 8

    print("PASSWORD POLICY AND STRENGTH ANALYZER")
    print("=" * 40)
    print("Minimum required length:", minimum_length)

    for password in test_passwords:
        result = analyze_password(password, minimum_length)
        display_report(password, result)


if __name__ == "__main__":
    main()
