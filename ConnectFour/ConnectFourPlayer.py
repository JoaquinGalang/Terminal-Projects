import random

# PLAYER CLASS
class Player:
    
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, game):
        move = None
        while move not in game.available_moves:
            move = int(input("\n             Enter a column: "))-1
        return move
    
class ComputerPlayer(Player):

    def get_move(self, game):
        return random.choice(game.available_moves)