import random
import pygame
from Data import DeckData
from DisplayData import PygamesDisplayData
from Actor import Actor
Data = DeckData()
startingRow = 450
startingCol = 130

tableRow = 150
tableCol = 130

textRow = 100
textCol = 550

white = (255, 255, 255)


class Board:
    def __init__(self):
        self.tableCenter = []
        self.organizedDecks = Data.organizedDeck
        self.shuffledDecks = self.shuffleDecks()
        self.players = self.assignStartDecks()
        self.currentPlayer = 0
        self.pongPlayer = []
        self.kongPlayer = []
        self.numberOfTurns = 0
        self.currentPlayerDisplay = "Current Player is : " + str(self.currentPlayer + 1)
        self.lastRoundIsPong = False
        self.newRound = True
        self.visibleTilesSpriteLocation = []
        self.displayBoard()

    def shuffleDecks(self):
        self.newDecks = []
        deckSize = len(self.organizedDecks) - 1
        for i in range (len(self.organizedDecks)):
            currentDeck = random.randint(0, deckSize)
            self.newDecks.append(self.organizedDecks.pop(currentDeck))
            deckSize = deckSize - 1
        return self.newDecks

    def assignStartDecks(self):
        players = []
        for i in range(4):
            # If first player assign him 13 cards
            if i == 0:
                actorCard = self.shuffledDecks[:13]
                players.append(Actor(actorCard, i))
                separateList = self.shuffledDecks[14:]
                self.shuffledDecks = separateList
            # Other players assign 12 cards
            else:
                actorCard = self.shuffledDecks[:12]
                players.append(Actor(actorCard, i))
                separateList = self.shuffledDecks[13:]
                self.shuffledDecks = separateList
        return players

    def displayBoard(self):
        # activate the pygame library .
        pygame.init()
        X = 600
        Y = 600

        # create the display surface object
        # of specific dimension..e(X, Y).
        scrn = pygame.display.set_mode((X, Y))

        # set the pygame window name
        pygame.display.set_caption('MahJong')

        font = pygame.font.Font('freesansbold.ttf', 32)

        # create a text surface object,
        # on which text is drawn on it.
        text = font.render('Current Player: 0', True, white)

        # create a rectangular object for the
        # text surface object
        textRect = text.get_rect()

        # set the center of the rectangular object.
        textRect.center = (textRow // 2, textCol // 2)

        # create a surface object, image is drawn on it.
        display = PygamesDisplayData(pygame)

        status = True
        while (status):
            if self.newRound:
                print(self.newRound)
            if self.numberOfTurns != 0 and self.newRound:
                # if self.lastRoundIsPong:
                #     self.lastRoundIsPong = False
                #     self.newRound = False
                # else:
                self.playerTakeNewCard(self.players[self.currentPlayer])
                self.newRound = False
            else :
                self.newRound = False
            scrn.fill((0, 163, 108))
            self.visibleTilesSpriteLocation = []

            display.displaytable(scrn, self.tableCenter)

            # for player in self.players:
            #     player.display()
            # Using blit to copy content from one surface to other
            rowDisplayIndex = startingRow
            # for player in range(len(self.players)):
            #

            # if player can pong / kong then display those player
            # if self.pongPlayer != [] or self.kongPlayer != []:
            #     displayUser = self.pongPlayer.extend(self.kongPlayer)
            #     for user in displayUser:

            self.visibleTilesSpriteLocation = display.displayPlayer(scrn, self.players[self.currentPlayer])
            display.displayPlayerPongKong(scrn, self.players[self.currentPlayer])


            text = font.render(self.currentPlayerDisplay, True, white)
            textRect = text.get_rect()
            textRect.center = (textCol // 2, textRow // 2)
            scrn.blit(text, textRect)
            # paint screen one time
            pygame.display.flip()
            # iterate over the list of Event objects
            # that was returned by pygame.event.get() method.
            for i in pygame.event.get():

                # if event object type is QUIT
                # then quitting the pygame
                # and program both.
                if i.type == pygame.QUIT:
                    status = False

                if i.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    (available, tile) = self.availablePieces(pos[0], pos[1])
                    if available:
                        if self.players[self.currentPlayer].removeDeck(self.mapDeckEnglish(tile)):
                            self.tableCenter.append(self.mapDeckEnglish(tile))
                            self.nextPlayer(self.mapDeckEnglish(tile))
                            self.currentPlayerDisplay = "Current Player : " + str(self.currentPlayer + 1)
                            self.newRound = True



            # print(self.currentPlayerDisplay)
            # while True:
            #     print("Player that can Pong : ", self.pongPlayer)
            #     print("Player that can Kong : ", self.kongPlayer)
            #     if len(self.pongPlayer) != 0:
            #         print("PONG available player : ", self.pongPlayer)
            #         a = input("Please select a valid player to Pong : ")
            #         print(a, int(a) in self.pongPlayer)
            #         pongPieces = self.tableCenter.pop(-1)
            #         if int(a) in self.pongPlayer or int(a) in self.kongPlayer:
            #             player = self.players[int(a)]
            #             if int(a) in self.pongPlayer:
            #                 player.pong(pongPieces)
            #             elif int(a) in self.kongPlayer:
            #                 player.kong(pongPieces)
            #             self.setCurrentPlayer(int(a))
            #             self.clearPongOrKongPlayer()
            #             break
            #     else:
            #         a = input("Please play ? ")
            #         print(a, self.mapDeck(a))
            #         if self.players[self.currentPlayer].removeDeck(self.mapDeck(a)):
            #             self.tableCenter.append(self.mapDeck(a))
            #             self.nextPlayer(self.mapDeck(a))
            #             self.currentPlayerDisplay = "Current Player : " + str(self.currentPlayer + 1)
            #             pygame.display.flip()
            #             break
        # deactivates the pygame library
        pygame.quit()

    def nextPlayer(self, newDeck, pongKongPlayer=None):
        if pongKongPlayer is not None:
            self.currentPlayer = (pongKongPlayer + 1) % 4
        else :
            self.clearPongOrKongPlayer()
            self.currentPlayer = (self.currentPlayer + 1) % 4
            self.numberOfTurns += 1
        if newDeck is not None:
            for player in range(len(self.players)):
                if self.players[player].canPong(newDeck):
                    self.pongPlayer.append(player)
                elif self.players[player].canKong(newDeck):
                    self.kongPlayer.append(player)

    def mapDeck(self, deckName):
        return Data.deckChinese[deckName]

    def mapDeckEnglish(self, deckName):
        return Data.deck[deckName]

    def playerTakeNewCard(self, player):
        player.addDeck(self.shuffledDecks.pop(0))

    def clearPongOrKongPlayer(self):
        self.pongPlayer = []
        self.kongPlayer = []
        self.lastRoundIsPong = True

    def setCurrentPlayer(self, player):
        self.currentPlayer = player

    def availablePieces(self, row, col):
        print(row, col)
        for i in self.visibleTilesSpriteLocation:
            curRow = i[1][0]
            curCol = i[1][1]
            curRowMax = curRow + 24
            curColMax = curCol + 32
            if row >= curRow and row <= curRowMax and col >= curCol and col <= curColMax:
                return (True, i[0])
        return (False, None)
game = Board()