
"""Milk Cooperative Payment Calculator"""

from decimal import Decimal, ROUND_HALF_UP
import json

# Rate card stored inside the Python file
RATE_CARD_JSON = """
{
    "base_rate": "30.00",
    "seasonal_base_rate": "32.00",
    "fat_step_value": "0.40",
    "seasonal_fat_step_value": "0.45",
    "snf_step_value": "0.30",
    "standard_fat": "3.50",
    "standard_snf": "8.50",
    "min_fat": "2.00",
    "max_fat": "7.00",
    "min_snf": "0.00",
    "max_snf": "15.00",
    "bonus_rate": "0.50",
    "bonus_limit": "500"
}
"""

CENT = Decimal("0.01")
STEP_SIZE = Decimal("0.10")


def money(value):
    """Round money to two decimal places."""
    return Decimal(value).quantize(
        CENT, rounding=ROUND_HALF_UP
    )


def load_rate_card():
    """Load the embedded JSON rate card."""
    data = json.loads(RATE_CARD_JSON)
    return {key: Decimal(value) for key, value in data.items()}


def get_rate_card(month, rates):
    """Select the rate card for the month."""
    if 4 <= month <= 6:
        return {
            "base": rates["seasonal_base_rate"],
            "fat_step": rates["seasonal_fat_step_value"]
        }

    return {
        "base": rates["base_rate"],
        "fat_step": rates["fat_step_value"]
    }


def validate_entry(litres, fat, snf, shift, rates):
    """Validate farmer entry values."""
    if not all(x.is_finite() for x in (litres, fat, snf)):
        raise ValueError("Values must be finite numbers")

    if litres < 0:
        raise ValueError("Litres cannot be negative")

    if not rates["min_fat"] <= fat <= rates["max_fat"]:
        raise ValueError("Fat must be between 2.0 and 7.0")

    if not rates["min_snf"] <= snf <= rates["max_snf"]:
        raise ValueError("SNF is outside the allowed range")

    if shift.lower() not in ("morning", "evening"):
        raise ValueError("Invalid shift")


def rate_per_litre(fat, snf, month, rates):
    """Calculate the rate per litre for the selected month."""
    card = get_rate_card(month, rates)

    fat_steps = (
        (fat - rates["standard_fat"]) / STEP_SIZE
    ).quantize(Decimal("1"), rounding=ROUND_HALF_UP)

    snf_steps = (
        (snf - rates["standard_snf"]) / STEP_SIZE
    ).quantize(Decimal("1"), rounding=ROUND_HALF_UP)

    rate = (
        card["base"]
        + fat_steps * card["fat_step"]
        + snf_steps * rates["snf_step_value"]
    )

    return money(rate)


def payout(litres, fat, snf, shift, month, rates):
    """Calculate the payment for one entry."""
    validate_entry(litres, fat, snf, shift, rates)
    rate = rate_per_litre(fat, snf, month, rates)
    return money(litres * rate)


def ten_day_total(entries, month, rates):
    """Calculate ten-day payment and volume bonus.

    Each entry contains (litres, fat, snf, shift).
    The bonus applies to all ten-day litres when the total
    exceeds 500 litres.
    """
    total_litres = Decimal("0")
    milk_payment = Decimal("0.00")

    for litres, fat, snf, shift in entries:
        amount = payout(litres, fat, snf, shift, month, rates)
        milk_payment += amount
        total_litres += litres

    bonus = Decimal("0.00")

    if total_litres > rates["bonus_limit"]:
        bonus = money(total_litres * rates["bonus_rate"])

    return {
        "litres": total_litres,
        "milk_payment": money(milk_payment),
        "bonus": bonus,
        "total": money(milk_payment + bonus)
    }


def run_tests(rates):
    """Test seasonal rates, bonus, and invalid entries."""
    fat = Decimal("4.23")
    snf = Decimal("8.67")

    assert rate_per_litre(fat, snf, 5, rates) == Decimal("35.75")
    assert rate_per_litre(fat, snf, 2, rates) == Decimal("33.40")

    entries_500 = [
        (Decimal("500"), fat, snf, "Morning")
    ]
    entries_501 = [
        (Decimal("501"), fat, snf, "Morning")
    ]

    assert ten_day_total(entries_500, 5, rates)["bonus"] == Decimal("0.00")
    assert ten_day_total(entries_501, 5, rates)["bonus"] == Decimal("250.50")

    try:
        payout(
            Decimal("-1"), fat, snf, "Morning", 5, rates
        )
    except ValueError:
        pass
    else:
        raise AssertionError("Negative litres were not rejected")

    print("All automated tests passed.")


def main():
    """Read entries and print the ten-day payment summary."""
    rates = load_rate_card()
    run_tests(rates)

    try:
        month = int(input("Enter month number (1-12): "))
        if not 1 <= month <= 12:
            raise ValueError
        count = int(input("Enter number of entries: "))
        if count < 0:
            raise ValueError
    except ValueError:
        print("Invalid month or entry count.")
        return

    entries = []

    for i in range(count):
        print(f"\nEntry {i + 1}")
        farmer_id = input("Farmer ID: ").strip()

        try:
            litres = Decimal(input("Litres: ").strip())
            fat = Decimal(input("Fat percentage: ").strip())
            snf = Decimal(input("SNF percentage: ").strip())
        except Exception:
            print("Invalid numeric input. Entry skipped.")
            continue

        shift = input("Shift (Morning/Evening): ").strip()

        try:
            amount = payout(litres, fat, snf, shift, month, rates)
            rate = rate_per_litre(fat, snf, month, rates)
        except ValueError as error:
            print("Invalid entry:", error)
            continue

        entries.append((litres, fat, snf, shift))

        print("Farmer ID:", farmer_id)
        print(f"Rate per litre: Rs. {rate:.2f}")
        print(f"Payment amount: Rs. {amount:.2f}")

    summary = ten_day_total(entries, month, rates)

    print("\n--- Ten-Day Summary ---")
    print(f"Total litres: {summary['litres']}")
    print(f"Milk payment: Rs. {summary['milk_payment']:.2f}")
    print(f"Bonus: Rs. {summary['bonus']:.2f}")
    print(f"Total payable: Rs. {summary['total']:.2f}")


if __name__ == "__main__":
    main()
