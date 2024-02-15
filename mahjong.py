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
startingRow = 300
startingCol = 130

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
        scrn.fill((0, 163, 108))

        # set the pygame window name
        pygame.display.set_caption('MahJong')

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
        # Using blit to copy content from one surface to other
        rowDisplayIndex = startingRow
        for player in range(len(self.players)):
            currentPlayer = self.players[player]
            displayIndex = startingCol
            for i in currentPlayer.decks:
                if i == deck['east']:
                    scrn.blit(east, (displayIndex, rowDisplayIndex))
                elif i == deck['west']:
                    scrn.blit(west, (displayIndex, rowDisplayIndex))
                elif i == deck['north']:
                    scrn.blit(north, (displayIndex, rowDisplayIndex))
                elif i == deck['south']:
                    scrn.blit(south, (displayIndex, rowDisplayIndex))
                elif i == deck['center']:
                    scrn.blit(center, (displayIndex, rowDisplayIndex))
                elif i == deck['space']:
                    scrn.blit(space, (displayIndex, rowDisplayIndex))
                elif i == deck['fa']:
                    scrn.blit(fa, (displayIndex, rowDisplayIndex))
                elif i == deck['oneCircle']:
                    scrn.blit(oneCircle, (displayIndex, rowDisplayIndex))
                elif i == deck['twoCircle']:
                    scrn.blit(twoCircle, (displayIndex, rowDisplayIndex))
                elif i == deck['threeCircle']:
                    scrn.blit(threeCircle, (displayIndex, rowDisplayIndex))
                elif i == deck['fourCircle']:
                    scrn.blit(fourCircle, (displayIndex, rowDisplayIndex))
                elif i == deck['fiveCircle']:
                    scrn.blit(fiveCircle, (displayIndex, rowDisplayIndex))
                elif i == deck['sixCircle']:
                    scrn.blit(sixCircle, (displayIndex, rowDisplayIndex))
                elif i == deck['sevenCircle']:
                    scrn.blit(sevenCircle, (displayIndex, rowDisplayIndex))
                elif i == deck['eightCircle']:
                    scrn.blit(eightCircle, (displayIndex, rowDisplayIndex))
                elif i == deck['nineCircle']:
                    scrn.blit(nineCircle, (displayIndex, rowDisplayIndex))
                elif i == deck['oneThousand']:
                    scrn.blit(oneThousand, (displayIndex, rowDisplayIndex))
                elif i == deck['twoThousand']:
                    scrn.blit(twoThousand, (displayIndex, rowDisplayIndex))
                elif i == deck['threeThousand']:
                    scrn.blit(threeThousand, (displayIndex, rowDisplayIndex))
                elif i == deck['fourThousand']:
                    scrn.blit(fourThousand, (displayIndex, rowDisplayIndex))
                elif i == deck['fiveThousand']:
                    scrn.blit(fiveThousand, (displayIndex, rowDisplayIndex))
                elif i == deck['sixThousand']:
                    scrn.blit(sixThousand, (displayIndex, rowDisplayIndex))
                elif i == deck['sevenThousand']:
                    scrn.blit(sevenThousand, (displayIndex, rowDisplayIndex))
                elif i == deck['eightThousand']:
                    scrn.blit(eightThousand, (displayIndex, rowDisplayIndex))
                elif i == deck['nineThousand']:
                    scrn.blit(nineThousand, (displayIndex, rowDisplayIndex))
                elif i == deck['oneStick']:
                    scrn.blit(oneStick, (displayIndex, rowDisplayIndex))
                elif i == deck['twoStick']:
                    scrn.blit(twoStick, (displayIndex, rowDisplayIndex))
                elif i == deck['threeStick']:
                    scrn.blit(threeStick, (displayIndex, rowDisplayIndex))
                elif i == deck['fourStick']:
                    scrn.blit(fourStick, (displayIndex, rowDisplayIndex))
                elif i == deck['fiveStick']:
                    scrn.blit(fiveStick, (displayIndex, rowDisplayIndex))
                elif i == deck['sixStick']:
                    scrn.blit(sixStick, (displayIndex, rowDisplayIndex))
                elif i == deck['sevenStick']:
                    scrn.blit(sevenStick, (displayIndex, rowDisplayIndex))
                elif i == deck['eightStick']:
                    scrn.blit(eightStick, (displayIndex, rowDisplayIndex))
                elif i == deck['nineStick']:
                    scrn.blit(nineStick, (displayIndex, rowDisplayIndex))
                displayIndex += 24
            rowDisplayIndex += 32

        # paint screen one time
        pygame.display.flip()
        status = True
        while (status):

            # iterate over the list of Event objects
            # that was returned by pygame.event.get() method.
            for i in pygame.event.get():

                # if event object type is QUIT
                # then quitting the pygame
                # and program both.
                if i.type == pygame.QUIT:
                    status = False

        # deactivates the pygame library
        pygame.quit()

class Actor:
    def __init__(self, deck, playerNumber):
        self.decks = []
        self.playerNumber = playerNumber
        self.decks.extend(deck)
        self.decks.sort()
        self.display()

    def display(self):
        print('Player : ', self.playerNumber)
        displayResult = ''
        for i in self.decks:
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

game = Board()