
def validate_units(units):
    """Check that consumption is a valid non-negative number."""
    return units >= 0


def calculate_tier_charges(units):
    """Calculate the charge for each consumption tier."""
    first_tier = 0
    second_tier = 0
    third_tier = 0

    if units <= 50:
        first_tier = units * 0.50

    elif units <= 150:
        first_tier = 50 * 0.50
        second_tier = (units - 50) * 0.75

    else:
        first_tier = 50 * 0.50
        second_tier = 100 * 0.75
        third_tier = (units - 150) * 1.20

    return {
        "first_tier": first_tier,
        "second_tier": second_tier,
        "third_tier": third_tier
    }


def calculate_total_bill(units, service_fee=0):
    """Calculate the bill, including an optional fixed service fee."""
    if not validate_units(units):
        raise ValueError("Units consumed cannot be negative.")

    if service_fee < 0:
        raise ValueError("Service fee cannot be negative.")

    tier_charges = calculate_tier_charges(units)

    energy_charge = (
        tier_charges["first_tier"]
        + tier_charges["second_tier"]
        + tier_charges["third_tier"]
    )

    total_bill = energy_charge + service_fee

    return total_bill


def generate_billing_summary(units, service_fee=0):
    """Generate a complete electricity billing summary."""
    if not validate_units(units):
        raise ValueError("Units consumed cannot be negative.")

    if service_fee < 0:
        raise ValueError("Service fee cannot be negative.")

    tier_charges = calculate_tier_charges(units)

    energy_charge = (
        tier_charges["first_tier"]
        + tier_charges["second_tier"]
        + tier_charges["third_tier"]
    )

    total_bill = calculate_total_bill(units, service_fee)

    summary = {
        "units_consumed": units,
        "first_50_units_charge": tier_charges["first_tier"],
        "next_100_units_charge": tier_charges["second_tier"],
        "above_150_units_charge": tier_charges["third_tier"],
        "energy_charge": energy_charge,
        "service_fee": service_fee,
        "total_bill": total_bill
    }

    return summary


def display_billing_summary(summary):
    """Display the billing summary in a readable format."""
    print("\nELECTRICITY BILL")
    print("=" * 40)

    print(f"Units consumed: {summary['units_consumed']:.2f}")
    print(
        "First 50 units charge: "
        f"{summary['first_50_units_charge']:.2f} Birr"
    )
    print(
        "Next 100 units charge: "
        f"{summary['next_100_units_charge']:.2f} Birr"
    )
    print(
        "Above 150 units charge: "
        f"{summary['above_150_units_charge']:.2f} Birr"
    )

    print("-" * 40)
    print(f"Energy charge: {summary['energy_charge']:.2f} Birr")
    print(f"Service fee: {summary['service_fee']:.2f} Birr")
    print(f"TOTAL BILL: {summary['total_bill']:.2f} Birr")
    print("=" * 40)


def main():
    print("ELECTRICITY BILL CALCULATOR")
    print("Rates are fictional assignment rates.")

    try:
        units = float(input("Enter units consumed: "))

        # Change this value to apply a fixed service fee.
        service_fee = 0.00

        if not validate_units(units):
            print("Error: Units consumed cannot be negative.")
            return

        summary = generate_billing_summary(
            units,
            service_fee=service_fee
        )

        display_billing_summary(summary)

    except ValueError:
        print("Error: Please enter a valid number.")


if __name__ == "__main__":
    main()
