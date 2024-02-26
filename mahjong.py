import random
import pygame
<<<<<<< HEAD
from Data import DeckData
from DisplayData import PygamesDisplayData
from Actor import Actor
Data = DeckData()
=======
import numpy as np
deck = {
    'east': 1,
    'west': 2,
    'north': 3,
    'south': 4,
    'space': 5,
    'fa': 6,
    'center': 7,
    'oneTong': 8,
    'twoTong': 9,
    'threeTong': 10,
    'fourTong': 11,
    'fiveTong': 12,
    'sixTong': 13,
    'sevenTong': 14,
    'eightTong': 15,
    'nineTong': 16,
    'oneWan': 17,
    'twoWan': 18,
    'threeWan': 19,
    'fourWan': 20,
    'fiveWan': 21,
    'sixWan': 22,
    'sevenWan': 23,
    'eightWan': 24,
    'nineWan': 25,
    'oneTiao': 26,
    'twoTiao': 27,
    'threeTiao': 28,
    'fourTiao': 29,
    'fiveTiao': 30,
    'sixTiao': 31,
    'sevenTiao': 32,
    'eightTiao': 33,
    'nineTiao': 34,
}
deckChinese = {
    '东': 1,
    '西': 2,
    '北': 3,
    '南': 4,
    '白': 5,
    '发': 6,
    '中': 7,
    '一筒': 8,
    '三筒': 9,
    '三筒': 10,
    '四筒': 11,
    '五筒': 12,
    '六筒': 13,
    '七筒': 14,
    '八筒': 15,
    '九筒': 16,
    '一万': 17,
    '二万': 18,
    '三万': 19,
    '四万': 20,
    '五万': 21,
    '六万': 22,
    '七万': 23,
    '八万': 24,
    '九万': 25,
    '一条': 26,
    '二条': 27,
    '三条': 28,
    '四条': 29,
    '五条': 30,
    '六条': 31,
    '七条': 32,
    '八条': 33,
    '九条': 34,
}
startingRow = 450
startingCol = 130

tableRow = 150
tableCol = 130

>>>>>>> 3aa8897abe7e9a6b29da2bf472dd99ac90beda11
textRow = 100
textCol = 550
white = (255, 255, 255)

class Board:
    def __init__(self):
        self.tableCenter = []
<<<<<<< HEAD
        self.organizedDecks = Data.organizedDeck
        self.shuffledDecks = self.shuffleDecks()
=======
        self.organizedDecks = [deck['east'], deck['east'], deck['east'], deck['east'],
                            deck['north'], deck['north'], deck['north'], deck['north'],
                            deck['west'], deck['west'], deck['west'], deck['west'],
                            deck['south'], deck['south'], deck['south'], deck['south'],
                            deck['center'], deck['center'], deck['center'], deck['center'],
                            deck['fa'], deck['fa'], deck['fa'], deck['fa'],
                            deck['space'], deck['space'], deck['space'], deck['space'],

                            deck['oneTong'], deck['oneTong'], deck['oneTong'], deck['oneTong'],
                            deck['twoTong'], deck['twoTong'], deck['twoTong'], deck['twoTong'],
                            deck['threeTong'], deck['threeTong'], deck['threeTong'], deck['threeTong'],
                            deck['fourTong'], deck['fourTong'], deck['fourTong'], deck['fourTong'],
                            deck['fiveTong'], deck['fiveTong'], deck['fiveTong'], deck['fiveTong'],
                            deck['sixTong'], deck['sixTong'], deck['sixTong'], deck['sixTong'],
                            deck['sevenTong'], deck['sevenTong'], deck['sevenTong'], deck['sevenTong'],
                            deck['eightTong'], deck['eightTong'], deck['eightTong'], deck['eightTong'],
                            deck['nineTong'], deck['nineTong'], deck['nineTong'], deck['nineTong'],

                            deck['oneTiao'], deck['oneTiao'], deck['oneTiao'], deck['oneTiao'],
                            deck['twoTiao'], deck['twoTiao'], deck['twoTiao'], deck['twoTiao'],
                            deck['threeTiao'], deck['threeTiao'], deck['threeTiao'], deck['threeTiao'],
                            deck['fourTiao'], deck['fourTiao'], deck['fourTiao'], deck['fourTiao'],
                            deck['fiveTiao'], deck['fiveTiao'], deck['fiveTiao'], deck['fiveTiao'],
                            deck['sixTiao'], deck['sixTiao'], deck['sixTiao'], deck['sixTiao'],
                            deck['sevenTiao'], deck['sevenTiao'], deck['sevenTiao'], deck['sevenTiao'],
                            deck['eightTiao'], deck['eightTiao'], deck['eightTiao'], deck['eightTiao'],
                            deck['nineTiao'], deck['nineTiao'], deck['nineTiao'], deck['nineTiao'],

                            deck['oneWan'], deck['oneWan'], deck['oneWan'], deck['oneWan'],
                            deck['twoWan'], deck['twoWan'], deck['twoWan'], deck['twoWan'],
                            deck['threeWan'], deck['threeWan'], deck['threeWan'], deck['threeWan'],
                            deck['fourWan'], deck['fourWan'], deck['fourWan'], deck['fourWan'],
                            deck['fiveWan'], deck['fiveWan'], deck['fiveWan'], deck['fiveWan'],
                            deck['sixWan'], deck['sixWan'], deck['sixWan'], deck['sixWan'],
                            deck['sevenWan'], deck['sevenWan'], deck['sevenWan'], deck['sevenWan'],
                            deck['eightWan'], deck['eightWan'], deck['eightWan'], deck['eightWan'],
                            deck['nineWan'], deck['nineWan'], deck['nineWan'], deck['nineWan'],
                            ]
        self.shuffledDecks = list(np.random.permutation(self.organizedDecks))
>>>>>>> 3aa8897abe7e9a6b29da2bf472dd99ac90beda11
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

    def assignStartDecks(self):
        players = []
        for i in range(4):
            actorCard = self.shuffledDecks[:12]
            self.shuffledDecks = self.shuffledDecks[13:]
            if i == 0: # If first player assign him 13 cards
                actorCard.append(self.shuffledDecks[0])
                self.shuffledDecks = self.shuffledDecks[1:]
            players.append(Actor(actorCard, i))
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

<<<<<<< HEAD
        display = PygamesDisplayData(pygame)
=======
        # create a surface object, image is drawn on it.
        center = pygame.image.load(".\\mahjong tiles\\center.png").convert_alpha()
        east = pygame.image.load(".\\mahjong tiles\\east.png").convert_alpha()
        west = pygame.image.load(".\\mahjong tiles\\west.png").convert_alpha()
        south = pygame.image.load(".\\mahjong tiles\\south.png").convert_alpha()
        north = pygame.image.load(".\\mahjong tiles\\north.png").convert_alpha()
        fa = pygame.image.load(".\\mahjong tiles\\fa.png").convert_alpha()
        space = pygame.image.load(".\\mahjong tiles\\space.png").convert_alpha()
        oneTong = pygame.image.load(".\\mahjong tiles\\oneTong.png").convert_alpha()
        twoTong = pygame.image.load(".\\mahjong tiles\\twoTong.png").convert_alpha()
        threeTong = pygame.image.load(".\\mahjong tiles\\threeTong.png").convert_alpha()
        fourTong = pygame.image.load(".\\mahjong tiles\\fourTong.png").convert_alpha()
        fiveTong = pygame.image.load(".\\mahjong tiles\\fiveTong.png").convert_alpha()
        sixTong = pygame.image.load(".\\mahjong tiles\\sixTong.png").convert_alpha()
        sevenTong = pygame.image.load(".\\mahjong tiles\\sevenTong.png").convert_alpha()
        eightTong = pygame.image.load(".\\mahjong tiles\\eightTong.png").convert_alpha()
        nineTong = pygame.image.load(".\\mahjong tiles\\nineTong.png").convert_alpha()

        oneWan = pygame.image.load(".\\mahjong tiles\\oneWan.png").convert_alpha()
        twoWan= pygame.image.load(".\\mahjong tiles\\twoWan.png").convert_alpha()
        threeWan= pygame.image.load(".\\mahjong tiles\\threeWan.png").convert_alpha()
        fourWan = pygame.image.load(".\\mahjong tiles\\fourWan.png").convert_alpha()
        fiveWan = pygame.image.load(".\\mahjong tiles\\fiveWan.png").convert_alpha()
        sixWan = pygame.image.load(".\\mahjong tiles\\sixWan.png").convert_alpha()
        sevenWan = pygame.image.load(".\\mahjong tiles\\sevenWan.png").convert_alpha()
        eightWan = pygame.image.load(".\\mahjong tiles\\eightWan.png").convert_alpha()
        nineWan = pygame.image.load(".\\mahjong tiles\\nineWan.png").convert_alpha()

        oneTiao = pygame.image.load(".\\mahjong tiles\\oneTiao.png").convert_alpha()
        twoTiao = pygame.image.load(".\\mahjong tiles\\twoTiao.png").convert_alpha()
        threeTiao= pygame.image.load(".\\mahjong tiles\\threeTiao.png").convert_alpha()
        fourTiao = pygame.image.load(".\\mahjong tiles\\fourTiao.png").convert_alpha()
        fiveTiao = pygame.image.load(".\\mahjong tiles\\fiveTiao.png").convert_alpha()
        sixTiao = pygame.image.load(".\\mahjong tiles\\sixTiao.png").convert_alpha()
        sevenTiao = pygame.image.load(".\\mahjong tiles\\sevenTiao.png").convert_alpha()
        eightTiao = pygame.image.load(".\\mahjong tiles\\eightTiao.png").convert_alpha()
        nineTiao = pygame.image.load(".\\mahjong tiles\\nineTiao.png").convert_alpha()

>>>>>>> 3aa8897abe7e9a6b29da2bf472dd99ac90beda11

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

<<<<<<< HEAD
            display.displaytable(scrn, self.tableCenter)

            # for player in self.players:
            #     player.display()
=======
            tableRowIndex = tableRow
            displayIndex = tableCol
            numberOfPieces = 0
            for i in self.tableCenter :
                    if i == deck['east']:
                        scrn.blit(east, (displayIndex, tableRowIndex))
                    elif i == deck['west']:
                        scrn.blit(west, (displayIndex, tableRowIndex))
                    elif i == deck['north']:
                        scrn.blit(north, (displayIndex, tableRowIndex))
                    elif i == deck['south']:
                        scrn.blit(south, (displayIndex, tableRowIndex))
                    elif i == deck['center']:
                        scrn.blit(center, (displayIndex, tableRowIndex))
                    elif i == deck['space']:
                        scrn.blit(space, (displayIndex, tableRowIndex))
                    elif i == deck['fa']:
                        scrn.blit(fa, (displayIndex, tableRowIndex))
                    elif i == deck['oneTong']:
                        scrn.blit(oneTong, (displayIndex, tableRowIndex))
                    elif i == deck['twoTong']:
                        scrn.blit(twoTong, (displayIndex, tableRowIndex))
                    elif i == deck['threeTong']:
                        scrn.blit(threeTong, (displayIndex, tableRowIndex))
                    elif i == deck['fourTong']:
                        scrn.blit(fourTong, (displayIndex, tableRowIndex))
                    elif i == deck['fiveTong']:
                        scrn.blit(fiveTong, (displayIndex, tableRowIndex))
                    elif i == deck['sixTong']:
                        scrn.blit(sixTong, (displayIndex, tableRowIndex))
                    elif i == deck['sevenTong']:
                        scrn.blit(sevenTong, (displayIndex, tableRowIndex))
                    elif i == deck['eightTong']:
                        scrn.blit(eightTong, (displayIndex, tableRowIndex))
                    elif i == deck['nineTong']:
                        scrn.blit(nineTong, (displayIndex, tableRowIndex))
                    elif i == deck['oneWan']:
                        scrn.blit(oneWan, (displayIndex, tableRowIndex))
                    elif i == deck['twoWan']:
                        scrn.blit(twoWan, (displayIndex, tableRowIndex))
                    elif i == deck['threeWan']:
                        scrn.blit(threeWan, (displayIndex, tableRowIndex))
                    elif i == deck['fourWan']:
                        scrn.blit(fourWan, (displayIndex, tableRowIndex))
                    elif i == deck['fiveWan']:
                        scrn.blit(fiveWan, (displayIndex, tableRowIndex))
                    elif i == deck['sixWan']:
                        scrn.blit(sixWan, (displayIndex, tableRowIndex))
                    elif i == deck['sevenWan']:
                        scrn.blit(sevenWan, (displayIndex, tableRowIndex))
                    elif i == deck['eightWan']:
                        scrn.blit(eightWan, (displayIndex, tableRowIndex))
                    elif i == deck['nineWan']:
                        scrn.blit(nineWan, (displayIndex, tableRowIndex))
                    elif i == deck['oneTiao']:
                        scrn.blit(oneTiao, (displayIndex, tableRowIndex))
                    elif i == deck['twoTiao']:
                        scrn.blit(twoTiao, (displayIndex, tableRowIndex))
                    elif i == deck['threeTiao']:
                        scrn.blit(threeTiao, (displayIndex, tableRowIndex))
                    elif i == deck['fourTiao']:
                        scrn.blit(fourTiao, (displayIndex, tableRowIndex))
                    elif i == deck['fiveTiao']:
                        scrn.blit(fiveTiao, (displayIndex, tableRowIndex))
                    elif i == deck['sixTiao']:
                        scrn.blit(sixTiao, (displayIndex, tableRowIndex))
                    elif i == deck['sevenTiao']:
                        scrn.blit(sevenTiao, (displayIndex, tableRowIndex))
                    elif i == deck['eightTiao']:
                        scrn.blit(eightTiao, (displayIndex, tableRowIndex))
                    elif i == deck['nineTiao']:
                        scrn.blit(nineTiao, (displayIndex, tableRowIndex))
                    numberOfPieces += 1
                    numberOfRow = numberOfPieces//13
                    numberofCol = numberOfPieces%13
                    displayIndex = tableCol + numberofCol*24
                    tableRowIndex = tableRow + numberOfRow*32

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

            currentPlayer = self.players[self.currentPlayer]
            displayIndex = startingCol
            for i in currentPlayer.decks:
                if i == deck['east']:
                    self.visibleTilesSpriteLocation.append(('east', (displayIndex, rowDisplayIndex)))
                    scrn.blit(east, (displayIndex, rowDisplayIndex))
                elif i == deck['west']:
                    self.visibleTilesSpriteLocation.append(('west', (displayIndex, rowDisplayIndex)))
                    scrn.blit(west, (displayIndex, rowDisplayIndex))
                elif i == deck['north']:
                    self.visibleTilesSpriteLocation.append(('north', (displayIndex, rowDisplayIndex)))
                    scrn.blit(north, (displayIndex, rowDisplayIndex))
                elif i == deck['south']:
                    self.visibleTilesSpriteLocation.append(('south', (displayIndex, rowDisplayIndex)))
                    scrn.blit(south, (displayIndex, rowDisplayIndex))
                elif i == deck['center']:
                    self.visibleTilesSpriteLocation.append(('center', (displayIndex, rowDisplayIndex)))
                    scrn.blit(center, (displayIndex, rowDisplayIndex))
                elif i == deck['space']:
                    self.visibleTilesSpriteLocation.append(('space', (displayIndex, rowDisplayIndex)))
                    scrn.blit(space, (displayIndex, rowDisplayIndex))
                elif i == deck['fa']:
                    self.visibleTilesSpriteLocation.append(('fa', (displayIndex, rowDisplayIndex)))
                    scrn.blit(fa, (displayIndex, rowDisplayIndex))
                elif i == deck['oneTong']:
                    self.visibleTilesSpriteLocation.append(('oneTong', (displayIndex, rowDisplayIndex)))
                    scrn.blit(oneTong, (displayIndex, rowDisplayIndex))
                elif i == deck['twoTong']:
                    self.visibleTilesSpriteLocation.append(('twoTong', (displayIndex, rowDisplayIndex)))
                    scrn.blit(twoTong, (displayIndex, rowDisplayIndex))
                elif i == deck['threeTong']:
                    self.visibleTilesSpriteLocation.append(('threeTong', (displayIndex, rowDisplayIndex)))
                    scrn.blit(threeTong, (displayIndex, rowDisplayIndex))
                elif i == deck['fourTong']:
                    self.visibleTilesSpriteLocation.append(('fourTong', (displayIndex, rowDisplayIndex)))
                    scrn.blit(fourTong, (displayIndex, rowDisplayIndex))
                elif i == deck['fiveTong']:
                    self.visibleTilesSpriteLocation.append(('fiveTong', (displayIndex, rowDisplayIndex)))
                    scrn.blit(fiveTong, (displayIndex, rowDisplayIndex))
                elif i == deck['sixTong']:
                    self.visibleTilesSpriteLocation.append(('sixTong', (displayIndex, rowDisplayIndex)))
                    scrn.blit(sixTong, (displayIndex, rowDisplayIndex))
                elif i == deck['sevenTong']:
                    self.visibleTilesSpriteLocation.append(('sevenTong', (displayIndex, rowDisplayIndex)))
                    scrn.blit(sevenTong, (displayIndex, rowDisplayIndex))
                elif i == deck['eightTong']:
                    self.visibleTilesSpriteLocation.append(('eightTong', (displayIndex, rowDisplayIndex)))
                    scrn.blit(eightTong, (displayIndex, rowDisplayIndex))
                elif i == deck['nineTong']:
                    self.visibleTilesSpriteLocation.append(('nineTong', (displayIndex, rowDisplayIndex)))
                    scrn.blit(nineTong, (displayIndex, rowDisplayIndex))
                elif i == deck['oneWan']:
                    self.visibleTilesSpriteLocation.append(('oneWan', (displayIndex, rowDisplayIndex)))
                    scrn.blit(oneWan, (displayIndex, rowDisplayIndex))
                elif i == deck['twoWan']:
                    self.visibleTilesSpriteLocation.append(('twoWan', (displayIndex, rowDisplayIndex)))
                    scrn.blit(twoWan, (displayIndex, rowDisplayIndex))
                elif i == deck['threeWan']:
                    self.visibleTilesSpriteLocation.append(('threeWan', (displayIndex, rowDisplayIndex)))
                    scrn.blit(threeWan, (displayIndex, rowDisplayIndex))
                elif i == deck['fourWan']:
                    self.visibleTilesSpriteLocation.append(('fourWan', (displayIndex, rowDisplayIndex)))
                    scrn.blit(fourWan, (displayIndex, rowDisplayIndex))
                elif i == deck['fiveWan']:
                    self.visibleTilesSpriteLocation.append(('fiveWan', (displayIndex, rowDisplayIndex)))
                    scrn.blit(fiveWan, (displayIndex, rowDisplayIndex))
                elif i == deck['sixWan']:
                    self.visibleTilesSpriteLocation.append(('sixWan', (displayIndex, rowDisplayIndex)))
                    scrn.blit(sixWan, (displayIndex, rowDisplayIndex))
                elif i == deck['sevenWan']:
                    self.visibleTilesSpriteLocation.append(('sevenWan', (displayIndex, rowDisplayIndex)))
                    scrn.blit(sevenWan, (displayIndex, rowDisplayIndex))
                elif i == deck['eightWan']:
                    self.visibleTilesSpriteLocation.append(('eightWan', (displayIndex, rowDisplayIndex)))
                    scrn.blit(eightWan, (displayIndex, rowDisplayIndex))
                elif i == deck['nineWan']:
                    self.visibleTilesSpriteLocation.append(('nineWan', (displayIndex, rowDisplayIndex)))
                    scrn.blit(nineWan, (displayIndex, rowDisplayIndex))
                elif i == deck['oneTiao']:
                    self.visibleTilesSpriteLocation.append(('oneTiao', (displayIndex, rowDisplayIndex)))
                    scrn.blit(oneTiao, (displayIndex, rowDisplayIndex))
                elif i == deck['twoTiao']:
                    self.visibleTilesSpriteLocation.append(('twoTiao', (displayIndex, rowDisplayIndex)))
                    scrn.blit(twoTiao, (displayIndex, rowDisplayIndex))
                elif i == deck['threeTiao']:
                    self.visibleTilesSpriteLocation.append(('threeTiao', (displayIndex, rowDisplayIndex)))
                    scrn.blit(threeTiao, (displayIndex, rowDisplayIndex))
                elif i == deck['fourTiao']:
                    self.visibleTilesSpriteLocation.append(('fourTiao', (displayIndex, rowDisplayIndex)))
                    scrn.blit(fourTiao, (displayIndex, rowDisplayIndex))
                elif i == deck['fiveTiao']:
                    self.visibleTilesSpriteLocation.append(('fiveTiao', (displayIndex, rowDisplayIndex)))
                    scrn.blit(fiveTiao, (displayIndex, rowDisplayIndex))
                elif i == deck['sixTiao']:
                    self.visibleTilesSpriteLocation.append(('sixTiao', (displayIndex, rowDisplayIndex)))
                    scrn.blit(sixTiao, (displayIndex, rowDisplayIndex))
                elif i == deck['sevenTiao']:
                    self.visibleTilesSpriteLocation.append(('sevenTiao', (displayIndex, rowDisplayIndex)))
                    scrn.blit(sevenTiao, (displayIndex, rowDisplayIndex))
                elif i == deck['eightTiao']:
                    self.visibleTilesSpriteLocation.append(('eightTiao', (displayIndex, rowDisplayIndex)))
                    scrn.blit(eightTiao, (displayIndex, rowDisplayIndex))
                elif i == deck['nineTiao']:
                    self.visibleTilesSpriteLocation.append(('nineTiao', (displayIndex, rowDisplayIndex)))
                    scrn.blit(nineTiao, (displayIndex, rowDisplayIndex))
                displayIndex += 24

            pongKongRowDisplayIndex = rowDisplayIndex + 32
            pongKongDisplayIndex = startingCol
            for i in currentPlayer.pongdeck:
                if i == deck['east']:
                    scrn.blit(east, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['west']:
                    scrn.blit(west, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['north']:
                    scrn.blit(north, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['south']:
                    scrn.blit(south, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['center']:
                    scrn.blit(center, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['space']:
                    scrn.blit(space, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['fa']:
                    scrn.blit(fa, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['oneTong']:
                    scrn.blit(oneTong, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['twoTong']:
                    scrn.blit(twoTong, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['threeTong']:
                    scrn.blit(threeTong, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['fourTong']:
                    scrn.blit(fourTong, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['fiveTong']:
                    scrn.blit(fiveTong, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['sixTong']:
                    scrn.blit(sixTong, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['sevenTong']:
                    scrn.blit(sevenTong, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['eightTong']:
                    scrn.blit(eightTong, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['nineTong']:
                    scrn.blit(nineTong, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['oneWan']:
                    scrn.blit(oneWan, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['twoWan']:
                    scrn.blit(twoWan, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['threeWan']:
                    scrn.blit(threeWan, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['fourWan']:
                    scrn.blit(fourWan, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['fiveWan']:
                    scrn.blit(fiveWan, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['sixWan']:
                    scrn.blit(sixWan, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['sevenWan']:
                    scrn.blit(sevenWan, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['eightWan']:
                    scrn.blit(eightWan, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['nineWan']:
                    scrn.blit(nineWan, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['oneTiao']:
                    scrn.blit(oneTiao, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['twoTiao']:
                    scrn.blit(twoTiao, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['threeTiao']:
                    scrn.blit(threeTiao, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['fourTiao']:
                    scrn.blit(fourTiao, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['fiveTiao']:
                    scrn.blit(fiveTiao, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['sixTiao']:
                    scrn.blit(sixTiao, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['sevenTiao']:
                    scrn.blit(sevenTiao, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['eightTiao']:
                    scrn.blit(eightTiao, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['nineTiao']:
                    scrn.blit(nineTiao, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                pongKongDisplayIndex += 24
>>>>>>> 3aa8897abe7e9a6b29da2bf472dd99ac90beda11

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
<<<<<<< HEAD
=======
class Actor:
    def __init__(self, deck, playerNumber):
        self.decks = []
        self.playerNumber = playerNumber
        self.decks.extend(deck)
        self.decks.sort()
        self.pongdeck = []
        # self.display()

    def display(self):
        print('Player : ', self.playerNumber)
        self.displayDeck(self.decks)
        self.displayDeck(self.pongdeck)

    def displayDeck(self, decks):
        displayResult = ''
        for i in decks:
            if i == deck['east']:
                displayResult += '|东|'
            elif i == deck['west']:
                displayResult += '|西|'
            elif i == deck['north']:
                displayResult += '|北|'
            elif i == deck['south']:
                displayResult += '|南|'
            elif i == deck['center']:
                displayResult += '|中|'
            elif i == deck['fa']:
                displayResult += '|发|'
            elif i == deck['space']:
                displayResult += '|白|'
            elif i == deck['oneTong']:
                displayResult += '|一筒|'
            elif i == deck['twoTong']:
                displayResult += '|二筒|'
            elif i == deck['threeTong']:
                displayResult += '|三筒|'
            elif i == deck['fourTong']:
                displayResult += '|四筒|'
            elif i == deck['fiveTong']:
                displayResult += '|五筒|'
            elif i == deck['sixTong']:
                displayResult += '|六筒|'
            elif i == deck['sevenTong']:
                displayResult += '|七筒|'
            elif i == deck['eightTong']:
                displayResult += '|八筒|'
            elif i == deck['nineTong']:
                displayResult += '|九筒|'
            elif i == deck['oneWan']:
                displayResult += '|一万|'
            elif i == deck['twoWan']:
                displayResult += '|二万|'
            elif i == deck['threeWan']:
                displayResult += '|三万|'
            elif i == deck['fourWan']:
                displayResult += '|四万|'
            elif i == deck['fiveWan']:
                displayResult += '|五万|'
            elif i == deck['sixWan']:
                displayResult += '|六万|'
            elif i == deck['sevenWan']:
                displayResult += '|七万|'
            elif i == deck['eightWan']:
                displayResult += '|八万|'
            elif i == deck['nineWan']:
                displayResult += '|九万|'
            elif i == deck['oneTiao']:
                displayResult += '|一条|'
            elif i == deck['twoTiao']:
                displayResult += '|二条|'
            elif i == deck['threeTiao']:
                displayResult += '|三条|'
            elif i == deck['fourTiao']:
                displayResult += '|四条|'
            elif i == deck['fiveTiao']:
                displayResult += '|五条|'
            elif i == deck['sixTiao']:
                displayResult += '|六条|'
            elif i == deck['sevenTiao']:
                displayResult += '|七条|'
            elif i == deck['eightTiao']:
                displayResult += '|八条|'
            elif i == deck['nineTiao']:
                displayResult += '|九条|'
        print(displayResult)

    def removeDeck(self, deck):
        print(self.decks, deck)
        for i in self.decks:
            if i == deck:
                self.decks.remove(deck)
                return True
        return False

    def addDeck(self, deck):
        self.decks.append(deck)
        self.decks.sort()

    def canPong(self, newDeck):
        numberOfSimilar = 0
        for deck in self.decks:
            if deck == newDeck:
                numberOfSimilar += 1
                if numberOfSimilar == 2:
                    return True
        return False

    def canKong(self, newDeck):
        numberOfSimilar = 0
        for deck in self.decks:
            if deck == newDeck:
                numberOfSimilar += 1
                if numberOfSimilar == 3:
                    return True
        return False

    def pong(self, newDeck):
        if self.canPong(newDeck):
            self.decks.remove(newDeck)
            self.decks.remove(newDeck)
        self.pongdeck.append(newDeck)
        self.pongdeck.append(newDeck)
        self.pongdeck.append(newDeck)

    def kong(self, newDeck):
        if self.canPong(newDeck):
            self.decks.remove(newDeck)
            self.decks.remove(newDeck)
            self.decks.remove(newDeck)
        self.pongdeck.append(newDeck)
        self.pongdeck.append(newDeck)
        self.pongdeck.append(newDeck)
        self.pongdeck.append(newDeck)
>>>>>>> 3aa8897abe7e9a6b29da2bf472dd99ac90beda11

game = Board()