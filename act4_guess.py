#AQUINO HEAVEN
#BAET2102
#GUESSING GAME

tries = 0
while True:
    guess = int(input("Guess:"))
    tries += 1

    if guess > 4:
        print("Too high")
    elif guess < 4:
        print("Too low")
    else:
        print(f"Correct! You got it in {tries} tries.")
        break

    