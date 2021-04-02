import random

print("""
This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!\n""")

goal = random.randint(1, 99)
count = 0
inp = -1
while inp != goal:
    print("What's your guess between 1 and 99?")
    inp = input(">>")
    if (inp == 'exit'):
        print("Goodbye!")
        exit(0)
    inp = int(inp)
    if inp > goal:
        print("Too high!")
    if inp < goal:
        print("Too low!")
    count += 1
print("Congratulations, you've got it!")
print("You won in {} attempts!".format(count))