
"""Rate card of the village milk co-operative."""

# Named constants
BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30


def rate_per_litre(fat, snf):
    """Calculate the rate per litre, rounded to 2 decimals."""
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)

    rate = (
        BASE_RATE
        + fat_steps * FAT_STEP_VALUE
        + snf_steps * SNF_STEP_VALUE
    )
    return round(rate, 2)


def payout(litres, fat, snf):
    """Calculate the farmer's payment, rounded to 2 decimals."""
    rate = rate_per_litre(fat, snf)
    return round(litres * rate, 2)


# Run this section only when the file is executed directly
if __name__ == "__main__":
    entries = [
        (10, 3.5, 8.5),
        (8.5, 4.2, 8.7),
        (12, 3.1, 8.3)
    ]

    for litres, fat, snf in entries:
        rate = rate_per_litre(fat, snf)
        amount = payout(litres, fat, snf)

        print(
            f"{litres:5} L  fat {fat}  snf {snf}"
            f"  rate {rate:6.2f}  pay {amount:8.2f}"
        )
