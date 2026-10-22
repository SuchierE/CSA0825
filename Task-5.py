BASE_RATE = 30.0
FAT_RATE = 0.40
SNF_RATE = 0.30


def read_float(prompt):
    while True:
        text = input(prompt).strip()

        try:
            return float(text)
        except ValueError:
            print("Invalid number! Enter a value such as 8.5.")


farmer_id = input("Enter Farmer ID: ").strip()
litres = read_float("Enter litres: ")
fat = read_float("Enter fat percentage: ")
snf = read_float("Enter SNF percentage: ")
shift = input("Enter shift (Morning/Evening): ").strip().lower()

if litres < 0:
    print("Litres cannot be negative.")
elif not 2.0 <= fat <= 7.0:
    print("Fat must be between 2.0 and 7.0.")
elif snf < 0:
    print("SNF cannot be negative.")
elif shift not in ("morning", "evening"):
    print("Invalid shift.")
else:
    # Calculate rate and payment
    rate = BASE_RATE + fat * FAT_RATE + snf * SNF_RATE
    amount = litres * rate

    print("\n--- Farmer Payment Details ---")
    print(f"{'Farmer ID':<18}: {farmer_id}")
    print(f"{'Shift':<18}: {shift.title()}")
    print(f"{'Litres':<18}: {litres:8.2f}")
    print(f"{'Fat %':<18}: {fat:8.2f}")
    print(f"{'SNF %':<18}: {snf:8.2f}")
    print(f"{'Rate per litre':<18}: Rs. {rate:8.2f}")
    print(f"{'Payment amount':<18}: Rs. {amount:8.2f}")
