import random
import pygame
from Data import DeckData
from DisplayData import PygamesDisplayData
from Actor import Actor
import numpy as np
Data = DeckData()

textRow = 100
textCol = 550

pongorKongRow = 818
pongorKongCol = 580

white = (255, 255, 255)


class Board:
    def __init__(self):
        self.tableCenter = []
        self.organizedDecks = Data.organizedDeck
        self.shuffledDecks = self.shuffleDecks()
        self.players = self.assignStartDecks()
        self.currentPlayer = 0
        self.lastPlayer = 0
        self.pongPlayer = []
        self.kongPlayer = []
        self.skip = []
        self.start = []
        self.shang = []
        self.pongKong = []
        self.hu = []
        self.numberOfTurns = 0
        self.currentPlayerDisplay = "Current Player is : " + str(self.currentPlayer + 1)
        self.newRound = True
        self.gameOn = False
        self.currentRoundCannotShang = True
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
            # If first player assign him 14 cards
            if i == 0:
                actorCard = self.shuffledDecks[:14]
                players.append(Actor(actorCard, i))
                separateList = self.shuffledDecks[15:]
                self.shuffledDecks = separateList
            # Other players assign 13 cards
            else:
                actorCard = self.shuffledDecks[:13]
                players.append(Actor(actorCard, i))
                separateList = self.shuffledDecks[14:]
                self.shuffledDecks = separateList
        return players

    def getNextPlayer(self):
        nextPlayerIndex = (self.currentPlayer + 1) % 4
        return self.players[nextPlayerIndex]

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
        smallerfont = pygame.font.Font('freesansbold.ttf', 16)

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
        scrn.fill((0, 163, 108))

        status = True
        while (status):
            if self.gameOn:
                if self.numberOfTurns != 0 and self.newRound and not self.pongKongAvailable() and not self.shangAvailable():
                    self.playerTakeNewCard(self.players[self.currentPlayer])
                    self.newRound = False
                    self.numberOfTurns += 1
                else :
                    self.newRound = False

                scrn.fill((0, 163, 108))
                self.visibleTilesSpriteLocation = []

                display.displaytable(scrn, self.tableCenter)

                if self.huAvailable():
                    playerThatCanHu = self.getPlayerCanHu()
                    print(playerThatCanHu, self.players[playerThatCanHu].decks)
                    if playerThatCanHu is not None :
                        HU = font.render('HU PLAYER : ' + str(self.currentPlayer + 1), True, white)
                        hutextrect = HU.get_rect()
                        hutextrect.center = (pongorKongCol // 2, pongorKongRow // 2)
                        hu = scrn.blit(HU, hutextrect)
                        self.hu.append(hu)
                        display.displayPlayer(scrn, self.players[playerThatCanHu])
                        display.displayPlayerPongKong(scrn, self.players[playerThatCanHu])
                        SKIP = font.render('SKIP', True, white)
                        skiptextrect = SKIP.get_rect()
                        skiptextrect.center = (pongorKongCol // 2, startingRow + 64)
                        a = scrn.blit(SKIP, skiptextrect)
                        self.skip.append(a)
                elif self.pongKongAvailable():
                    print("pong kong available")
                    print("pong: ", self.pongPlayer)
                    print("kong: ", self.kongPlayer)
                    players = self.pongPlayer + self.kongPlayer
                    PONGKONG = font.render('PONG / KONG PLAYER : ' + str(players[0]+1), True, white)
                    pngkngtextrect = PONGKONG.get_rect()
                    pngkngtextrect.center = (pongorKongCol // 2, pongorKongRow // 2)
                    pongKong = scrn.blit(PONGKONG, pngkngtextrect)
                    self.pongKong.append(pongKong)
                    players = self.getAllPongKongAvailablePlayer()
                    startingRow = display.startingRow
                    for player in players:
                        self.visibleTilesSpriteLocation += display.displayPlayerActivePongKong(scrn, self.players[player], player, startingRow)
                        display.displayPlayerPongKong(scrn, self.players[player])
                        startingRow += 32
                    SKIP = font.render('SKIP', True, white)
                    skiptextrect = SKIP.get_rect()
                    skiptextrect.center = (pongorKongCol // 2, startingRow + 64)
                    a = scrn.blit(SKIP, skiptextrect)
                    self.skip.append(a)
                else:
                    if self.shangAvailable():
                        EAT = font.render('EAT', True, white)
                        eattextrect = EAT.get_rect()
                        eattextrect.center = (pongorKongCol // 2, pongorKongRow // 2)
                        eat = scrn.blit(EAT, eattextrect)
                        self.shang.append(eat)
                        display.displayPlayer(scrn, self.players[self.currentPlayer])
                        display.displayPlayerPongKong(scrn, self.players[self.currentPlayer])
                        SKIP = font.render('SKIP', True, white)
                        skiptextrect = SKIP.get_rect()
                        skiptextrect.center = (pongorKongCol // 2, display.startingRow + 96)
                        a = scrn.blit(SKIP, skiptextrect)
                        self.skip.append(a)
                    else :
                        self.visibleTilesSpriteLocation = display.displayPlayer(scrn, self.players[self.currentPlayer])
                        display.displayPlayerPongKong(scrn, self.players[self.currentPlayer])


                text = font.render(self.currentPlayerDisplay, True, white)
                textRect = text.get_rect()
                textRect.center = (textCol // 2, textRow // 2)
                scrn.blit(text, textRect)
                # paint screen one time
                pygame.display.flip()
            else:
                self.start.append(display.displayNewGameScreen(scrn))

            # iterate over the list of Event objects
            # that was returned by pygame.event.get() method.
            for i in pygame.event.get():

                # if event object type is QUIT
                # then quitting the pygame
                # and program both.
                if i.type == pygame.QUIT:
                    status = False
                if self.gameOn:
                    if i.type == pygame.MOUSEBUTTONDOWN:
                        if self.huAvailable():
                            print("Waiting for HU")
                            # pos = pygame.mouse.get_pos()
                            # if self.huClicked(pos[0], pos[1]):
                            #     print("hu")

                        elif self.pongKongAvailable():
                            pos = pygame.mouse.get_pos()
                            if self.skipClicked(pos[0], pos[1]):
                                print("skip")
                                self.clearPongOrKongPlayer()
                                self.newRound = True
                            elif self.pongKongClicked(pos[0], pos[1]):
                                players = self.pongPlayer + self.kongPlayer
                                player = players[0]
                                pongPieces = self.tableCenter.pop(-1)
                                if player in self.pongPlayer:
                                    self.players[player].pong(pongPieces)
                                elif player in self.kongPlayer:
                                    self.players[player].kong(pongPieces)
                                    self.playerTakeNewCard(self.players[player])
                                self.setCurrentPlayer(player)
                                self.clearPongOrKongPlayer()
                                # If you have pong or kong, you cannot shang anymore
                                self.clearShang()
                                self.newRound = False
                        elif self.shangAvailable():
                            pos = pygame.mouse.get_pos()
                            if self.skipClicked(pos[0], pos[1]):
                                print("skip")
                                self.clearShang()
                                self.newRound = True
                            elif self.shangClicked(pos[0], pos[1]):
                                deck = self.tableCenter.pop(-1)
                                self.players[self.currentPlayer].shang(deck)
                                self.clearShang()
                                self.newRound = False
                        else :
                            pos = pygame.mouse.get_pos()
                            (available, tile) = self.availablePieces(pos[0], pos[1])
                            if available:
                                if self.players[self.currentPlayer].removeDeck(self.mapDeckEnglish(tile)):
                                    self.tableCenter.append(self.mapDeckEnglish(tile))
                                    if self.getNextPlayer().canShang(self.mapDeckEnglish(tile)):
                                        self.currentRoundCannotShang = False
                                    self.nextPlayer(self.mapDeckEnglish(tile))
                                    self.currentPlayerDisplay = "Current Player : " + str(self.currentPlayer + 1)
                                    self.newRound = True
                else:
                    if i.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if self.startClicked(pos[0], pos[1]):
                            self.gameOn = True
                            self.start = []
        pygame.quit()

    def nextPlayer(self, newDeck, pongKongPlayer=None):
        if pongKongPlayer is not None:
            self.lastPlayer = self.currentPlayer
            self.currentPlayer = (pongKongPlayer + 1) % 4
        else :
            self.clearPongOrKongPlayer()
            self.lastPlayer = self.currentPlayer
            self.currentPlayer = (self.currentPlayer + 1) % 4
            self.numberOfTurns += 1
        if newDeck is not None:
            for player in range(len(self.players)):
                if player != (self.lastPlayer)%4:
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
        self.skip = []

    def clearShang(self):
        self.currentRoundCannotShang = True
        self.shang = []
        self.skip = []


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

    def availablePongKongPieces(self, row, col):
        for i in self.visibleTilesSpriteLocation:
            curRow = i[1][0]
            curCol = i[1][1]
            curRowMax = curRow + 24
            curColMax = curCol + 32
            if row >= curRow and row <= curRowMax and col >= curCol and col <= curColMax:
                return (True, i[0])
        return (False, None)
    def pongKongClicked(self, row, col):
        if self.pongKong != [] :
            return self.buttonClicked(self.pongKong[0], row, col)
        return False

    def skipClicked(self, row, col):
        if self.skip != [] :
            return self.buttonClicked(self.skip[0], row, col)
        return False

    def shangClicked(self, row, col):
        if self.shang != [] :
            return self.buttonClicked(self.shang[0], row, col)
        return False

    def startClicked(self, row, col):
        if self.start != [] :
            return self.buttonClicked(self.start[0], row, col)
        return False

    def huClicked(self, row, col):
        if self.hu != [] :
            return self.buttonClicked(self.hu[0], row, col)
        return False

    def buttonClicked(self, button, mouseRow, mouseCol):
        startRowMin = button.topleft[0]
        startColMin = button.topleft[1]
        startRowMax = button.bottomright[0]
        startColMax = button.bottomright[1]
        if mouseRow >= startRowMin and mouseRow <= startRowMax and mouseCol >= startColMin and mouseCol <= startColMax:
            return True
        return False

    def pongKongAvailable(self):
        return self.pongPlayer != [] or self.kongPlayer != []

    def huAvailable(self):
        for player in range(len(self.players)):
            if self.players[player].canHu():
                return True
            if len(self.tableCenter) > 0 and self.players[player].canHu(self.tableCenter[-1]):
                return True
        return False

    def getPlayerCanHu(self):
        for player in range(len(self.players)):
            if self.players[player].canHu():
                return player
            if len(self.tableCenter) > 0 and self.players[player].canHu(self.tableCenter[-1]):
                return player
        return None

    def shangAvailable(self):
        return len(self.tableCenter) >= 1 and (self.players[self.currentPlayer].canShang(self.tableCenter[-1])) and self.currentRoundCannotShang == False

    def getAllPongKongAvailablePlayer(self):
        return self.pongPlayer + self.kongPlayer
game = Board()