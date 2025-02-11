# 1. Create a program that prints the following output to the screen: "Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked."
print("Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked.")
# 2. Create a program that prompts for 2 numbers and then outputs the addition, subtraction, multiplication, and division of the first number by the second number.
x = int(input("x = "))
y = int(input("y = "))
print(x + y,x - y,x * y,x / y)
# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula. (https://en.wikipedia.org/wiki/Heron%27s_formula)
a = int(input("Side a = "))
b = int(input("Side b = "))
c = int(input("Side c = "))
area = print((a + b + c) * 0.5)
# 4. Create a program that computes different statistics given five numbers including the total, average, minimum, maximum, range, and standard deviation (https://en.wikipedia.org/wiki/Standard_deviation).
import math
Value_A = int(input("First number is "))
Value_B = int(input("Second number is "))
Value_C = int(input("Third number is "))
Value_D = int(input("Forth number is "))
Value_E = int(input("Final number is "))
numbers = Value_A,Value_B,Value_C,Value_D,Value_E
total = print(Value_A + Value_B + Value_C + Value_D + Value_E)
average = print((Value_A + Value_B + Value_C + Value_D + Value_E) / 5)
minimum = print(min(Value_A,Value_B,Value_C,Value_D,Value_E))
maximum = print(max(Value_A,Value_B,Value_C,Value_D,Value_E))
import statistics
print(statistics.pstdev(numbers))
