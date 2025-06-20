import random

def hangman():
    # List of words to choose from
    words = ['python', 'hangman', 'programming', 'computer', 'keyboard', 'developer', 'algorithm']
    
    # Select a random word
    secret_word = random.choice(words).upper()
    guessed_letters = []
    attempts = 6  # Number of allowed wrong guesses
    
    print("Welcome to Hangman!")
    print("Guess the word one letter at a time. You have 6 wrong attempts allowed.")
    
    while True:
        # Display the current state of the word
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in secret_word])
        print(f"\nWord: {display_word}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Attempts left: {attempts}")
        
        # Check if player has won
        if all(letter in guessed_letters for letter in secret_word):
            print(f"\nCongratulations! You guessed the word: {secret_word}")
            break
            
        # Check if player has lost
        if attempts <= 0:
            print(f"\nGame over! The word was: {secret_word}")
            break
            
        # Get player's guess
        while True:
            guess = input("Guess a letter: ").upper()
            if len(guess) != 1:
                print("Please enter a single letter.")
            elif not guess.isalpha():
                print("Please enter a letter (A-Z).")
            elif guess in guessed_letters:
                print("You've already guessed that letter. Try another one.")
            else:
                break
                
        guessed_letters.append(guess)
        
        # Check if guess is correct
        if guess not in secret_word:
            attempts -= 1
            print(f"Wrong guess! The letter {guess} is not in the word.")
        else:
            print(f"Good guess! The letter {guess} is in the word.")

if _name_ == "_main_":
    hangman()