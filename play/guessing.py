from random import randint

## Configurable range
guessRange = (1, 100, 500)

# Print some instructions
print(f"Simple guessing game.   Guess a number from {guessRange[0]} to {guessRange[1]} inclusive.")
print(f"Enter {guessRange[2]} to escape")

# Choose the target
target = randint(guessRange[0], guessRange[1])
#print (f"Debug {target}")

# Initialize our guess list (let's us count the guesses)
guesses = [0]

while True:
    num = input("Enter a guess: ")
    if num.isnumeric():
        num = int(num)
        guesses.append(num)
    else:
        print("Numbers only please")
        continue
    # Input validatated and added to list, check stuff
    if num == guessRange[2]:
        print("The easy way out")
        break
    elif num == target:
        print(f"You got it!  It took {len(guesses)-1} guesses!")
        break
    # The easy part is done, now we need to look at our warmer/colder cycle
    elif len(guesses) > 2:
        if (abs(target-num) <= abs(target-guesses[-2])):
            print("Warmer")
        else:
            print("colder")
    else:  # We haven't been within 10
        if abs(target-num) <= 10:
            print ("Warm")
        else:
            print ("Ice Cold")
