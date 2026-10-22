
from decimal import Decimal
from time import perf_counter

# Generate payment amounts as decimal strings
PAYMENT = "33.40"
SIZES = [300, 6000, 150000]


def total_float(payments):
    """Calculate the total using floating-point arithmetic."""
    total = 0.0
    for payment in payments:
        total += float(payment)
    return total


def total_decimal(payments):
    """Calculate the exact decimal total from strings."""
    total = Decimal("0.00")
    for payment in payments:
        total += Decimal(payment)
    return total


def measure_time(function, payments):
    """Return the result and execution time in seconds."""
    start = perf_counter()
    result = function(payments)
    elapsed = perf_counter() - start
    return result, elapsed


print("FLOAT vs DECIMAL TOTALS")
print("-" * 75)

for n in SIZES:
    payments = [PAYMENT] * n

    float_total, float_time = measure_time(total_float, payments)
    decimal_total, decimal_time = measure_time(total_decimal, payments)

    difference = abs(Decimal(str(float_total)) - decimal_total)

    print(f"\nPayments: {n}")
    print(f"Float total   : {float_total:.10f}")
    print(f"Decimal total : {decimal_total:.2f}")
    print(f"Difference    : {difference}")
    print(f"Float time    : {float_time:.6f} seconds")
    print(f"Decimal time  : {decimal_time:.6f} seconds")


# Compare rounding each payment vs rounding the final total
print("\nROUNDING COMPARISON")

amounts = [0.105] * 10

round_each = sum(round(x, 2) for x in amounts)
round_total = round(sum(amounts), 2)

decimal_each = sum(
    (Decimal(str(x)).quantize(Decimal("0.01")) for x in amounts),
    Decimal("0.00")
)
decimal_total = sum(
    (Decimal(str(x)) for x in amounts),
    Decimal("0.00")
).quantize(Decimal("0.01"))

print("Round each float payment:", round_each)
print("Round float total      :", round_total)
print("Round each Decimal     :", decimal_each)
print("Round Decimal total    :", decimal_total)


# Compare recalculation with dictionary lookup
BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30


def calculate_rate(fat, snf):
    """Calculate a rate from fat and SNF values."""
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)
    return round(
        BASE_RATE
        + fat_steps * FAT_STEP_VALUE
        + snf_steps * SNF_STEP_VALUE, 2
    )


entries = [(4.2, 8.7)] * 150000

start = perf_counter()
recalculated = [calculate_rate(fat, snf) for fat, snf in entries]
recalculate_time = perf_counter() - start

start = perf_counter()
rate_table = {
    (fat, snf): calculate_rate(fat, snf)
    for fat, snf in set(entries)
}
lookup_rates = [rate_table[(fat, snf)] for fat, snf in entries]
lookup_time = perf_counter() - start

assert recalculated == lookup_rates

print("\nRATE CALCULATION COMPARISON")
print(f"Recalculation time: {recalculate_time:.6f} seconds")
print(f"Dictionary time   : {lookup_time:.6f} seconds")
print("Distinct rate pairs:", len(rate_table))
