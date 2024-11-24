
def display_grid(positions):
    print("     -------------")
    print("     | {} | {} | {} |".format(positions[6], positions[7], positions[8]))
    print("     |-----------|")
    print("     | {} | {} | {} |".format(positions[3], positions[4], positions[5]))
    print("     |-----------|")
    print("     | {} | {} | {} |".format(positions[0], positions[1], positions[2]))
    print("     -------------")

def win_check(symbol, positions):
    if [symbol, symbol, symbol] == [positions[0], positions[1], positions[2]]:
        return True
    elif [symbol, symbol, symbol] == [positions[3], positions[4], positions[5]]:
        return True
    elif [symbol, symbol, symbol] == [positions[6], positions[7], positions[8]]:
        return True
    elif [symbol, symbol, symbol] == [positions[0], positions[3], positions[6]]:
        return True
    elif [symbol, symbol, symbol] == [positions[1], positions[4], positions[7]]:
        return True
    elif [symbol, symbol, symbol] == [positions[2], positions[5], positions[8]]:
        return True
    elif [symbol, symbol, symbol] == [positions[0], positions[4], positions[8]]:
        return True
    elif [symbol, symbol, symbol] == [positions[2], positions[4], positions[6]]:
        return True

def switch(symbol):
    if symbol == "X":
        return "O"
    else:
        return "X"

game_on = True
while game_on:

    print("-------------------------")
    print("      TIC TAC TOE")
    print("-------------------------")

    print("      Sample Grid ")
    print("     -------------")
    print("     | 7 | 8 | 9 |")
    print("     -------------")
    print("     | 4 | 5 | 6 |")
    print("     -------------")
    print("     | 1 | 2 | 3 |")
    print("     -------------\n")

    positions = [" "]*9

    symbol = ""
    while symbol not in ["X", "O"]:
        symbol = input("Who goes first? [X/O] : ")[0].upper()
        if symbol not in ["X", "O"]:
            print("Invalid input! Try again.")

    while True:
        print("\n"*2)
        display_grid(positions)
        

        pos = int(input("        >> ")) - 1
        while positions[pos] != " ":
            print("Invalid position! Try again.")
            pos = int(input("        >> ")) - 1
        positions[pos]  = symbol

        game_set = win_check(symbol, positions)

        if game_set:
            print("\n"*2)
            display_grid(positions)
            print(f"        {symbol} Wins!")
            break
        elif not(game_set) and " " not in positions:
            print("\n"*2)
            display_grid(positions)
            print(f"        It's a draw!")
            break

        symbol = switch(symbol)
    
    again =  ""
    while again not in ["Y", "N"]:
        again = input("\nWould you like to play again? [Y/N]: ")[0].upper()
        if again == "N":
            game_on = False
            break
        elif again == "Y":
            pass
        print("Invalid input! Try again.")
    
