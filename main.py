import random


class Game:

    def __init__(self, withBot):

        self.noneSprite = '-'

        self.grid = self.generateGrid()

        self.withBot = withBot

        self.answers = [[11, 12, 13],
                        [21, 22, 23],
                        [31, 32, 33],
                        [11, 21, 31],
                        [12, 22, 32],
                        [13, 23, 33],
                        [11, 22, 33],
                        [13, 22, 31]]

        self.playerTurn = 1
        self.playing = True


    def getGrid(self):

        gridString = ""
        currentKey = "1"

        for key, value in self.grid.items():
            previousKey = currentKey
            currentKey = key[0]
            if not currentKey == previousKey:
                gridString += "\n     " + value
            else:
                gridString += "     " + value

        return gridString


    def checkWinO(self):

        for answer in self.answers:
            answers_amount = 0
            for key, value in self.grid.items():
                if not value == "o":
                    continue
                if int(key) in answer:
                    answers_amount += 1
                    if answers_amount >= 3:
                        self.playing = False
                        return True
                else:
                    pass
        return False


    def checkWinX(self):

        for answer in self.answers:
            answers_amount = 0
            for key, value in self.grid.items():
                if not value == "x":
                    continue
                if int(key) in answer:
                    answers_amount += 1
                    if answers_amount >= 3:
                        self.playing = False
                        return True
                else:
                    pass
        return False


    def generateGrid(self):

        return {"11": self.noneSprite, "12": self.noneSprite, "13": self.noneSprite,
                "21": self.noneSprite, "22": self.noneSprite, "23": self.noneSprite,
                "31": self.noneSprite, "32": self.noneSprite, "33": self.noneSprite}


    def move(self):

        try:
            playerSprite = "O" if self.playerTurn == 1 else "X"
            if playerSprite == "X":
                if self.withBot:
                    bot.findspot()
                    if self.playerTurn == 1:
                        self.playerTurn = 2
                    else:
                        self.playerTurn = 1
                    return True
            lineColumn = input("\nPlease player " + playerSprite + " choose a line and column to go or r to restart: ")
            if lineColumn == "r":
                self.restart()

            if not self.grid[lineColumn] == self.noneSprite:
                print("\n[WARNING] Trying to cheat, try again")
                return
            self.grid[lineColumn] = playerSprite.lower()

            if self.playerTurn == 1:
                self.playerTurn = 2
            else:
                self.playerTurn = 1
        except KeyError:
            print("\n[WARNING] you choosed wrong spot, try writing something like 23")
            return

    def restart(self):
        self.playerTurn = 1
        self.playing = True
        self.grid = self.generateGrid()
        return


class BotAI:

    def __init__(self):
        self.answers = [[11, 12, 13],
                        [21, 22, 23],
                        [31, 32, 33],
                        [11, 21, 31],
                        [12, 22, 32],
                        [13, 23, 33],
                        [11, 22, 33],
                        [13, 22, 31]]

    def findspot(self):
        possibleAnswers = {"x": [],
                           "o": []}
        for answer in self.answers:
            print(answer)
            oFound = 0
            xFound = 0
            ansnwerItSelf = 0
            for spot in answer:
                ansnwerItSelf += 1
                spotted = False
                objectType = game.grid[str(spot)]
                print(objectType)
                if not objectType == game.noneSprite:
                    spotted = True
                    if objectType == "o":
                        oFound += 1
                    else:
                        xFound += 1
                print(f"{xFound} x moves, {oFound} o moves, {ansnwerItSelf} answers it self")
                if not spotted:
                    if xFound == 2:
                        possibleAnswers["x"].append(spot)
                    if oFound == 2:
                        possibleAnswers["o"].append(spot)
                if oFound == 2:
                    for spot in answer:
                        ansnwerItSelf += 1
                        spotted = False
                        objectType = game.grid[str(spot)]
                        print(objectType)
                        if not objectType == game.noneSprite:
                            spotted = True
                            if objectType == "o":
                                oFound += 1
                            else:
                                xFound += 1
                        if not spotted:
                            possibleAnswers["o"].append(spot)
                if xFound == 2:
                    for spot in answer:
                        ansnwerItSelf += 1
                        spotted = False
                        objectType = game.grid[str(spot)]
                        print(objectType)
                        if not objectType == game.noneSprite:
                            spotted = True
                            if objectType == "o":
                                oFound += 1
                            else:
                                xFound += 1
                        if not spotted:
                            possibleAnswers["x"].append(spot)
        if len(possibleAnswers["x"]) > 0:
            game.grid[str(possibleAnswers['x'][0])] = "X"
            return True
        if len(possibleAnswers["o"]) > 0:
            game.grid[str(possibleAnswers['o'][0])] = "X"
            return True
        spotting = True
        while spotting:
            spot = random.choice(list(game.grid.keys()))
            objectType = game.grid[str(spot)]
            if objectType == game.noneSprite:
                game.grid[str(spot)] = "X"
                return True


game = Game(True)
bot = BotAI()

print("\n_____________________________________________________\n|||--------------EPIC TICTACTOE GAME--------------|||\n")
while game.playing:
    print('\n\n++--------------------++\n' + game.getGrid().upper() + '\n++--------------------++\n')
    game.move()
    if game.checkWinX():
        print('\n\n++--------------------++\n' + game.getGrid().upper())
        print('\nPLAYER X HAS WON THE GAME\n++--------------------++\nRESTARRTING...')
        game.restart()
    if game.checkWinO():
        print('\n\n++--------------------++\n' + game.getGrid().upper())
        print('\nPLAYER O HAS WON THE GAME\n++--------------------++\nRESTARTING...')
        game.restart()









