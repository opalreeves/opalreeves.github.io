num_secret = int(input("Enter the integer for the player to guess:"))
num_guess = int(input("Enter your guess:"))
num_tries = 1

while num_guess != num_secret:
    if num_guess > num_secret:
        num_guess = int(input("Too high - Try again."))
    else: 
        num_guess = int(input("Too low - Try again."))
    num_tries += 1
if num_tries == 1:
    print("You guessed it in 1 try")
else:
    print(f"You guessed it in {num_tries} tries.")