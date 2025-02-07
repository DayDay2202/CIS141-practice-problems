#1. Prompt the user for a positive integer n. Use a while loop to sum all the integers from 1 up to n. Print the final sum.

n = int(input("Enter a positive integer:"))
i = 1
sum = 0
while i <= n:
    sum = sum + i
    i += 1
print("The final sum is", sum)

#2. Define a string variable (e.g., my_string = "Olympic College"). Use a for loop to print each character on its own line. Convert each character to uppercase before printing.

my_string = "Olympic College"
my1 = my_string.upper()
for i in range(0,len(my_string)):
    print(my1[i])

#3. Use a for loop and the range() function to print all even numbers from 2 to 20.

for i in range(2,21):
    if i % 2 == 0:
        print(i)

#4. Use nested for loops to create a simple multiplication table for numbers 1 through 5. Format your output so that each row corresponds to multiplying by a specific number.

for i in range(1,6):              # Column: 1,2,3,4,5
    print(f"{i}", end="")         # Prints first i value then first j value, etc.
    for j in range(2,6):          # Row: 1,2,3,4,5
        print(f"{i * j:4}",end="")# Prints i value multiplied by j value and put 4 spaces in between each result/
    print("")                     # Prints a new line after each j loop.

#5. Write a program that continuously asks the user to input a number. If the user enters 0, immediately stop asking for more numbers. Otherwise, print the number they entered.

while True:
    num = int(input("Enter a number (0 will stop the program):"))# Have to set inputed number to variable.
    if num == 0:                                                 # If 0 then the program will end.
        print("Stopping the program.")                           # Will print "Stopping the program".
        break
    else:
        print(f"The number you entered is {num}.")               # If any other number is inputted it will show up and ask for a number again.
