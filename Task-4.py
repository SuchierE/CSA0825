
import math

# Named constants
BASE_RATE = 30.0
FAT_RATE = 0.40
SNF_RATE = 0.30
STEP_SIZE = 0.1

# Farmer values
fat = 4.2
snf = 8.0
litres = 10.0

# Calculate fat and SNF steps
fat_steps = round((fat - 3.5) / STEP_SIZE)
snf_steps = round((snf - 7.0) / STEP_SIZE)

# Calculate rate and payment
rate = BASE_RATE + fat_steps * FAT_RATE + snf_steps * SNF_RATE
amount = litres * rate

print("Fat steps:", fat_steps)
print("SNF steps:", snf_steps)
print("Rate per litre: Rs.", round(rate, 2))
print("Payment amount: Rs.", round(amount, 2))

# Floating-point surprises
print("\nFloating-point surprises:")
print("(4.2 - 3.5) / 0.1 =", (4.2 - 3.5) / 0.1)
print("0.1 + 0.2 =", 0.1 + 0.2)
print("0.1 + 0.2 == 0.3:", 0.1 + 0.2 == 0.3)

# Operator precedence and associativity
print("\nOperator precedence:")
print("2 ** 3 ** 2 =", 2 ** 3 ** 2)
print("-2 ** 2 =", -2 ** 2)
print("(-2) ** 2 =", (-2) ** 2)

# round(), int(), and floor()
print("\nRounding differences:")
for x in [2.7, -2.7]:
    print("Value:", x,
          "round:", round(x),
          "int:", int(x),
          "floor:", math.floor(x))

# Compare step calculation methods
print("\nStep calculation comparison:")
for fat_value in [4.2, 3.1]:
    steps_round = round((fat_value - 3.5) / STEP_SIZE)
    steps_int = int((fat_value - 3.5) / STEP_SIZE)
    steps_floor = math.floor((fat_value - 3.5) / STEP_SIZE)

    print("\nFat:", fat_value)
    print("round steps:", steps_round,
          "rate:", BASE_RATE + steps_round * FAT_RATE)
    print("int steps:", steps_int,
          "rate:", BASE_RATE + steps_int * FAT_RATE)
    print("floor steps:", steps_floor,
          "rate:", BASE_RATE + steps_floor * FAT_RATE)

# Comparison chaining and Boolean operators
print("\nValidation:")
print("Fat valid:", 2.0 <= fat <= 7.0)
print("SNF valid:", 0.0 <= snf <= 15.0)
print("All valid:", 2.0 <= fat <= 7.0 and 0.0 <= snf <= 15.0)
print("At least one valid:", fat >= 2.0 or snf >= 7.0)

# Complexity
print("\nTime Complexity: O(1)")
print("Space Complexity: O(1)")
