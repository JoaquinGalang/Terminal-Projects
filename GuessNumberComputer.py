import random

def guess(x):
    random_number = random.randint(1, x)
    tries = 0
    answer = 0
    while answer != random_number:
        answer = int(input("   >> "))
        if answer < random_number:
            print("   Higher! Try again.\n")
            tries += 1
        elif answer > random_number:
            print("   Lower! Try again.\n")
            tries += 1
    print(f"   You win! The number was {random_number}.")
    print(f"   Number of Tries: {tries}.\n")

def play_again():
    again = ""
    while again not in ["Y", "N"]:
        again = input("Do you want to play again? [Y/N] : ")[0].upper()
        if again == "N":
            return False
        elif again == "Y":
            return True
        print("Invalid input! Try again.")

    

game_on = True
while game_on:
    print("\n"*2)
    print("-------------------------")
    print("    GUESS THE NUMBER")
    print("-------------------------")
    print()
    number_range = int(input("Enter a range [1 - ???] : "))
    print()

    guess(number_range)

    game_on = play_again()
    
