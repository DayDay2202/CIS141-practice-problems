#1. Given a list of numbers, write code to iterate through the list and calculate the sum of all even numbers. Print the resulting sum.
numbers = [14,2,27,54,8,10,15,33] # First make a list
Sum = 0                           # Create a sum value starting at zero
for number in numbers:            # Make a loop that identifies even numbers and adds said numbers to sum
    if number % 2 == 0:
        Sum += number
print("The sum of the even numbers is", Sum)
#2. With a list of strings provided, write code that counts how many times the word "Olympic" appears in the list, and then print the count.
words = ["Olympic","Teachers","Students","Olympic","Olympic","Tennis","Olympic"] #Make a list
count = 0                                                                        #Make a counter at 0
for word in words:                                                               #Make a loop that adds 1 to count if word = "Olympic"
    if word == "Olympic":
        count += 1
print("The word 'Olympic' appears ", count, "times.")
#3. Given a list of strings, write code to 'create a new list that includes only the strings longer than three characters. Print the resulting filtered list.
strings = ["Movie","Book","He","She","Monopoly","The"] #Make a list
unique_strings = []                                    #Make the new list
for string in strings:                                 #Create a loop that will add words with letters > 3
    if len(string) > 3:
        unique_strings.append(string)
print(unique_strings)
#4. For a list of integers, write code that counts how many numbers are positive and how many are negative, then print both counts.
integers = [13,-5,82,-36,-19,52,23]                                                 #Make a list
pos_count = 0                                                                       #Make a positive and negative counter
neg_count = 0
for integer in integers:                                                            #Make a loop that will list number of pos and neg numbers
    if integer > 0:
        pos_count += 1
    else:
        neg_count += 1
print("The positve counter is",pos_count,". The negative counter is",neg_count,".")

#5. For a list of integers, use a loop to build a new list where each element is the square of the corresponding element in the original list. Print the new list.
new_integers = [7,3,5,9,2,8]                #Make a list
final_integers = []                         #Make a new list
for new_integer in new_integers:            #Make a loop that will take the square root of the number in the last list
    final_integers.append(new_integer ** 2)
print(final_integers)
