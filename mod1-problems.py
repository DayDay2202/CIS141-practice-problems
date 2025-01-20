# 1. Create a program that prints the following output to the screen: "Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked."
print("Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked.")
# 2. Create a program that prompts for 2 numbers and then outputs the addition, subtraction, multiplication, and division of the first number by the second number.
x = 10
y = 5
print(x + y,x - y,x * y,x / y)
# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula. (https://en.wikipedia.org/wiki/Heron%27s_formula)
import math

def herons_formula(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
a = int(input("Side a is..."))
b = int(input("Side b is..."))
c = int(input("Side c is..."))
area = herons_formula(a, b, c)
print(f"The area of the triangle with sides {a}, {b}, and {c} is {area:.2f}")
# 4. Create a program that computes different statistics given five numbers including the total, average, minimum, maximum, range, and standard deviation (https://en.wikipedia.org/wiki/Standard_deviation).
import math
def compute_statistics(numbers):
    if len(numbers) != 5:
        raise ValueError("Exactly five numbers are required.")
    total = sum(numbers)
    average = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    range_val = maximum - minimum
    variance = sum((x - average) ** 2 for x in numbers) / len(numbers)
    std_deviation = math.sqrt(variance)
    return {
        "Total": total,
        "Average": average,
        "Minimum": minimum,
        "Maximum": maximum,
        "Range": range_val,
        "Standard Deviation": std_deviation
    }
numbers = [10, 20, 30, 40, 50]
stats = compute_statistics(numbers)
for key, value in stats.items():
    print(f"{key}: {value}")
