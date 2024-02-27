from Data import DeckData
Data = DeckData()
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
            if i == Data.deck['east']:
                displayResult += '|东|'
            elif i == Data.deck['west']:
                displayResult += '|西|'
            elif i == Data.deck['north']:
                displayResult += '|北|'
            elif i == Data.deck['south']:
                displayResult += '|南|'
            elif i == Data.deck['center']:
                displayResult += '|中|'
            elif i == Data.deck['fa']:
                displayResult += '|发|'
            elif i == Data.deck['space']:
                displayResult += '|白|'
            elif i == Data.deck['oneCircle']:
                displayResult += '|一同|'
            elif i == Data.deck['twoCircle']:
                displayResult += '|二同|'
            elif i == Data.deck['threeCircle']:
                displayResult += '|三同|'
            elif i == Data.deck['fourCircle']:
                displayResult += '|四同|'
            elif i == Data.deck['fiveCircle']:
                displayResult += '|五同|'
            elif i == Data.deck['sixCircle']:
                displayResult += '|六同|'
            elif i == Data.deck['sevenCircle']:
                displayResult += '|七同|'
            elif i == Data.deck['eightCircle']:
                displayResult += '|八同|'
            elif i == Data.deck['nineCircle']:
                displayResult += '|九同|'
            elif i == Data.deck['oneThousand']:
                displayResult += '|一万|'
            elif i == Data.deck['twoThousand']:
                displayResult += '|二万|'
            elif i == Data.deck['threeThousand']:
                displayResult += '|三万|'
            elif i == Data.deck['fourThousand']:
                displayResult += '|四万|'
            elif i == Data.deck['fiveThousand']:
                displayResult += '|五万|'
            elif i == Data.deck['sixThousand']:
                displayResult += '|六万|'
            elif i == Data.deck['sevenThousand']:
                displayResult += '|七万|'
            elif i == Data.deck['eightThousand']:
                displayResult += '|八万|'
            elif i == Data.deck['nineThousand']:
                displayResult += '|九万|'
            elif i == Data.deck['oneStick']:
                displayResult += '|一条|'
            elif i == Data.deck['twoStick']:
                displayResult += '|二条|'
            elif i == Data.deck['threeStick']:
                displayResult += '|三条|'
            elif i == Data.deck['fourStick']:
                displayResult += '|四条|'
            elif i == Data.deck['fiveStick']:
                displayResult += '|五条|'
            elif i == Data.deck['sixStick']:
                displayResult += '|六条|'
            elif i == Data.deck['sevenStick']:
                displayResult += '|七条|'
            elif i == Data.deck['eightStick']:
                displayResult += '|八条|'
            elif i == Data.deck['nineStick']:
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

    def canShang(self, newDeck):
        for deck in range(len(self.decks)):
            if self.decks[deck] == newDeck + 1 and len(self.decks) - 1 != deck and self.decks[deck+1] == newDeck + 2:
                return (True, "Front")
            elif self.decks[deck] == newDeck - 1 and len(self.decks) - 1 != deck and self.decks[deck+1] == newDeck + 1:
                return (True, "Medium")
            elif self.decks[deck] == newDeck - 2 and len(self.decks) - 1 != deck and self.decks[deck+1] == newDeck - 1:
                return (True, "Last")
        return False

    def pong(self, newDeck):
        if self.canPong(newDeck):
            self.decks.remove(newDeck)
            self.decks.remove(newDeck)
        self.pongdeck.append(newDeck)
        self.pongdeck.append(newDeck)
        self.pongdeck.append(newDeck)

    def kong(self, newDeck):
        if self.canKong(newDeck):
            self.decks.remove(newDeck)
            self.decks.remove(newDeck)
            self.decks.remove(newDeck)
        self.pongdeck.append(newDeck)
        self.pongdeck.append(newDeck)
        self.pongdeck.append(newDeck)
        self.pongdeck.append(newDeck)

    def shang(self, newDeck):
        (canShang, position) = self.canShang(newDeck)
        if canShang:
            if position == "Front":
                self.decks.remove(newDeck + 1)
                self.decks.remove(newDeck + 2)
                self.pongdeck.append(newDeck)
                self.pongdeck.append(newDeck+1)
                self.pongdeck.append(newDeck+2)
            elif position == "Medium":
                self.decks.remove(newDeck - 1)
                self.decks.remove(newDeck + 1)
                self.pongdeck.append(newDeck - 1)
                self.pongdeck.append(newDeck)
                self.pongdeck.append(newDeck+1)
            elif position == "Last":
                self.decks.remove(newDeck - 1)
                self.decks.remove(newDeck - 2)
                self.pongdeck.append(newDeck - 2)
                self.pongdeck.append(newDeck - 1)
                self.pongdeck.append(newDeck)


