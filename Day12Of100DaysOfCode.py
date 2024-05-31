logo = """

   

,---.   .--.  ___    _ ,---.    ,---. _______       .-''-.  .-------.   _ _    .-'''-.           .-_'''-.      ____    ,---.    ,---.    .-''-.   
|    \  |  |.'   |  | ||    \  /    |\  ____  \   .'_ _   \ |  _ _   \ ( ' )  / _     \         '_( )_   \   .'  __ `. |    \  /    |  .'_ _   \  
|  ,  \ |  ||   .'  | ||  ,  \/  ,  || |    \ |  / ( ` )   '| ( ' )  |(_{;}_)(`' )/`--'        |(_ o _)|  ' /   '  \  \|  ,  \/  ,  | / ( ` )   ' 
|  |\_ \|  |.'  '_  | ||  |\_   /|  || |____/ / . (_ o _)  ||(_ o _) / (_,_)(_ o _).           . (_,_)/___| |___|  /  ||  |\_   /|  |. (_ o _)  | 
|  _( )_\  |'   ( \.-.||  _( )_/ |  ||   _ _ '. |  (_,_)___|| (_,_).' __     (_,_). '.         |  |  .-----.   _.-`   ||  _( )_/ |  ||  (_,_)___| 
| (_ o _)  |' (`. _` /|| (_ o _) |  ||  ( ' )  \'  \   .---.|  |\ \  |  |   .---.  \  :        '  \  '-   .'.'   _    || (_ o _) |  |'  \   .---. 
|  (_,_)\  || (_ (_) _)|  (_,_)  |  || (_{;}_) | \  `-'    /|  | \ `'   /   \    `-'  |         \  `-'`   | |  _( )_  ||  (_,_)  |  | \  `-'    / 
|  |    |  | \ /  . \ /|  |      |  ||  (_,_)  /  \       / |  |  \    /     \       /           \        / \ (_ o _) /|  |      |  |  \       /  
'--'    '--'  ``-'`-'' '--'      '--'/_______.'    `'-..-'  ''-'   `'-'       `-...-'             `'-...-'   '.(_,_).' '--'      '--'   `'-..-'   
"""


import random

def guessing_game():
    print(logo)
    # Generates a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    user_name = input("What is your name?: ")
    # Asks the player to choose the difficulty level
    mode = input("Choose your mode (easy/difficult): ").lower()
    
    # Sets the number of chances based on the chosen difficulty level
    chances = 10 if mode == 'easy' else 5
    
    print(f"{user_name}, you have chosen the {mode} mode. You have {chances} chances to guess the number.")
    
    # Game loop
    while chances > 0:
        try:
            # Player makes a guess
            guess = int(input("Guess the number (1-100): "))
            
            # Checks if the guess is correct
            if guess == number_to_guess:
                print(f"Congratulations, {user_name}!! You've guessed the number correctly.")
                break
            # Gives hints if the guess is wrong
            elif guess < number_to_guess:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
            
            # Reduce the number of chances
            chances -= 1
            print(f"You have {chances} chances left.")
            
        except ValueError:
            print("Please enter a valid number.")
    
    if chances == 0:
        print(f"Game over! The number was {number_to_guess}.")

# Start the game
guessing_game()
                                                                                                                                        



