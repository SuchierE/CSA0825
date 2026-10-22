
from decimal import Decimal
import sys

# TASK 2: Explore Values and Types in Python

print("1. DATA TYPES")
print(type(10))
print(type(10.0))
print(type("10"))
print(type(True))
print(type([10, 8.5]))

print("\n2. ARITHMETIC OPERATORS")
print("7 / 2 =", 7 / 2)
print("7 // 2 =", 7 // 2)
print("7 % 2 =", 7 % 2)
print("-7 // 2 =", -7 // 2)

print("\n3. FLOATING-POINT ISSUE")
print("0.1 + 0.2 == 0.3:", 0.1 + 0.2 == 0.3)
print("Decimal comparison:",
      Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))

# 1,000 payments of Rs 33.40 and three adjustments of Rs 0.10
payments = ["33.40"] * 1000 + ["0.10"] * 3


# Method 1: Using float
def total_float(items):
    total = 0.0
    for amount in items:
        total += float(amount)
    return total


# Method 2: Using Decimal
def total_decimal(items):
    total = Decimal("0.00")
    for amount in items:
        total += Decimal(amount)
    return total


# Method 3: Using Decimal(float(amount))
def total_decimal_float(items):
    total = Decimal("0.00")
    for amount in items:
        total += Decimal(float(amount))
    return total


# Method 4: Using integer paise
def total_paise(items):
    total = 0
    for amount in items:
        rupees, paise = amount.split(".")
        total += int(rupees) * 100 + int(paise.ljust(2, "0"))
    return total


# Method 5: Using round()
def total_round(items):
    total = 0.0
    for amount in items:
        total = round(total + float(amount), 2)
    return total


# Display totals
print("\n4. PAYMENT TOTALS")
print("float  :", total_float(payments))
print("Decimal:", total_decimal(payments))
print("Decimal(float):", total_decimal_float(payments))
print("Integer paise:", total_paise(payments))
print("Paise in rupees: Rs.", f"{total_paise(payments) // 100}."
      f"{total_paise(payments) % 100:02d}")
print("Rounded total:", total_round(payments))

# Memory usage
print("\n5. MEMORY USAGE")
print("Integer:", sys.getsizeof(10), "bytes")
print("Float:", sys.getsizeof(10.0), "bytes")
print("Decimal:", sys.getsizeof(Decimal("10.00")), "bytes")

# Complexity analysis
print("\n6. COMPLEXITY ANALYSIS")
print("Float: O(n) time")
print("Decimal: O(n) time")
print("Integer paise: O(n) time")
print("Round: O(n) time")
print("Auxiliary space for running total: O(1)")
print("Input list space: O(n)")
