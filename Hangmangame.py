import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "strawberry", "blueberry", "melon"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()

def hangman():
    print("Welcome to Hangman!")
    word = choose_word()
    guessed_letters = []
    attempts = 6  
    
    while True:
        print("\nWord to guess:", display_word(word, guessed_letters))
        print("Attempts left:", attempts)
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print("Good guess!")
        else:
            print("Oops! That letter is not in the word.")
            attempts -= 1
        
        if "_" not in display_word(word, guessed_letters):
            print("\nCongratulations! You guessed the word:", word)
            break
        
        if attempts == 0:
            print("\nSorry, you ran out of attempts. The word was:", word)
            break

if __name__ == "__main__":
    hangman()
