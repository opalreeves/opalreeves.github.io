#have user enter an integer for player to guess
num_secret = int(input("Enter the integer for the player to guess:"))

#player enters guess
num_guess = int(input("Enter your guess:"))

#count the number of tries
num_tries = 1

#while loop for high and low guesses. make sure to add tries after guesses
while num_guess != num_secret:
    if num_guess > num_secret:
        num_guess = int(input("Too high - Try again."))
    else: 
        num_guess = int(input("Too low - Try again."))
    num_tries += 1

#if statement for when guessed correctly printing number of tries
if num_tries == 1:
    print("You guessed it in 1 try")
else:
    print(f"You guessed it in {num_tries} tries.")