
def is_prime(number):
    """Check whether a number is prime."""
    if number < 2:
        return False

    divisor = 2

    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1

    return True


def get_divisors(number):
    """Return all positive divisors of a positive number."""
    divisors = []

    if number <= 0:
        return divisors

    divisor = 1

    while divisor <= number:
        if number % divisor == 0:
            divisors.append(divisor)
        divisor += 1

    return divisors


def sum_of_digits(number):
    """Calculate the sum of a number's digits."""
    number = abs(number)
    total = 0

    while number > 0:
        digit = number % 10
        total += digit
        number //= 10

    return total


def reverse_number(number):
    """Reverse the digits and preserve the sign."""
    sign = -1 if number < 0 else 1
    number = abs(number)
    reversed_value = 0

    while number > 0:
        digit = number % 10
        reversed_value = reversed_value * 10 + digit
        number //= 10

    return sign * reversed_value


def analyze_number(number):
    """Return a complete analysis of an integer."""

    if number == 0:
        number_type = "Zero"
    elif number % 2 == 0:
        number_type = "Even"
    else:
        number_type = "Odd"

    analysis = {
        "Number": number,
        "Even or Odd": number_type,
        "Is Prime": is_prime(number),
        "Sum of Digits": sum_of_digits(number),
        "Reversed Number": reverse_number(number),
        "Divisors": get_divisors(number)
    }

    return analysis


def main():
    print("ADVANCED NUMBER ANALYZER")
    print("=" * 30)

    try:
        number = int(input("Enter an integer: "))

        result = analyze_number(number)

        print("\nNUMBER ANALYSIS")
        print("-" * 30)

        for key, value in result.items():
            print(f"{key}: {value}")

    except ValueError:
        print("Invalid input! Please enter a whole number.")


# Start the program
if __name__ == "__main__":
    main()
