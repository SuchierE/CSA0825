
# TASK 9: Implement and Test the Milk Payment Calculator

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

MIN_FAT = 2.0
MAX_FAT = 7.0
MIN_SNF = 0.0
MAX_SNF = 15.0


def rate_per_litre(fat, snf):
    """Calculate milk rate using the 3.5% fat and 8.5% SNF base."""
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)

    rate = (
        BASE_RATE
        + fat_steps * FAT_STEP_VALUE
        + snf_steps * SNF_STEP_VALUE
    )
    return round(rate, 2)


def payout(litres, fat, snf):
    """Return the payment for a valid milk entry."""
    validate_entry(litres, fat, snf)
    return round(litres * rate_per_litre(fat, snf), 2)


def validate_entry(litres, fat, snf):
    """Reject invalid quantities and milk quality values."""
    if not all(isinstance(x, (int, float)) for x in (litres, fat, snf)):
        raise ValueError("Litres, fat and SNF must be numbers")

    if not all(__import__("math").isfinite(x) for x in (litres, fat, snf)):
        raise ValueError("Values must be finite numbers")

    if litres < 0:
        raise ValueError("Litres cannot be negative")

    if not MIN_FAT <= fat <= MAX_FAT:
        raise ValueError("Fat must be between 2.0 and 7.0")

    if not MIN_SNF <= snf <= MAX_SNF:
        raise ValueError("SNF is outside the allowed range")


def run_tests():
    """Test normal, boundary, invalid and five-entry cases."""
    tests = [
        ("Standard values", 10, 3.5, 8.5, 300.00),
        ("Fat and SNF above standard", 10, 4.0, 9.0, 335.00),
        ("Fat and SNF below standard", 10, 3.0, 8.0, 265.00),
        ("Minimum fat", 10, 2.0, 8.5, 240.00),
        ("Maximum fat", 10, 7.0, 8.5, 440.00),
    ]

    print("VALID TESTS")
    for name, litres, fat, snf, expected in tests:
        actual = payout(litres, fat, snf)
        assert actual == expected, f"{name}: expected {expected}, got {actual}"
        print(f"{name}: expected Rs. {expected:.2f}, actual Rs. {actual:.2f} PASS")

    print("\nINVALID TESTS")
    invalid_tests = [
        ("Text input", ("ten", 4.0, 8.5)),
        ("Negative litres", (-5, 4.0, 8.5)),
        ("Fat below range", (10, 1.5, 8.5)),
        ("Fat above range", (10, 7.5, 8.5)),
    ]

    for name, values in invalid_tests:
        try:
            payout(*values)
            assert False, f"{name}: expected ValueError"
        except ValueError:
            print(f"{name}: correctly rejected PASS")

    print("\nFIVE-ENTRY TOTAL")
    entries = [
        (10, 3.5, 8.5),
        (8, 4.0, 9.0),
        (12, 3.0, 8.0),
        (5, 2.0, 8.5),
        (6, 7.0, 8.5),
    ]

    expected_amounts = [300.00, 268.00, 318.00, 120.00, 264.00]
    amounts = [payout(*entry) for entry in entries]

    for i, (amount, expected) in enumerate(zip(amounts, expected_amounts), 1):
        assert amount == expected
        print(f"Entry {i}: Rs. {amount:.2f}")

    total = sum(amounts)
    assert total == 1270.00
    print(f"Total: Rs. {total:.2f} PASS")
    print("\nAll tests passed!")


if __name__ == "__main__":
    run_tests()
