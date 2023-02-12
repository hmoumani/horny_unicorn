import random

print("""This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!\n""")

goal = random.randint(1, 99)
count = 1
inp = -1
while True:
    try:
        print("What's your guess between 1 and 99?")
        inp = input(">>")
        if (inp == 'exit'):
            print("Goodbye!")
            exit(0)
        if inp == '42':
            print("The answer to the ultimate question of life, the universe and everything is 42.")
            break
        inp = int(inp)
        if inp > goal:
            print("Too high!")
        elif inp < goal:
            print("Too low!")
        else:
            break
    except Exception:
        print("That's not a number.")
    count += 1
if count > 1:
    print("Congratulations, you've got it!")
    print("You won in {} attempts!".format(count))
else:
    print("Congratulations! You got it on your first try!")