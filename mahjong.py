import random
import pygame
deck = {
    'east': 1,
    'west': 2,
    'north': 3,
    'south': 4,
    'space': 5,
    'fa': 6,
    'center': 7,
    'oneCircle': 8,
    'twoCircle': 9,
    'threeCircle': 10,
    'fourCircle': 11,
    'fiveCircle': 12,
    'sixCircle': 13,
    'sevenCircle': 14,
    'eightCircle': 15,
    'nineCircle': 16,
    'oneThousand': 17,
    'twoThousand': 18,
    'threeThousand': 19,
    'fourThousand': 20,
    'fiveThousand': 21,
    'sixThousand': 22,
    'sevenThousand': 23,
    'eightThousand': 24,
    'nineThousand': 25,
    'oneStick': 26,
    'twoStick': 27,
    'threeStick': 28,
    'fourStick': 29,
    'fiveStick': 30,
    'sixStick': 31,
    'sevenStick': 32,
    'eightStick': 33,
    'nineStick': 34,
}
deckChinese = {
    '东': 1,
    '西': 2,
    '北': 3,
    '南': 4,
    '白': 5,
    '发': 6,
    '中': 7,
    '一同': 8,
    '三同': 9,
    '三同': 10,
    '四同': 11,
    '五同': 12,
    '六同': 13,
    '七同': 14,
    '八同': 15,
    '九同': 16,
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

textRow = 100
textCol = 550

white = (255, 255, 255)


class Board:
    def __init__(self):
        self.tableCenter = []
        self.organizedDecks = [deck['east'], deck['east'], deck['east'], deck['east'],
                            deck['north'], deck['north'], deck['north'], deck['north'],
                            deck['west'], deck['west'], deck['west'], deck['west'],
                            deck['south'], deck['south'], deck['south'], deck['south'],
                            deck['center'], deck['center'], deck['center'], deck['center'],
                            deck['fa'], deck['fa'], deck['fa'], deck['fa'],
                            deck['space'], deck['space'], deck['space'], deck['space'],

                            deck['oneCircle'], deck['oneCircle'], deck['oneCircle'], deck['oneCircle'],
                            deck['twoCircle'], deck['twoCircle'], deck['twoCircle'], deck['twoCircle'],
                            deck['threeCircle'], deck['threeCircle'], deck['threeCircle'], deck['threeCircle'],
                            deck['fourCircle'], deck['fourCircle'], deck['fourCircle'], deck['fourCircle'],
                            deck['fiveCircle'], deck['fiveCircle'], deck['fiveCircle'], deck['fiveCircle'],
                            deck['sixCircle'], deck['sixCircle'], deck['sixCircle'], deck['sixCircle'],
                            deck['sevenCircle'], deck['sevenCircle'], deck['sevenCircle'], deck['sevenCircle'],
                            deck['eightCircle'], deck['eightCircle'], deck['eightCircle'], deck['eightCircle'],
                            deck['nineCircle'], deck['nineCircle'], deck['nineCircle'], deck['nineCircle'],

                            deck['oneStick'], deck['oneStick'], deck['oneStick'], deck['oneStick'],
                            deck['twoStick'], deck['twoStick'], deck['twoStick'], deck['twoStick'],
                            deck['threeStick'], deck['threeStick'], deck['threeStick'], deck['threeStick'],
                            deck['fourStick'], deck['fourStick'], deck['fourStick'], deck['fourStick'],
                            deck['fiveStick'], deck['fiveStick'], deck['fiveStick'], deck['fiveStick'],
                            deck['sixStick'], deck['sixStick'], deck['sixStick'], deck['sixStick'],
                            deck['sevenStick'], deck['sevenStick'], deck['sevenStick'], deck['sevenStick'],
                            deck['eightStick'], deck['eightStick'], deck['eightStick'], deck['eightStick'],
                            deck['nineStick'], deck['nineStick'], deck['nineStick'], deck['nineStick'],

                            deck['oneThousand'], deck['oneThousand'], deck['oneThousand'], deck['oneThousand'],
                            deck['twoThousand'], deck['twoThousand'], deck['twoThousand'], deck['twoThousand'],
                            deck['threeThousand'], deck['threeThousand'], deck['threeThousand'], deck['threeThousand'],
                            deck['fourThousand'], deck['fourThousand'], deck['fourThousand'], deck['fourThousand'],
                            deck['fiveThousand'], deck['fiveThousand'], deck['fiveThousand'], deck['fiveThousand'],
                            deck['sixThousand'], deck['sixThousand'], deck['sixThousand'], deck['sixThousand'],
                            deck['sevenThousand'], deck['sevenThousand'], deck['sevenThousand'], deck['sevenThousand'],
                            deck['eightThousand'], deck['eightThousand'], deck['eightThousand'], deck['eightThousand'],
                            deck['nineThousand'], deck['nineThousand'], deck['nineThousand'], deck['nineThousand'],
                            ]
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
        center = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\center.png").convert_alpha()
        east = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\east.png").convert_alpha()
        west = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\west.png").convert_alpha()
        south = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\south.png").convert_alpha()
        north = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\north.png").convert_alpha()
        fa = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\fa.png").convert_alpha()
        space = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\space.png").convert_alpha()
        oneCircle = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\oneCircle.png").convert_alpha()
        twoCircle = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\twoCircle.png").convert_alpha()
        threeCircle = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\threeCircle.png").convert_alpha()
        fourCircle = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\fourCircle.png").convert_alpha()
        fiveCircle = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\fiveCircle.png").convert_alpha()
        sixCircle = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\sixCircle.png").convert_alpha()
        sevenCircle = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\sevenCircle.png").convert_alpha()
        eightCircle = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\eightCircle.png").convert_alpha()
        nineCircle = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\nineCircle.png").convert_alpha()

        oneThousand = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\oneThousand.png").convert_alpha()
        twoThousand= pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\twoThousand.png").convert_alpha()
        threeThousand= pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\threeThousand.png").convert_alpha()
        fourThousand = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\fourThousand.png").convert_alpha()
        fiveThousand = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\fiveThousand.png").convert_alpha()
        sixThousand = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\sixThousand.png").convert_alpha()
        sevenThousand = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\sevenThousand.png").convert_alpha()
        eightThousand = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\eightThousand.png").convert_alpha()
        nineThousand = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\nineThousand.png").convert_alpha()

        oneStick = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\oneStick.png").convert_alpha()
        twoStick = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\twoStick.png").convert_alpha()
        threeStick= pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\threeStick.png").convert_alpha()
        fourStick = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\fourStick.png").convert_alpha()
        fiveStick = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\fiveStick.png").convert_alpha()
        sixStick = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\sixStick.png").convert_alpha()
        sevenStick = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\sevenStick.png").convert_alpha()
        eightStick = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\eightStick.png").convert_alpha()
        nineStick = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\nineStick.png").convert_alpha()


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
                    elif i == deck['oneCircle']:
                        scrn.blit(oneCircle, (displayIndex, tableRowIndex))
                    elif i == deck['twoCircle']:
                        scrn.blit(twoCircle, (displayIndex, tableRowIndex))
                    elif i == deck['threeCircle']:
                        scrn.blit(threeCircle, (displayIndex, tableRowIndex))
                    elif i == deck['fourCircle']:
                        scrn.blit(fourCircle, (displayIndex, tableRowIndex))
                    elif i == deck['fiveCircle']:
                        scrn.blit(fiveCircle, (displayIndex, tableRowIndex))
                    elif i == deck['sixCircle']:
                        scrn.blit(sixCircle, (displayIndex, tableRowIndex))
                    elif i == deck['sevenCircle']:
                        scrn.blit(sevenCircle, (displayIndex, tableRowIndex))
                    elif i == deck['eightCircle']:
                        scrn.blit(eightCircle, (displayIndex, tableRowIndex))
                    elif i == deck['nineCircle']:
                        scrn.blit(nineCircle, (displayIndex, tableRowIndex))
                    elif i == deck['oneThousand']:
                        scrn.blit(oneThousand, (displayIndex, tableRowIndex))
                    elif i == deck['twoThousand']:
                        scrn.blit(twoThousand, (displayIndex, tableRowIndex))
                    elif i == deck['threeThousand']:
                        scrn.blit(threeThousand, (displayIndex, tableRowIndex))
                    elif i == deck['fourThousand']:
                        scrn.blit(fourThousand, (displayIndex, tableRowIndex))
                    elif i == deck['fiveThousand']:
                        scrn.blit(fiveThousand, (displayIndex, tableRowIndex))
                    elif i == deck['sixThousand']:
                        scrn.blit(sixThousand, (displayIndex, tableRowIndex))
                    elif i == deck['sevenThousand']:
                        scrn.blit(sevenThousand, (displayIndex, tableRowIndex))
                    elif i == deck['eightThousand']:
                        scrn.blit(eightThousand, (displayIndex, tableRowIndex))
                    elif i == deck['nineThousand']:
                        scrn.blit(nineThousand, (displayIndex, tableRowIndex))
                    elif i == deck['oneStick']:
                        scrn.blit(oneStick, (displayIndex, tableRowIndex))
                    elif i == deck['twoStick']:
                        scrn.blit(twoStick, (displayIndex, tableRowIndex))
                    elif i == deck['threeStick']:
                        scrn.blit(threeStick, (displayIndex, tableRowIndex))
                    elif i == deck['fourStick']:
                        scrn.blit(fourStick, (displayIndex, tableRowIndex))
                    elif i == deck['fiveStick']:
                        scrn.blit(fiveStick, (displayIndex, tableRowIndex))
                    elif i == deck['sixStick']:
                        scrn.blit(sixStick, (displayIndex, tableRowIndex))
                    elif i == deck['sevenStick']:
                        scrn.blit(sevenStick, (displayIndex, tableRowIndex))
                    elif i == deck['eightStick']:
                        scrn.blit(eightStick, (displayIndex, tableRowIndex))
                    elif i == deck['nineStick']:
                        scrn.blit(nineStick, (displayIndex, tableRowIndex))
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
                elif i == deck['oneCircle']:
                    self.visibleTilesSpriteLocation.append(('oneCircle', (displayIndex, rowDisplayIndex)))
                    scrn.blit(oneCircle, (displayIndex, rowDisplayIndex))
                elif i == deck['twoCircle']:
                    self.visibleTilesSpriteLocation.append(('twoCircle', (displayIndex, rowDisplayIndex)))
                    scrn.blit(twoCircle, (displayIndex, rowDisplayIndex))
                elif i == deck['threeCircle']:
                    self.visibleTilesSpriteLocation.append(('threeCircle', (displayIndex, rowDisplayIndex)))
                    scrn.blit(threeCircle, (displayIndex, rowDisplayIndex))
                elif i == deck['fourCircle']:
                    self.visibleTilesSpriteLocation.append(('fourCircle', (displayIndex, rowDisplayIndex)))
                    scrn.blit(fourCircle, (displayIndex, rowDisplayIndex))
                elif i == deck['fiveCircle']:
                    self.visibleTilesSpriteLocation.append(('fiveCircle', (displayIndex, rowDisplayIndex)))
                    scrn.blit(fiveCircle, (displayIndex, rowDisplayIndex))
                elif i == deck['sixCircle']:
                    self.visibleTilesSpriteLocation.append(('sixCircle', (displayIndex, rowDisplayIndex)))
                    scrn.blit(sixCircle, (displayIndex, rowDisplayIndex))
                elif i == deck['sevenCircle']:
                    self.visibleTilesSpriteLocation.append(('sevenCircle', (displayIndex, rowDisplayIndex)))
                    scrn.blit(sevenCircle, (displayIndex, rowDisplayIndex))
                elif i == deck['eightCircle']:
                    self.visibleTilesSpriteLocation.append(('eightCircle', (displayIndex, rowDisplayIndex)))
                    scrn.blit(eightCircle, (displayIndex, rowDisplayIndex))
                elif i == deck['nineCircle']:
                    self.visibleTilesSpriteLocation.append(('nineCircle', (displayIndex, rowDisplayIndex)))
                    scrn.blit(nineCircle, (displayIndex, rowDisplayIndex))
                elif i == deck['oneThousand']:
                    self.visibleTilesSpriteLocation.append(('oneThousand', (displayIndex, rowDisplayIndex)))
                    scrn.blit(oneThousand, (displayIndex, rowDisplayIndex))
                elif i == deck['twoThousand']:
                    self.visibleTilesSpriteLocation.append(('twoThousand', (displayIndex, rowDisplayIndex)))
                    scrn.blit(twoThousand, (displayIndex, rowDisplayIndex))
                elif i == deck['threeThousand']:
                    self.visibleTilesSpriteLocation.append(('threeThousand', (displayIndex, rowDisplayIndex)))
                    scrn.blit(threeThousand, (displayIndex, rowDisplayIndex))
                elif i == deck['fourThousand']:
                    self.visibleTilesSpriteLocation.append(('fourThousand', (displayIndex, rowDisplayIndex)))
                    scrn.blit(fourThousand, (displayIndex, rowDisplayIndex))
                elif i == deck['fiveThousand']:
                    self.visibleTilesSpriteLocation.append(('fiveThousand', (displayIndex, rowDisplayIndex)))
                    scrn.blit(fiveThousand, (displayIndex, rowDisplayIndex))
                elif i == deck['sixThousand']:
                    self.visibleTilesSpriteLocation.append(('sixThousand', (displayIndex, rowDisplayIndex)))
                    scrn.blit(sixThousand, (displayIndex, rowDisplayIndex))
                elif i == deck['sevenThousand']:
                    self.visibleTilesSpriteLocation.append(('sevenThousand', (displayIndex, rowDisplayIndex)))
                    scrn.blit(sevenThousand, (displayIndex, rowDisplayIndex))
                elif i == deck['eightThousand']:
                    self.visibleTilesSpriteLocation.append(('eightThousand', (displayIndex, rowDisplayIndex)))
                    scrn.blit(eightThousand, (displayIndex, rowDisplayIndex))
                elif i == deck['nineThousand']:
                    self.visibleTilesSpriteLocation.append(('nineThousand', (displayIndex, rowDisplayIndex)))
                    scrn.blit(nineThousand, (displayIndex, rowDisplayIndex))
                elif i == deck['oneStick']:
                    self.visibleTilesSpriteLocation.append(('oneStick', (displayIndex, rowDisplayIndex)))
                    scrn.blit(oneStick, (displayIndex, rowDisplayIndex))
                elif i == deck['twoStick']:
                    self.visibleTilesSpriteLocation.append(('twoStick', (displayIndex, rowDisplayIndex)))
                    scrn.blit(twoStick, (displayIndex, rowDisplayIndex))
                elif i == deck['threeStick']:
                    self.visibleTilesSpriteLocation.append(('threeStick', (displayIndex, rowDisplayIndex)))
                    scrn.blit(threeStick, (displayIndex, rowDisplayIndex))
                elif i == deck['fourStick']:
                    self.visibleTilesSpriteLocation.append(('fourStick', (displayIndex, rowDisplayIndex)))
                    scrn.blit(fourStick, (displayIndex, rowDisplayIndex))
                elif i == deck['fiveStick']:
                    self.visibleTilesSpriteLocation.append(('fiveStick', (displayIndex, rowDisplayIndex)))
                    scrn.blit(fiveStick, (displayIndex, rowDisplayIndex))
                elif i == deck['sixStick']:
                    self.visibleTilesSpriteLocation.append(('sixStick', (displayIndex, rowDisplayIndex)))
                    scrn.blit(sixStick, (displayIndex, rowDisplayIndex))
                elif i == deck['sevenStick']:
                    self.visibleTilesSpriteLocation.append(('sevenStick', (displayIndex, rowDisplayIndex)))
                    scrn.blit(sevenStick, (displayIndex, rowDisplayIndex))
                elif i == deck['eightStick']:
                    self.visibleTilesSpriteLocation.append(('eightStick', (displayIndex, rowDisplayIndex)))
                    scrn.blit(eightStick, (displayIndex, rowDisplayIndex))
                elif i == deck['nineStick']:
                    self.visibleTilesSpriteLocation.append(('nineStick', (displayIndex, rowDisplayIndex)))
                    scrn.blit(nineStick, (displayIndex, rowDisplayIndex))
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
                elif i == deck['oneCircle']:
                    scrn.blit(oneCircle, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['twoCircle']:
                    scrn.blit(twoCircle, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['threeCircle']:
                    scrn.blit(threeCircle, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['fourCircle']:
                    scrn.blit(fourCircle, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['fiveCircle']:
                    scrn.blit(fiveCircle, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['sixCircle']:
                    scrn.blit(sixCircle, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['sevenCircle']:
                    scrn.blit(sevenCircle, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['eightCircle']:
                    scrn.blit(eightCircle, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['nineCircle']:
                    scrn.blit(nineCircle, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['oneThousand']:
                    scrn.blit(oneThousand, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['twoThousand']:
                    scrn.blit(twoThousand, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['threeThousand']:
                    scrn.blit(threeThousand, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['fourThousand']:
                    scrn.blit(fourThousand, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['fiveThousand']:
                    scrn.blit(fiveThousand, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['sixThousand']:
                    scrn.blit(sixThousand, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['sevenThousand']:
                    scrn.blit(sevenThousand, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['eightThousand']:
                    scrn.blit(eightThousand, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['nineThousand']:
                    scrn.blit(nineThousand, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['oneStick']:
                    scrn.blit(oneStick, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['twoStick']:
                    scrn.blit(twoStick, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['threeStick']:
                    scrn.blit(threeStick, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['fourStick']:
                    scrn.blit(fourStick, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['fiveStick']:
                    scrn.blit(fiveStick, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['sixStick']:
                    scrn.blit(sixStick, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['sevenStick']:
                    scrn.blit(sevenStick, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['eightStick']:
                    scrn.blit(eightStick, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['nineStick']:
                    scrn.blit(nineStick, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                pongKongDisplayIndex += 24


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
        return deckChinese[deckName]

    def mapDeckEnglish(self, deckName):
        return deck[deckName]

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
            elif i == deck['oneCircle']:
                displayResult += '|一同|'
            elif i == deck['twoCircle']:
                displayResult += '|二同|'
            elif i == deck['threeCircle']:
                displayResult += '|三同|'
            elif i == deck['fourCircle']:
                displayResult += '|四同|'
            elif i == deck['fiveCircle']:
                displayResult += '|五同|'
            elif i == deck['sixCircle']:
                displayResult += '|六同|'
            elif i == deck['sevenCircle']:
                displayResult += '|七同|'
            elif i == deck['eightCircle']:
                displayResult += '|八同|'
            elif i == deck['nineCircle']:
                displayResult += '|九同|'
            elif i == deck['oneThousand']:
                displayResult += '|一万|'
            elif i == deck['twoThousand']:
                displayResult += '|二万|'
            elif i == deck['threeThousand']:
                displayResult += '|三万|'
            elif i == deck['fourThousand']:
                displayResult += '|四万|'
            elif i == deck['fiveThousand']:
                displayResult += '|五万|'
            elif i == deck['sixThousand']:
                displayResult += '|六万|'
            elif i == deck['sevenThousand']:
                displayResult += '|七万|'
            elif i == deck['eightThousand']:
                displayResult += '|八万|'
            elif i == deck['nineThousand']:
                displayResult += '|九万|'
            elif i == deck['oneStick']:
                displayResult += '|一条|'
            elif i == deck['twoStick']:
                displayResult += '|二条|'
            elif i == deck['threeStick']:
                displayResult += '|三条|'
            elif i == deck['fourStick']:
                displayResult += '|四条|'
            elif i == deck['fiveStick']:
                displayResult += '|五条|'
            elif i == deck['sixStick']:
                displayResult += '|六条|'
            elif i == deck['sevenStick']:
                displayResult += '|七条|'
            elif i == deck['eightStick']:
                displayResult += '|八条|'
            elif i == deck['nineStick']:
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

game = Board()