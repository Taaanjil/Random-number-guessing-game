# Name: Md Monjur Morshed Tanjil
# Matriculation: 3156261



import random
import time
import winsound

def guess_random_number():
    # generate a random number between 1 and 100
    digit = random.randint(1, 100)

    # set the initial values for the number of attempts and highest score
    attempts = 0
    guess=0
    highest_score = float("inf")

    # begin the game
    while True:
        # request the user to guess the number
        guess = (input("Guess a number between 1 and 100 (or 'q' to quit): "))
        #check if user wants to quit
        if guess=='q':
            print('Game over. The answer was',digit)
            winsound.PlaySound("SystemExit", winsound.SND_ALIAS) #play sound
            return
        #convert the guess to integer
        guess=int(guess)
        # increase the count of attempts
        attempts += 1
        
        # verify whether the guess is correct
        if guess == digit:
            print(f"Congratulations! You have guessed the number in {attempts} attempts.")
            winsound.PlaySound("*", winsound.SND_PURGE) #play sound
            
            # update the high score if it is required
            if attempts < highest_score:
                print("New high score!")
                highest_score = attempts
            # request the user if they want to play again
            play_again = input("Play again? (y/n):").lower()
            if play_again == "y":
                # generate a new random number
                digit = random.randint(1, 100)
                # reset the number of guesses
                attempts = 0
                # start the timer
                start_time = time.time()
            else:
                return attempts
                
        elif guess < digit:
            print("Too low. Guess again.")
            frequency = 1500 
            duration = 500  
            winsound.Beep(frequency, duration) #play sound
        else:
            print("Too high. Guess again.")
            frequency = 2000 
            duration = 700 
            winsound.Beep(frequency, duration) #play sound
            
        # add a timer
        if attempts == 1:
            start_time = time.time()
        elif attempts >= 10:
            print(f"Time elapsed: {time.time() - start_time:.2f} seconds")

if __name__ == '__main__':
    guess_random_number()
