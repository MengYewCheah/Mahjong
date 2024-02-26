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
    'onetong': 8,
    'twotong': 9,
    'threetong': 10,
    'fourtong': 11,
    'fivetong': 12,
    'sixtong': 13,
    'seventong': 14,
    'eighttong': 15,
    'ninetong': 16,
    'onewan': 17,
    'twowan': 18,
    'threewan': 19,
    'fourwan': 20,
    'fivewan': 21,
    'sixwan': 22,
    'sevenwan': 23,
    'eightwan': 24,
    'ninewan': 25,
    'onetiao': 26,
    'twotiao': 27,
    'threetiao': 28,
    'fourtiao': 29,
    'fivetiao': 30,
    'sixtiao': 31,
    'seventiao': 32,
    'eighttiao': 33,
    'ninetiao': 34,
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

                            deck['onetong'], deck['onetong'], deck['onetong'], deck['onetong'],
                            deck['twotong'], deck['twotong'], deck['twotong'], deck['twotong'],
                            deck['threetong'], deck['threetong'], deck['threetong'], deck['threetong'],
                            deck['fourtong'], deck['fourtong'], deck['fourtong'], deck['fourtong'],
                            deck['fivetong'], deck['fivetong'], deck['fivetong'], deck['fivetong'],
                            deck['sixtong'], deck['sixtong'], deck['sixtong'], deck['sixtong'],
                            deck['seventong'], deck['seventong'], deck['seventong'], deck['seventong'],
                            deck['eighttong'], deck['eighttong'], deck['eighttong'], deck['eighttong'],
                            deck['ninetong'], deck['ninetong'], deck['ninetong'], deck['ninetong'],

                            deck['onetiao'], deck['onetiao'], deck['onetiao'], deck['onetiao'],
                            deck['twotiao'], deck['twotiao'], deck['twotiao'], deck['twotiao'],
                            deck['threetiao'], deck['threetiao'], deck['threetiao'], deck['threetiao'],
                            deck['fourtiao'], deck['fourtiao'], deck['fourtiao'], deck['fourtiao'],
                            deck['fivetiao'], deck['fivetiao'], deck['fivetiao'], deck['fivetiao'],
                            deck['sixtiao'], deck['sixtiao'], deck['sixtiao'], deck['sixtiao'],
                            deck['seventiao'], deck['seventiao'], deck['seventiao'], deck['seventiao'],
                            deck['eighttiao'], deck['eighttiao'], deck['eighttiao'], deck['eighttiao'],
                            deck['ninetiao'], deck['ninetiao'], deck['ninetiao'], deck['ninetiao'],

                            deck['onewan'], deck['onewan'], deck['onewan'], deck['onewan'],
                            deck['twowan'], deck['twowan'], deck['twowan'], deck['twowan'],
                            deck['threewan'], deck['threewan'], deck['threewan'], deck['threewan'],
                            deck['fourwan'], deck['fourwan'], deck['fourwan'], deck['fourwan'],
                            deck['fivewan'], deck['fivewan'], deck['fivewan'], deck['fivewan'],
                            deck['sixwan'], deck['sixwan'], deck['sixwan'], deck['sixwan'],
                            deck['sevenwan'], deck['sevenwan'], deck['sevenwan'], deck['sevenwan'],
                            deck['eightwan'], deck['eightwan'], deck['eightwan'], deck['eightwan'],
                            deck['ninewan'], deck['ninewan'], deck['ninewan'], deck['ninewan'],
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
        center = pygame.image.load(".\\mahjong tiles\\center.png").convert_alpha()
        east = pygame.image.load(".\\mahjong tiles\\east.png").convert_alpha()
        west = pygame.image.load(".\\mahjong tiles\\west.png").convert_alpha()
        south = pygame.image.load(".\\mahjong tiles\\south.png").convert_alpha()
        north = pygame.image.load(".\\mahjong tiles\\north.png").convert_alpha()
        fa = pygame.image.load(".\\mahjong tiles\\fa.png").convert_alpha()
        space = pygame.image.load(".\\mahjong tiles\\space.png").convert_alpha()
        onetong = pygame.image.load(".\\mahjong tiles\\onetong.png").convert_alpha()
        twotong = pygame.image.load(".\\mahjong tiles\\twotong.png").convert_alpha()
        threetong = pygame.image.load(".\\mahjong tiles\\threetong.png").convert_alpha()
        fourtong = pygame.image.load(".\\mahjong tiles\\fourtong.png").convert_alpha()
        fivetong = pygame.image.load(".\\mahjong tiles\\fivetong.png").convert_alpha()
        sixtong = pygame.image.load(".\\mahjong tiles\\sixtong.png").convert_alpha()
        seventong = pygame.image.load(".\\mahjong tiles\\seventong.png").convert_alpha()
        eighttong = pygame.image.load(".\\mahjong tiles\\eighttong.png").convert_alpha()
        ninetong = pygame.image.load(".\\mahjong tiles\\ninetong.png").convert_alpha()

        onewan = pygame.image.load(".\\mahjong tiles\\onewan.png").convert_alpha()
        twowan= pygame.image.load(".\\mahjong tiles\\twowan.png").convert_alpha()
        threewan= pygame.image.load(".\\mahjong tiles\\threewan.png").convert_alpha()
        fourwan = pygame.image.load(".\\mahjong tiles\\fourwan.png").convert_alpha()
        fivewan = pygame.image.load(".\\mahjong tiles\\fivewan.png").convert_alpha()
        sixwan = pygame.image.load(".\\mahjong tiles\\sixwan.png").convert_alpha()
        sevenwan = pygame.image.load(".\\mahjong tiles\\sevenwan.png").convert_alpha()
        eightwan = pygame.image.load(".\\mahjong tiles\\eightwan.png").convert_alpha()
        ninewan = pygame.image.load(".\\mahjong tiles\\ninewan.png").convert_alpha()

        onetiao = pygame.image.load(".\\mahjong tiles\\onetiao.png").convert_alpha()
        twotiao = pygame.image.load(".\\mahjong tiles\\twotiao.png").convert_alpha()
        threetiao= pygame.image.load(".\\mahjong tiles\\threetiao.png").convert_alpha()
        fourtiao = pygame.image.load(".\\mahjong tiles\\fourtiao.png").convert_alpha()
        fivetiao = pygame.image.load(".\\mahjong tiles\\fivetiao.png").convert_alpha()
        sixtiao = pygame.image.load(".\\mahjong tiles\\sixtiao.png").convert_alpha()
        seventiao = pygame.image.load(".\\mahjong tiles\\seventiao.png").convert_alpha()
        eighttiao = pygame.image.load(".\\mahjong tiles\\eighttiao.png").convert_alpha()
        ninetiao = pygame.image.load(".\\mahjong tiles\\ninetiao.png").convert_alpha()


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
                    elif i == deck['onetong']:
                        scrn.blit(onetong, (displayIndex, tableRowIndex))
                    elif i == deck['twotong']:
                        scrn.blit(twotong, (displayIndex, tableRowIndex))
                    elif i == deck['threetong']:
                        scrn.blit(threetong, (displayIndex, tableRowIndex))
                    elif i == deck['fourtong']:
                        scrn.blit(fourtong, (displayIndex, tableRowIndex))
                    elif i == deck['fivetong']:
                        scrn.blit(fivetong, (displayIndex, tableRowIndex))
                    elif i == deck['sixtong']:
                        scrn.blit(sixtong, (displayIndex, tableRowIndex))
                    elif i == deck['seventong']:
                        scrn.blit(seventong, (displayIndex, tableRowIndex))
                    elif i == deck['eighttong']:
                        scrn.blit(eighttong, (displayIndex, tableRowIndex))
                    elif i == deck['ninetong']:
                        scrn.blit(ninetong, (displayIndex, tableRowIndex))
                    elif i == deck['onewan']:
                        scrn.blit(onewan, (displayIndex, tableRowIndex))
                    elif i == deck['twowan']:
                        scrn.blit(twowan, (displayIndex, tableRowIndex))
                    elif i == deck['threewan']:
                        scrn.blit(threewan, (displayIndex, tableRowIndex))
                    elif i == deck['fourwan']:
                        scrn.blit(fourwan, (displayIndex, tableRowIndex))
                    elif i == deck['fivewan']:
                        scrn.blit(fivewan, (displayIndex, tableRowIndex))
                    elif i == deck['sixwan']:
                        scrn.blit(sixwan, (displayIndex, tableRowIndex))
                    elif i == deck['sevenwan']:
                        scrn.blit(sevenwan, (displayIndex, tableRowIndex))
                    elif i == deck['eightwan']:
                        scrn.blit(eightwan, (displayIndex, tableRowIndex))
                    elif i == deck['ninewan']:
                        scrn.blit(ninewan, (displayIndex, tableRowIndex))
                    elif i == deck['onetiao']:
                        scrn.blit(onetiao, (displayIndex, tableRowIndex))
                    elif i == deck['twotiao']:
                        scrn.blit(twotiao, (displayIndex, tableRowIndex))
                    elif i == deck['threetiao']:
                        scrn.blit(threetiao, (displayIndex, tableRowIndex))
                    elif i == deck['fourtiao']:
                        scrn.blit(fourtiao, (displayIndex, tableRowIndex))
                    elif i == deck['fivetiao']:
                        scrn.blit(fivetiao, (displayIndex, tableRowIndex))
                    elif i == deck['sixtiao']:
                        scrn.blit(sixtiao, (displayIndex, tableRowIndex))
                    elif i == deck['seventiao']:
                        scrn.blit(seventiao, (displayIndex, tableRowIndex))
                    elif i == deck['eighttiao']:
                        scrn.blit(eighttiao, (displayIndex, tableRowIndex))
                    elif i == deck['ninetiao']:
                        scrn.blit(ninetiao, (displayIndex, tableRowIndex))
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
                elif i == deck['onetong']:
                    self.visibleTilesSpriteLocation.append(('onetong', (displayIndex, rowDisplayIndex)))
                    scrn.blit(onetong, (displayIndex, rowDisplayIndex))
                elif i == deck['twotong']:
                    self.visibleTilesSpriteLocation.append(('twotong', (displayIndex, rowDisplayIndex)))
                    scrn.blit(twotong, (displayIndex, rowDisplayIndex))
                elif i == deck['threetong']:
                    self.visibleTilesSpriteLocation.append(('threetong', (displayIndex, rowDisplayIndex)))
                    scrn.blit(threetong, (displayIndex, rowDisplayIndex))
                elif i == deck['fourtong']:
                    self.visibleTilesSpriteLocation.append(('fourtong', (displayIndex, rowDisplayIndex)))
                    scrn.blit(fourtong, (displayIndex, rowDisplayIndex))
                elif i == deck['fivetong']:
                    self.visibleTilesSpriteLocation.append(('fivetong', (displayIndex, rowDisplayIndex)))
                    scrn.blit(fivetong, (displayIndex, rowDisplayIndex))
                elif i == deck['sixtong']:
                    self.visibleTilesSpriteLocation.append(('sixtong', (displayIndex, rowDisplayIndex)))
                    scrn.blit(sixtong, (displayIndex, rowDisplayIndex))
                elif i == deck['seventong']:
                    self.visibleTilesSpriteLocation.append(('seventong', (displayIndex, rowDisplayIndex)))
                    scrn.blit(seventong, (displayIndex, rowDisplayIndex))
                elif i == deck['eighttong']:
                    self.visibleTilesSpriteLocation.append(('eighttong', (displayIndex, rowDisplayIndex)))
                    scrn.blit(eighttong, (displayIndex, rowDisplayIndex))
                elif i == deck['ninetong']:
                    self.visibleTilesSpriteLocation.append(('ninetong', (displayIndex, rowDisplayIndex)))
                    scrn.blit(ninetong, (displayIndex, rowDisplayIndex))
                elif i == deck['onewan']:
                    self.visibleTilesSpriteLocation.append(('onewan', (displayIndex, rowDisplayIndex)))
                    scrn.blit(onewan, (displayIndex, rowDisplayIndex))
                elif i == deck['twowan']:
                    self.visibleTilesSpriteLocation.append(('twowan', (displayIndex, rowDisplayIndex)))
                    scrn.blit(twowan, (displayIndex, rowDisplayIndex))
                elif i == deck['threewan']:
                    self.visibleTilesSpriteLocation.append(('threewan', (displayIndex, rowDisplayIndex)))
                    scrn.blit(threewan, (displayIndex, rowDisplayIndex))
                elif i == deck['fourwan']:
                    self.visibleTilesSpriteLocation.append(('fourwan', (displayIndex, rowDisplayIndex)))
                    scrn.blit(fourwan, (displayIndex, rowDisplayIndex))
                elif i == deck['fivewan']:
                    self.visibleTilesSpriteLocation.append(('fivewan', (displayIndex, rowDisplayIndex)))
                    scrn.blit(fivewan, (displayIndex, rowDisplayIndex))
                elif i == deck['sixwan']:
                    self.visibleTilesSpriteLocation.append(('sixwan', (displayIndex, rowDisplayIndex)))
                    scrn.blit(sixwan, (displayIndex, rowDisplayIndex))
                elif i == deck['sevenwan']:
                    self.visibleTilesSpriteLocation.append(('sevenwan', (displayIndex, rowDisplayIndex)))
                    scrn.blit(sevenwan, (displayIndex, rowDisplayIndex))
                elif i == deck['eightwan']:
                    self.visibleTilesSpriteLocation.append(('eightwan', (displayIndex, rowDisplayIndex)))
                    scrn.blit(eightwan, (displayIndex, rowDisplayIndex))
                elif i == deck['ninewan']:
                    self.visibleTilesSpriteLocation.append(('ninewan', (displayIndex, rowDisplayIndex)))
                    scrn.blit(ninewan, (displayIndex, rowDisplayIndex))
                elif i == deck['onetiao']:
                    self.visibleTilesSpriteLocation.append(('onetiao', (displayIndex, rowDisplayIndex)))
                    scrn.blit(onetiao, (displayIndex, rowDisplayIndex))
                elif i == deck['twotiao']:
                    self.visibleTilesSpriteLocation.append(('twotiao', (displayIndex, rowDisplayIndex)))
                    scrn.blit(twotiao, (displayIndex, rowDisplayIndex))
                elif i == deck['threetiao']:
                    self.visibleTilesSpriteLocation.append(('threetiao', (displayIndex, rowDisplayIndex)))
                    scrn.blit(threetiao, (displayIndex, rowDisplayIndex))
                elif i == deck['fourtiao']:
                    self.visibleTilesSpriteLocation.append(('fourtiao', (displayIndex, rowDisplayIndex)))
                    scrn.blit(fourtiao, (displayIndex, rowDisplayIndex))
                elif i == deck['fivetiao']:
                    self.visibleTilesSpriteLocation.append(('fivetiao', (displayIndex, rowDisplayIndex)))
                    scrn.blit(fivetiao, (displayIndex, rowDisplayIndex))
                elif i == deck['sixtiao']:
                    self.visibleTilesSpriteLocation.append(('sixtiao', (displayIndex, rowDisplayIndex)))
                    scrn.blit(sixtiao, (displayIndex, rowDisplayIndex))
                elif i == deck['seventiao']:
                    self.visibleTilesSpriteLocation.append(('seventiao', (displayIndex, rowDisplayIndex)))
                    scrn.blit(seventiao, (displayIndex, rowDisplayIndex))
                elif i == deck['eighttiao']:
                    self.visibleTilesSpriteLocation.append(('eighttiao', (displayIndex, rowDisplayIndex)))
                    scrn.blit(eighttiao, (displayIndex, rowDisplayIndex))
                elif i == deck['ninetiao']:
                    self.visibleTilesSpriteLocation.append(('ninetiao', (displayIndex, rowDisplayIndex)))
                    scrn.blit(ninetiao, (displayIndex, rowDisplayIndex))
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
                elif i == deck['onetong']:
                    scrn.blit(onetong, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['twotong']:
                    scrn.blit(twotong, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['threetong']:
                    scrn.blit(threetong, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['fourtong']:
                    scrn.blit(fourtong, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['fivetong']:
                    scrn.blit(fivetong, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['sixtong']:
                    scrn.blit(sixtong, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['seventong']:
                    scrn.blit(seventong, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['eighttong']:
                    scrn.blit(eighttong, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['ninetong']:
                    scrn.blit(ninetong, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['onewan']:
                    scrn.blit(onewan, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['twowan']:
                    scrn.blit(twowan, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['threewan']:
                    scrn.blit(threewan, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['fourwan']:
                    scrn.blit(fourwan, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['fivewan']:
                    scrn.blit(fivewan, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['sixwan']:
                    scrn.blit(sixwan, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['sevenwan']:
                    scrn.blit(sevenwan, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['eightwan']:
                    scrn.blit(eightwan, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['ninewan']:
                    scrn.blit(ninewan, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['onetiao']:
                    scrn.blit(onetiao, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['twotiao']:
                    scrn.blit(twotiao, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['threetiao']:
                    scrn.blit(threetiao, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['fourtiao']:
                    scrn.blit(fourtiao, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['fivetiao']:
                    scrn.blit(fivetiao, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['sixtiao']:
                    scrn.blit(sixtiao, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['seventiao']:
                    scrn.blit(seventiao, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['eighttiao']:
                    scrn.blit(eighttiao, (pongKongDisplayIndex, pongKongRowDisplayIndex))
                elif i == deck['ninetiao']:
                    scrn.blit(ninetiao, (pongKongDisplayIndex, pongKongRowDisplayIndex))
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
            elif i == deck['onetong']:
                displayResult += '|一筒|'
            elif i == deck['twotong']:
                displayResult += '|二筒|'
            elif i == deck['threetong']:
                displayResult += '|三筒|'
            elif i == deck['fourtong']:
                displayResult += '|四筒|'
            elif i == deck['fivetong']:
                displayResult += '|五筒|'
            elif i == deck['sixtong']:
                displayResult += '|六筒|'
            elif i == deck['seventong']:
                displayResult += '|七筒|'
            elif i == deck['eighttong']:
                displayResult += '|八筒|'
            elif i == deck['ninetong']:
                displayResult += '|九筒|'
            elif i == deck['onewan']:
                displayResult += '|一万|'
            elif i == deck['twowan']:
                displayResult += '|二万|'
            elif i == deck['threewan']:
                displayResult += '|三万|'
            elif i == deck['fourwan']:
                displayResult += '|四万|'
            elif i == deck['fivewan']:
                displayResult += '|五万|'
            elif i == deck['sixwan']:
                displayResult += '|六万|'
            elif i == deck['sevenwan']:
                displayResult += '|七万|'
            elif i == deck['eightwan']:
                displayResult += '|八万|'
            elif i == deck['ninewan']:
                displayResult += '|九万|'
            elif i == deck['onetiao']:
                displayResult += '|一条|'
            elif i == deck['twotiao']:
                displayResult += '|二条|'
            elif i == deck['threetiao']:
                displayResult += '|三条|'
            elif i == deck['fourtiao']:
                displayResult += '|四条|'
            elif i == deck['fivetiao']:
                displayResult += '|五条|'
            elif i == deck['sixtiao']:
                displayResult += '|六条|'
            elif i == deck['seventiao']:
                displayResult += '|七条|'
            elif i == deck['eighttiao']:
                displayResult += '|八条|'
            elif i == deck['ninetiao']:
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