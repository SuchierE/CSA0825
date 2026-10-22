
# TASK 3: Variables and Named Constants

# Named constants
BASE_RATE = 30.0
FAT_RATE = 0.40
SNF_RATE = 0.30

MIN_FAT = 2.0
MAX_FAT = 7.0
MIN_LITRES = 0.0

# Farmer details
farmer_id = "F101"
litres = 10.0
fat = 4.0
snf = 8.0
shift = "Morning"

# Calculate milk rate and payment
rate = BASE_RATE + (fat * FAT_RATE) + (snf * SNF_RATE)
amount = litres * rate

print("Farmer ID:", farmer_id)
print("Litres:", litres)
print("Fat:", fat, "%")
print("SNF:", snf, "%")
print("Shift:", shift)
print("Rate per litre: Rs.", round(rate, 2))
print("Payment amount: Rs.", round(amount, 2))

# Dynamic typing
value = 10
print("\nValue:", value, "Type:", type(value))

value = "Hello"
print("Value:", value, "Type:", type(value))

# Multiple assignment
a, b = 10, 20
print("\nBefore swapping:", a, b)

a, b = b, a
print("After swapping:", a, b)

# Alternative: dictionary rate card
RATE_CARD = {
    "base": 30.0,
    "fat": 0.40,
    "snf": 0.30
}

dictionary_rate = (
    RATE_CARD["base"]
    + fat * RATE_CARD["fat"]
    + snf * RATE_CARD["snf"]
)

print("\nDictionary rate: Rs.", round(dictionary_rate, 2))

# Complexity analysis
print("\nTime Complexity: O(1)")
print("Space Complexity: O(1)")
