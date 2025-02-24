'''
1. Write a function called count_vowels(input) that takes a string
and returns the number of vowels (a, e, i, o, u) in it.
Test: User's Input
Input: Strings
Output: Integer
Function Body: Vowel variable, count variable, for loop, return
'''
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for vowel in input_string:
        if vowel in vowels:
            count += 1
    return count

input_string = "HELLO! My name is Dayshawn."
print(count_vowels(input_string))
'''
2. Write a function called is_palindrome(s) that checks whether a string is a
palindrome
(reads the same forward and backward, ignoring case). The function should
returns
either True or False.
Test: racecar (True), pikachu (False), Racecar (True)
Input: string (s)
Output: boolean
Function body: lowercase s, flip s and save to new variable (flipped_s), and then compare s & flipped_s
'''
def is_palindrome(s):
    lower_s = s.lower()
    flipped_s = lower_s[::-1]
    print(flipped_s)
    return lower_s == flipped_s
    
print(is_palindrome("pikachu"))    
print(is_palindrome("racecar"))
print(is_palindrome("Racecar"))
'''
3. In the game Pokemon, certain types of Pokemon do extra damage to other types.
For example, water is very effective to fight fire.
Write a function called type_advantage(attacker, defender) that takes two
Pokémon types as
strings and returns "Super Effective", "Not Very Effective", or "Neutral" based
on
simple type effectiveness rules. Your solution only needs to work for these
three sets of input:
print(type_advantage("Water", "Fire")) # "Super Effective"
print(type_advantage("Fire", "Water")) # "Not Very Effective"
print(type_advantage("Electric", "Grass")) # "Neutral"
Test: Attack effectiveness
Input: Two Pokemon types
Output: Effectiveness
Function Body: If, elif and else statements. Set Attacker and Defender to Pokemon types.
'''
def type_advantage(attacker,defender):
    if attacker  == "Water" and defender == "Fire":
        return "Super Effective"
    elif attacker == "Fire" and defender == "Water":
        return "Not Very Effective"
    else:
        return "Neutral"
print(type_advantage("Water", "Fire")) # "Super Effective"
print(type_advantage("Fire", "Water")) # "Not Very Effective"
print(type_advantage("Electric", "Grass")) # "Neutral"
'''
4. Write a function called ferry_fare(age, vehicle) that calculates the Washington
State Ferry fare
based on age and whether the person has a vehicle. Assume the following rates:
* Adults (19-64): $10 without a vehicle, $20 with a vehicle.
* Seniors (65+): $5 without a vehicle, $15 with a vehicle.
* Children (0-18): Free.

'''
def ferry_fare(age, vehicle):
    if vehicle == "Owns":
        if age >= 64:
            return "That will be $15."
        elif age >= 19:
            return "That will be $20."
        else:
            return "You don't have to pay anything."
    else:
        if age >= 64:
            return "That will be $5."
        elif age >= 19:
            return "That will be $10."
        else:
            return "You don't have to pay anything."
print(ferry_fare(65,"Owns"))
print(ferry_fare(19,"Owns"))
print(ferry_fare(5,"Owns"))
print(ferry_fare(65,"Doesn't Own"))
print(ferry_fare(19,"Doesn't Own"))
print(ferry_fare(5,"Doesn't Own"))
'''
5. Write a function called level_up(experience) that takes a player's experience
points
and returns their new level based on these rules:
* 0-99 XP → Level 1
* 100-199 XP → Level 2
* 200+ XP → Level 3
'''
def level_up(experience):
    if experience <= 99:
        return "You are currently level 1."
    elif experience <= 199:
        return "You are currently level 2."
    else:
        return "You are currently level 3!"
print(level_up(99))
print(level_up(199))
print(level_up(325))
