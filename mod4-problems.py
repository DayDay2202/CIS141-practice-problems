#1. Construct a truth table for the expression: (A AND B) OR (NOT B) where A and B each can be True or False. Your truth table should be commented out (as it's not valid Python code!)
# A B   (A AND B)   (NOT B)     (A AND B) OR (NOT B)
# T T   T           F           T                       
# T F   F           T           T                       
# F T   F           F           F                       
# F F   F           T           T                       
#2. The headlights of a car should only automatically turn on when the daylight outside is below a certain threshold. If a sensor threshold is below the number 8, print "Headlights On"; otherwise, print "Headlights Off".
Daylight_Threshold = int(input("The sensor threshold is currently: "))
if Daylight_Threshold < 8:
    print("Headlights On")
else:
    print("Headlights Off")
#3. Prompt the user for their bank balance. Evaluate whether the balance is less than $100. Print True if the user’s balance is below $100; print False, otherwise.
Balance = int(input("What is your bank balance?: "))
print(Balance < 100)
#4. A theater wants to enforce age restrictions for movie tickets. Ask the user for their age, and tell them whether they can see G (appropriate for under 13), PG-13 (appropriate for 13 to 17), or R (appropriate for over 18) rated movies.
Age = int(input("What is your age?: "))
if Age < 13:
    print("You can watch movies rated G.")
elif Age < 18:
    print("You can watch both rated G and PG-13 movies.")
else:
    print("You can watch any movie from rated G, PG-13, and R.")
#5. A store charges $5 for shipping on any order under $50. If the order amount is $50 or more, shipping is free. Ask the user for the order total and print the total cost, including shipping.
Total_Cost = int(input("What is the total cost of your order?: "))
if Total_Cost < 50:
    Price = Total_Cost + 5
    print("Okay, you have to pay $5 for shipping so your total cost is $", Price, ".")
else:
    print("Okay, you have free shipping so your total cost is $", Total_Cost, ".")
