
# Task 1: Farmer Milk Payment Problem

# Named constants
MIN_FAT = 2.0
MAX_FAT = 7.0
MIN_SNF = 0.0
MAX_SNF = 15.0
FARMERS = 300

# Store farmer entries in a list
farmer_entries = []
ten_day_total = 0.0

# Input farmer details
n = int(input("Enter number of farmers: "))

for i in range(n):
    print(f"\nFarmer {i + 1}")

    farmer_id = input("Enter Farmer ID: ")
    litres = float(input("Enter litres of milk: "))
    fat = float(input("Enter fat percentage: "))
    snf = float(input("Enter SNF percentage: "))
    shift = input("Enter shift (Morning/Evening): ").strip().lower()

    # Validate inputs
    if litres < 0:
        print("Invalid litres. Must not be negative.")
        continue

    if not MIN_FAT <= fat <= MAX_FAT:
        print("Invalid fat percentage.")
        continue

    if not MIN_SNF <= snf <= MAX_SNF:
        print("Invalid SNF percentage.")
        continue

    if shift not in ("morning", "evening"):
        print("Invalid shift.")
        continue

    # Example payment rate formula
    rate = 5 * fat + 2 * snf
    amount = litres * rate

    # Store each entry as a tuple
    farmer_entries.append(
        (farmer_id, litres, fat, snf, shift, rate, amount)
    )

    ten_day_total += amount

    print(f"Rate per litre: Rs. {rate:.2f}")
    print(f"Payment amount: Rs. {amount:.2f}")

print("\n--- Payment Summary ---")
print("Valid entries:", len(farmer_entries))
print(f"Total payment: Rs. {ten_day_total:.2f}")
print("Ten-day total assumes these entries cover all ten days.")

# Complexity analysis
print("\nTime Complexity: O(n)")
print("Space Complexity: O(n)")
