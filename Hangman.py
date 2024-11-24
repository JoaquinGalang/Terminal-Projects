import random

# GENERATES A RANDOM PHRASE FROM A LIST
def generate_phrase():
    random_phrases = ["Cloudy Skies", "Sunny Side Up", "Midnight Snack",
                    "Merry Christmas", "Raise A Glass", "Happily Ever After"]
    chosen_phrase = random.choice(random_phrases)
    return chosen_phrase

# ENCRYPTS A GIVEN PHRASE
def encrypt_phrase(phrase, letters):
    encrypted = ""
    for letter in phrase:
        if letter.isspace():
            encrypted += " "
        elif letter.upper() in letters:
            encrypted += letter
        else:
            encrypted += "-"
    return encrypted

# RETURNS A LIST OF 3 RANDOM LETTERS FROM THE PHRASE
def generate_letters(phrase):
    phrase_letters = list(set(phrase))
    letters = []
    for n in range(2):
        letters.append(phrase_letters.pop(random.randint(0, len(phrase_letters)-1)).upper())
    return letters


# DISPLAY HANGMAN WITH BODY PARTS BASED ON "ATTEMPTS"
def display_hangman(attempts):
    bodypart_list = ["O", "|", "/", "\\", "/", "\\"]
    hangman_list = [" "]*6

    for num in range(attempts):
        hangman_list[num] = bodypart_list[num]

    print("_______     ")
    print("|     |     ")
    print("|     {}    ".format(hangman_list[0])) 
    print("|    {}{}{} ".format(hangman_list[2], hangman_list[1], hangman_list[3]))
    print("|    {} {}  ".format(hangman_list[4], hangman_list[5]))
    print("|           ")
 
# PROMPTS USER TO INPUT A VALID LETTER
def user_guess(letters):
    guess = input("Enter a letter: ")[0].upper()
    while guess not in letters:
        print("Enter a different letter!")
        guess = input("Enter a letter: ")[0].upper()
    return guess

# GAME LOOP
game_on = True
while game_on:
    print("\n"*3)
    print("-------------------------")
    print("        HANGMAN")
    print("-------------------------")
    # Generates a random phrase
    chosen_phrase = generate_phrase()
    # Generates 3 random letters
    letters = generate_letters(chosen_phrase)
    attempts = 0
    while True:
        # Display hangman
        display_hangman(attempts)

        # Encrypt phrase, characters from the letters variable will not be encrypted
        hidden_phrase = encrypt_phrase(chosen_phrase, letters)
        print(hidden_phrase)

        # Win or lose check
        if attempts == 6:
            print("YOU LOSE!")
            print(f"The phrase was: \"{chosen_phrase}\"")
            break
        elif chosen_phrase == hidden_phrase:
            print("YOU WIN!")
            break
        
        # Prompt user guess and validate guess
        guess = input("Enter Letter: ")[0].upper()
        while guess in letters:
            print("Try another letter.")
            guess = input("Enter Letter: ")[0].upper()
        letters.append(guess)
        print("\n"*2)

        # If the guess is not in the phrase, increment attempts by 1
        if guess not in chosen_phrase.upper():
            attempts += 1

    # Prompt user if they want to play again and validate their response
    again = input("Play Again? [Y/N]: ")[0].upper()
    while again not in ["Y", "N"]:
        print("Invalid Input! Try again.")
        again = input("Play Again? [Y/N]: ")[0].upper()
        if again == "N":
            game_on = False
            break
    
        
    

    