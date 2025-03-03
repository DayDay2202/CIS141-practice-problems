'''
#1. Create a file called gardening_tips.txt and add at least 3 gardening tips to
it.
Write a Python script that reads a file gardening_tips.txt and prints
out each tip one by one.
'''
file1 = open("gardening_tips.txt","r")
print(file1.read())
file1.close()
'''
#2. Write a Python program that allows users to log their hiking trips. The program
should:
- Use a while loop to repeatedly ask for a hike name and distance in miles
- Save each entry to hiking_log.txt (each hike on a new line)
- When the user presses 0, exit the loop & print the contents of hiking_log.txt
'''
with open('hiking_log.txt', 'a') as file:
    while True:
        name = input("What is the hikers name? Input 0 to exit the program: ")
        if name == "0":
            break
        distance = input("What was their distance traveled in miles? Input 0 to exit the program: ")
        if distance == "0":
            break
        file.write(name + "\t" + distance + "\n")
print("\n" + "Hiking Log:")
with open("hiking_log.txt", "r") as file:
    print(file.read())
'''
#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into
it. Write a Python program that:
- Reads the file
- Requests 5 inputs from the user: 5 words the user would like to count the
frequency of
- Counts how many times each word appears
- Creates a dictionary of the words and their counts
- Print the dictionary to the console
'''
with open("song_lyrics.txt", "r") as file:
    lyrics = file.read().lower()
words_to_count = []
print("Enter in five words you would like to check the frequency of in this song: ")
for i in range(5):
    word = input("Word: ").lower()
    words_to_count.append(word)
word_counts = {}
for word in words_to_count:
    word_counts[word] = lyrics.split().count(word)
print("The word frequencies are: ", word_counts)
'''
#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated
by commas.
Write a program that reads the poll.txt file
Count how many votes "yea" or "nay" received and print the results.
'''
file_path = poll.txt
count_votes(file_path)
def count_votes(file_path):
    with open(file_path,"r") as file:
        votes = file.read.strip().split("'")
    yea_count = votes.count("yea")
    nay_count = votes.count("nay")
print("The 'yea' votes are: ",yea_count,". The 'nay' votes are: ",nay_count,".")
