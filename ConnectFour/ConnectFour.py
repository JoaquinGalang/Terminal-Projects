from ConnectFourPlayer import Player
from ConnectFourPlayer import ComputerPlayer
import time

class Game:
    
    def __init__(self, player1, player2):
        self.grid = [[" ", " ", " ", " ", " ", " ", " ",],
                    [" ", " ", " ", " ", " ", " ", " ",],
                    [" ", " ", " ", " ", " ", " ", " ",],
                    [" ", " ", " ", " ", " ", " ", " ",],
                    [" ", " ", " ", " ", " ", " ", " ",],
                    [" ", " ", " ", " ", " ", " ", " ",],
                    [" ", " ", " ", " ", " ", " ", " ",],]
        self.available_moves = []
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.game_won = False
        self.game_tie = False

    def display_grid(self):
        print(" "*3 + (" "*5).join([str(n) for n in range(1, 8)]))
        print("┏━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┓")
        for num, row in enumerate(self.grid):
            print("┃  " + "  ┃  ".join(row) + "  ┃")
            if num != 6:
                print("┣━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━╋━━━━━┫")
        print("┗━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┻━━━━━┛")

    def get_available_moves(self):
        self.available_moves = []
        for column in range(7):
            for row in range(7):
                if self.grid[row][column] == " ":
                    self.available_moves.append(column)
                    break

    def make_move(self, column):
        # WRONG
        for row in range(7):
            if self.grid[row][column] != " ":
                self.grid[row-1][column] = self.current_player.symbol
                break

        if self.grid[-1][column] == " ":
            self.grid[-1][column] = self.current_player.symbol

    def win_check(self):
        pass
        # CHECK ALL HORIZONTAL
        for row in self.grid:
            for space in range(4):
                if (row[space] == row[space+1] == row[space+2] == row[space+3]) and (row[space] != " "):
                    self.game_won = True
                
        # CHECK ALL VERTICAL
        for column in range(7):
            for row in range(4):
                if (self.grid[row][column] == self.grid[row+1][column] == self.grid[row+2][column] == self.grid[row+3][column]) and (self.grid[row][column] != " "):
                    self.game_won = True
                
        # CHECK DIAGONAL (FALL)
        for column in range(4):
            for row in range(4):
                if (self.grid[row][column] == self.grid[row+1][column+1] == self.grid[row+2][column+2] == self.grid[row+3][column+3]) and (self.grid[row][column] != " "):
                    self.game_won = True

        # CHECK DIAGONAL (CLIMB)
        for column in range(4):
            for row in range(6, 2, -1):
                #print(row)
                if (self.grid[row][column] == self.grid[row-1][column+1] == self.grid[row-2][column+2] == self.grid[row-3][column+3]) and (self.grid[row][column] != " "):
                    self.game_won = True
                    
    def draw_check(self):
        if len(self.available_moves) == 0:
            self.game_tie = True

    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

def play_again():
    again = input("\n     Would you like to play again? [Y/N]: ")[0].upper()
    while again not in ["Y", "N"]:
        print("\n          Invalid input! Try again.")
        again = input("\n     Would you like to play again? [Y/N]: ")[0].upper()

    if again == "N":
        return False
    return True

def prompt_mode():
    mode = input("\n          PvP or PvC [1/2]: ")[0]
    while mode not in ["1", "2"]:
        print("\n          Invalid input! Try again.")
        mode = input("\n          PvP or PvC [1/2]: ")[0]

    if mode == "2":
        return False
    return True

game_on = True

while game_on:

    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃         WELCOME TO CONNECT FOUR         ┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

    mode = prompt_mode()

    if mode:
        # Defines player objects
        player1 = Player("X")
        player2 = Player("O")
    else:
        # Defines player and computer objects
        player1 = Player("X")
        player2 = ComputerPlayer("O")
    

    # Defines the game
    game = Game(player1, player2)

    while True:
        
        # Display grid
        game.display_grid()

        # Compiles a list of all available moves
        game.get_available_moves()

        # If it is a draw, announce the tie and end the game
        game.draw_check()
        if game.game_tie:
            print("\n"*3)
            game.display_grid()
            print("\n               It's A Draw!")
            break

        # Asks player to input their move (w/ input validation)
        chosen_column = game.current_player.get_move(game)
        game.make_move(chosen_column)
        time.sleep(.7)
        
        
        print("\n"*3)

        # If a player has won, announce the winner and end the game
        game.win_check()
        if game.game_won:
            game.display_grid()
            print(f"\n                  {game.current_player.symbol} Wins!")
            break
        
        # If it is neither a draw or a tie, switch the current player
        game.switch_player()

    print("\n"*3)

    # Asks the user if they would like to play again.
    game_on = play_again()

    print("\n"*3)