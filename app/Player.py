class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.lastInput = None
    
    def convertStrToId(self): #converts a string input such as "ROCK" or "SCISSORS" into its assosciated index from the actions list.
        actions = ["ROCK","PAPER","SCISSORS"]
        for i in range(len(actions)):
            if (actions[i] == self.lastInput):
                return i
        return 3 #the action couldn't be found, Game() will ask Player again to pick an existing pick

    def newPick(self):
        self.lastInput = input("Enter Item : ")
        try:
            self.lastInput = int(self.lastInput)
        except:
            self.lastInput = self.convertStrToId()


