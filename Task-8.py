
# TASK 8: Ten-Day Farmer Payment Algorithm

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30


def rate_per_litre(fat, snf):
    """Calculate the milk rate per litre."""
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    return round(
        BASE_RATE
        + fat_steps * FAT_STEP_VALUE
        + snf_steps * SNF_STEP_VALUE, 2
    )


def payout(litres, fat, snf):
    """Calculate payment for one valid entry."""
    return round(litres * rate_per_litre(fat, snf), 2)


def valid_entry(litres, fat, snf, shift):
    """Check the entry against the validation rules."""
    return (
        litres >= 0
        and 2.0 <= fat <= 7.0
        and 0.0 <= snf <= 15.0
        and shift.lower() in ("morning", "evening")
    )


def main():
    """Calculate payments and the total for ten days."""
    total = 0.0
    entries = [
        ("F101", 10, 3.5, 8.5, "Morning"),
        ("F102", 8.5, 4.2, 8.7, "Evening"),
        ("F103", 12, 3.1, 8.3, "Morning")
    ]

    for farmer_id, litres, fat, snf, shift in entries:
        if not valid_entry(litres, fat, snf, shift):
            print(f"{farmer_id}: Invalid entry")
            continue

        rate = rate_per_litre(fat, snf)
        amount = payout(litres, fat, snf)
        total = round(total + amount, 2)

        print(
            f"{farmer_id} | Rate: Rs. {rate:.2f}"
            f" | Payment: Rs. {amount:.2f}"
        )

    print(f"\nTen-day total: Rs. {total:.2f}")


if __name__ == "__main__":
    main()
