
from decimal import Decimal, ROUND_HALF_UP

# Standard values
STANDARD_FAT = Decimal("3.50")
STANDARD_SNF = Decimal("8.50")
STEP_SIZE = Decimal("0.10")
SNF_STEP_VALUE = Decimal("0.30")
BONUS_RATE = Decimal("0.50")
BONUS_LIMIT = Decimal("500")
CENT = Decimal("0.01")


def money(value):
    """Round a monetary value to two decimal places."""
    return Decimal(value).quantize(
        CENT, rounding=ROUND_HALF_UP
    )


def get_rate_card(month):
    """Return the rate card for the given month."""
    if 4 <= month <= 6:
        return {
            "base": Decimal("32.00"),
            "fat_step": Decimal("0.45")
        }

    return {
        "base": Decimal("30.00"),
        "fat_step": Decimal("0.40")
    }


def calculate_steps(value, standard):
    """Calculate the nearest whole 0.1 percentage step."""
    return ((value - standard) / STEP_SIZE).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP
    )


def rate_per_litre(fat, snf, month):
    """Calculate the seasonal rate per litre."""
    card = get_rate_card(month)

    fat_steps = calculate_steps(fat, STANDARD_FAT)
    snf_steps = calculate_steps(snf, STANDARD_SNF)

    rate = (
        card["base"]
        + fat_steps * card["fat_step"]
        + snf_steps * SNF_STEP_VALUE
    )

    return money(rate)


def calculate_ten_day_payment(entries, month):
    """Calculate ten-day milk payment and volume bonus.

    Each entry is a tuple containing (litres, fat, snf).
    The bonus applies to all ten-day litres when total litres
    exceed 500.
    """
    total_litres = Decimal("0")
    milk_payment = Decimal("0")

    for litres, fat, snf in entries:
        if litres < 0:
            raise ValueError("Litres cannot be negative")
        if not Decimal("2.0") <= fat <= Decimal("7.0"):
            raise ValueError("Fat must be between 2.0 and 7.0")
        if not Decimal("0.0") <= snf <= Decimal("15.0"):
            raise ValueError("SNF is outside the allowed range")

        rate = rate_per_litre(fat, snf, month)
        total_litres += litres
        milk_payment += money(litres * rate)

    bonus = Decimal("0.00")

    if total_litres > BONUS_LIMIT:
        bonus = money(total_litres * BONUS_RATE)

    return {
        "litres": total_litres,
        "milk_payment": money(milk_payment),
        "bonus": bonus,
        "total": money(milk_payment + bonus)
    }


def run_tests():
    """Test seasonal rates and ten-day bonus eligibility."""
    fat = Decimal("4.23")
    snf = Decimal("8.67")

    # Seasonal and non-seasonal rate tests
    assert rate_per_litre(fat, snf, 5) == Decimal("35.75")
    assert rate_per_litre(fat, snf, 2) == Decimal("33.40")

    # Exactly 500 litres: no bonus
    result_500 = calculate_ten_day_payment(
        [(Decimal("500"), fat, snf)], 5
    )
    assert result_500["bonus"] == Decimal("0.00")

    # 501 litres: bonus applies to all litres
    result_501 = calculate_ten_day_payment(
        [(Decimal("501"), fat, snf)], 5
    )
    assert result_501["bonus"] == Decimal("250.50")

    # 600 litres: bonus applies to all litres
    result_600 = calculate_ten_day_payment(
        [(Decimal("600"), fat, snf)], 5
    )
    assert result_600["bonus"] == Decimal("300.00")

    print("All tests passed.")
    print("May rate per litre:", rate_per_litre(fat, snf, 5))
    print("February rate per litre:", rate_per_litre(fat, snf, 2))
    print("500 L bonus:", result_500["bonus"])
    print("501 L bonus:", result_501["bonus"])
    print("600 L bonus:", result_600["bonus"])
    print("600 L total payment:", result_600["total"])


if __name__ == "__main__":
    run_tests()
