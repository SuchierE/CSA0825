
# TASK 6: Organise the Logic into Functions

# Named constants
BASE_RATE = 30.0
FAT_RATE = 0.40
SNF_RATE = 0.30


def rate_per_litre(fat, snf):
    """Calculate and return the milk rate per litre."""
    return BASE_RATE + (fat * FAT_RATE) + (snf * SNF_RATE)


def payout(litres, fat, snf):
    """Calculate and return the payment for a milk entry."""
    rate = rate_per_litre(fat, snf)
    return litres * rate


def ten_day_total(payments):
    """Return the sum of payments collected over ten days."""
    return sum(payments)


def main():
    """Read farmer details, calculate payment, and display results."""
    payments = []

    n = int(input("Enter number of entries: "))

    for i in range(n):
        print(f"\nFarmer {i + 1}")

        farmer_id = input("Enter Farmer ID: ")
        litres = float(input("Enter litres: "))
        fat = float(input("Enter fat percentage: "))
        snf = float(input("Enter SNF percentage: "))

        if litres < 0 or not 2.0 <= fat <= 7.0 or snf < 0:
            print("Invalid input. Entry skipped.")
            continue

        rate = rate_per_litre(fat, snf)
        amount = payout(litres, fat, snf)
        payments.append(amount)

        print(f"Farmer ID: {farmer_id}")
        print(f"Rate per litre: Rs. {rate:.2f}")
        print(f"Payment amount: Rs. {amount:.2f}")

    total = ten_day_total(payments)
    print(f"\nTotal payment: Rs. {total:.2f}")


if __name__ == "__main__":
    main()
