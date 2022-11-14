from random import choice

class Game:

    def __init__(self, player1, player2, winCond = 3):
        self.actions = ["ROCK", "PAPER", "SCISSORS"] #an item is beaten by the item at his right but beats the item at his left. The first item beats the last item.
        self.players = [player1,player2]
        self.winnerId = None
        self.winCond = winCond #Amount of round a player must win to win the game

    def updateWinner(self):
        self.winnerId = self.checkWinner()
        if (self.winnerId != None):
            self.players[self.winnerId].score += 1

    def checkWinner(self):
        if (self.players[0].lastInput == self.players[1].lastInput):
            return None #in case of draw.
        elif(self.players[0].lastInput-self.players[1].lastInput in [1,-len(self.actions)+1]):
            return 0
        else:
            return 1

    def game(self):
        while (self.winCond not in [self.players[i].score for i in range(len(self.players))]):
            for player in self.players:
                print(player.name + "'s turn !")
                player.lastInput = None
                while player.lastInput not in [0,1,2]:
                    player.newPick()
                print(self.actions[player.lastInput])
            self.updateWinner()
            if self.winnerId == None:
                print("DRAW")
            else:
                print("The round winner is " + self.players[self.winnerId].name)
        print("The game winner is " + self.players[self.winnerId].name)

if (__name__ == "__main__"):
    from app.Player import *
    from app.Computer import *
    game = Game(Player("Player1"), Computer())
    game.game()