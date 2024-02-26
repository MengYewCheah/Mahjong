from Data import DeckData

Data = DeckData()
class PygamesDisplayData:
    def __init__(self, pygame):
        # create a surface object, image is drawn on it.
        self.center = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\center.png").convert_alpha()
        self.east = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\east.png").convert_alpha()
        self.west = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\west.png").convert_alpha()
        self.south = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\south.png").convert_alpha()
        self.north = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\north.png").convert_alpha()
        self.fa = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\fa.png").convert_alpha()
        self.space = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\space.png").convert_alpha()
        self.oneCircle = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\oneCircle.png").convert_alpha()
        self.twoCircle = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\twoCircle.png").convert_alpha()
        self.threeCircle = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\threeCircle.png").convert_alpha()
        self.fourCircle = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\fourCircle.png").convert_alpha()
        self.fiveCircle = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\fiveCircle.png").convert_alpha()
        self.sixCircle = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\sixCircle.png").convert_alpha()
        self.sevenCircle = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\sevenCircle.png").convert_alpha()
        self.eightCircle = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\eightCircle.png").convert_alpha()
        self.nineCircle = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\nineCircle.png").convert_alpha()

        self.oneThousand = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\oneThousand.png").convert_alpha()
        self.twoThousand= pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\twoThousand.png").convert_alpha()
        self.threeThousand= pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\threeThousand.png").convert_alpha()
        self.fourThousand = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\fourThousand.png").convert_alpha()
        self.fiveThousand = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\fiveThousand.png").convert_alpha()
        self.sixThousand = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\sixThousand.png").convert_alpha()
        self.sevenThousand = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\sevenThousand.png").convert_alpha()
        self.eightThousand = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\eightThousand.png").convert_alpha()
        self.nineThousand = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\nineThousand.png").convert_alpha()

        self.oneStick = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\oneStick.png").convert_alpha()
        self.twoStick = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\twoStick.png").convert_alpha()
        self.threeStick= pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\threeStick.png").convert_alpha()
        self.fourStick = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\fourStick.png").convert_alpha()
        self.fiveStick = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\fiveStick.png").convert_alpha()
        self.sixStick = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\sixStick.png").convert_alpha()
        self.sevenStick = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\sevenStick.png").convert_alpha()
        self.eightStick = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\eightStick.png").convert_alpha()
        self.nineStick = pygame.image.load("C:\\Users\\Cheah Meng Yew\\Desktop\\CSS training\\bootstrap\\Learning\\mahjong tiles\\nineStick.png").convert_alpha()

        self.startingRow = 450
        self.startingCol = 130

        self.tableRow = 150
        self.tableCol = 130

        self.textRow = 100
        self.textCol = 550

    def displaytable(self, scrn, tablecenter):
        tableRowIndex = self.tableRow
        displayIndex = self.tableCol
        numberOfPieces = 0
        for i in tablecenter:
            if i == Data.deck['east']:
                scrn.blit(self.east, (displayIndex, tableRowIndex))
            elif i == Data.deck['west']:
                scrn.blit(self.west, (displayIndex, tableRowIndex))
            elif i == Data.deck['north']:
                scrn.blit(self.north, (displayIndex, tableRowIndex))
            elif i == Data.deck['south']:
                scrn.blit(self.south, (displayIndex, tableRowIndex))
            elif i == Data.deck['center']:
                scrn.blit(self.center, (displayIndex, tableRowIndex))
            elif i == Data.deck['space']:
                scrn.blit(self.space, (displayIndex, tableRowIndex))
            elif i == Data.deck['fa']:
                scrn.blit(self.fa, (displayIndex, tableRowIndex))
            elif i == Data.deck['oneCircle']:
                scrn.blit(self.oneCircle, (displayIndex, tableRowIndex))
            elif i == Data.deck['twoCircle']:
                scrn.blit(self.twoCircle, (displayIndex, tableRowIndex))
            elif i == Data.deck['threeCircle']:
                scrn.blit(self.threeCircle, (displayIndex, tableRowIndex))
            elif i == Data.deck['fourCircle']:
                scrn.blit(self.fourCircle, (displayIndex, tableRowIndex))
            elif i == Data.deck['fiveCircle']:
                scrn.blit(self.fiveCircle, (displayIndex, tableRowIndex))
            elif i == Data.deck['sixCircle']:
                scrn.blit(self.sixCircle, (displayIndex, tableRowIndex))
            elif i == Data.deck['sevenCircle']:
                scrn.blit(self.sevenCircle, (displayIndex, tableRowIndex))
            elif i == Data.deck['eightCircle']:
                scrn.blit(self.eightCircle, (displayIndex, tableRowIndex))
            elif i == Data.deck['nineCircle']:
                scrn.blit(self.nineCircle, (displayIndex, tableRowIndex))
            elif i == Data.deck['oneThousand']:
                scrn.blit(self.oneThousand, (displayIndex, tableRowIndex))
            elif i == Data.deck['twoThousand']:
                scrn.blit(self.twoThousand, (displayIndex, tableRowIndex))
            elif i == Data.deck['threeThousand']:
                scrn.blit(self.threeThousand, (displayIndex, tableRowIndex))
            elif i == Data.deck['fourThousand']:
                scrn.blit(self.fourThousand, (displayIndex, tableRowIndex))
            elif i == Data.deck['fiveThousand']:
                scrn.blit(self.fiveThousand, (displayIndex, tableRowIndex))
            elif i == Data.deck['sixThousand']:
                scrn.blit(self.sixThousand, (displayIndex, tableRowIndex))
            elif i == Data.deck['sevenThousand']:
                scrn.blit(self.sevenThousand, (displayIndex, tableRowIndex))
            elif i == Data.deck['eightThousand']:
                scrn.blit(self.eightThousand, (displayIndex, tableRowIndex))
            elif i == Data.deck['nineThousand']:
                scrn.blit(self.nineThousand, (displayIndex, tableRowIndex))
            elif i == Data.deck['oneStick']:
                scrn.blit(self.oneStick, (displayIndex, tableRowIndex))
            elif i == Data.deck['twoStick']:
                scrn.blit(self.twoStick, (displayIndex, tableRowIndex))
            elif i == Data.deck['threeStick']:
                scrn.blit(self.threeStick, (displayIndex, tableRowIndex))
            elif i == Data.deck['fourStick']:
                scrn.blit(self.fourStick, (displayIndex, tableRowIndex))
            elif i == Data.deck['fiveStick']:
                scrn.blit(self.fiveStick, (displayIndex, tableRowIndex))
            elif i == Data.deck['sixStick']:
                scrn.blit(self.sixStick, (displayIndex, tableRowIndex))
            elif i == Data.deck['sevenStick']:
                scrn.blit(self.sevenStick, (displayIndex, tableRowIndex))
            elif i == Data.deck['eightStick']:
                scrn.blit(self.eightStick, (displayIndex, tableRowIndex))
            elif i == Data.deck['nineStick']:
                scrn.blit(self.nineStick, (displayIndex, tableRowIndex))
            numberOfPieces += 1
            numberOfRow = numberOfPieces // 13
            numberofCol = numberOfPieces % 13
            displayIndex = self.tableCol + numberofCol * 24
            tableRowIndex = self.tableRow + numberOfRow * 32

    def displayPlayer(self, scrn, playerDeck):
        rowDisplayIndex = self.startingRow
        visibleTilesSpriteLocation = []
        displayIndex = self.startingCol
        for i in playerDeck.decks:
            if i == Data.deck['east']:
                visibleTilesSpriteLocation.append(('east', (displayIndex, rowDisplayIndex)))
                scrn.blit(self.east, (displayIndex, rowDisplayIndex))
            elif i == Data.deck['west']:
                visibleTilesSpriteLocation.append(('west', (displayIndex, rowDisplayIndex)))
                scrn.blit(self.west, (displayIndex, rowDisplayIndex))
            elif i == Data.deck['north']:
                visibleTilesSpriteLocation.append(('north', (displayIndex, rowDisplayIndex)))
                scrn.blit(self.north, (displayIndex, rowDisplayIndex))
            elif i == Data.deck['south']:
                visibleTilesSpriteLocation.append(('south', (displayIndex, rowDisplayIndex)))
                scrn.blit(self.south, (displayIndex, rowDisplayIndex))
            elif i == Data.deck['center']:
                visibleTilesSpriteLocation.append(('center', (displayIndex, rowDisplayIndex)))
                scrn.blit(self.center, (displayIndex, rowDisplayIndex))
            elif i == Data.deck['space']:
                visibleTilesSpriteLocation.append(('space', (displayIndex, rowDisplayIndex)))
                scrn.blit(self.space, (displayIndex, rowDisplayIndex))
            elif i == Data.deck['fa']:
                visibleTilesSpriteLocation.append(('fa', (displayIndex, rowDisplayIndex)))
                scrn.blit(self.fa, (displayIndex, rowDisplayIndex))
            elif i == Data.deck['oneCircle']:
                visibleTilesSpriteLocation.append(('oneCircle', (displayIndex, rowDisplayIndex)))
                scrn.blit(self.oneCircle, (displayIndex, rowDisplayIndex))
            elif i == Data.deck['twoCircle']:
                visibleTilesSpriteLocation.append(('twoCircle', (displayIndex, rowDisplayIndex)))
                scrn.blit(self.twoCircle, (displayIndex, rowDisplayIndex))
            elif i == Data.deck['threeCircle']:
                visibleTilesSpriteLocation.append(('threeCircle', (displayIndex, rowDisplayIndex)))
                scrn.blit(self.threeCircle, (displayIndex, rowDisplayIndex))
            elif i == Data.deck['fourCircle']:
                visibleTilesSpriteLocation.append(('fourCircle', (displayIndex, rowDisplayIndex)))
                scrn.blit(self.fourCircle, (displayIndex, rowDisplayIndex))
            elif i == Data.deck['fiveCircle']:
                visibleTilesSpriteLocation.append(('fiveCircle', (displayIndex, rowDisplayIndex)))
                scrn.blit(self.fiveCircle, (displayIndex, rowDisplayIndex))
            elif i == Data.deck['sixCircle']:
                visibleTilesSpriteLocation.append(('sixCircle', (displayIndex, rowDisplayIndex)))
                scrn.blit(self.sixCircle, (displayIndex, rowDisplayIndex))
            elif i == Data.deck['sevenCircle']:
                visibleTilesSpriteLocation.append(('sevenCircle', (displayIndex, rowDisplayIndex)))
                scrn.blit(self.sevenCircle, (displayIndex, rowDisplayIndex))
            elif i == Data.deck['eightCircle']:
                visibleTilesSpriteLocation.append(('eightCircle', (displayIndex, rowDisplayIndex)))
                scrn.blit(self.eightCircle, (displayIndex, rowDisplayIndex))
            elif i == Data.deck['nineCircle']:
                visibleTilesSpriteLocation.append(('nineCircle', (displayIndex, rowDisplayIndex)))
                scrn.blit(self.nineCircle, (displayIndex, rowDisplayIndex))
            elif i == Data.deck['oneThousand']:
                visibleTilesSpriteLocation.append(('oneThousand', (displayIndex, rowDisplayIndex)))
                scrn.blit(self.oneThousand, (displayIndex, rowDisplayIndex))
            elif i == Data.deck['twoThousand']:
                visibleTilesSpriteLocation.append(('twoThousand', (displayIndex, rowDisplayIndex)))
                scrn.blit(self.twoThousand, (displayIndex, rowDisplayIndex))
            elif i == Data.deck['threeThousand']:
                visibleTilesSpriteLocation.append(('threeThousand', (displayIndex, rowDisplayIndex)))
                scrn.blit(self.threeThousand, (displayIndex, rowDisplayIndex))
            elif i == Data.deck['fourThousand']:
                visibleTilesSpriteLocation.append(('fourThousand', (displayIndex, rowDisplayIndex)))
                scrn.blit(self.fourThousand, (displayIndex, rowDisplayIndex))
            elif i == Data.deck['fiveThousand']:
                visibleTilesSpriteLocation.append(('fiveThousand', (displayIndex, rowDisplayIndex)))
                scrn.blit(self.fiveThousand, (displayIndex, rowDisplayIndex))
            elif i == Data.deck['sixThousand']:
                visibleTilesSpriteLocation.append(('sixThousand', (displayIndex, rowDisplayIndex)))
                scrn.blit(self.sixThousand, (displayIndex, rowDisplayIndex))
            elif i == Data.deck['sevenThousand']:
                visibleTilesSpriteLocation.append(('sevenThousand', (displayIndex, rowDisplayIndex)))
                scrn.blit(self.sevenThousand, (displayIndex, rowDisplayIndex))
            elif i == Data.deck['eightThousand']:
                visibleTilesSpriteLocation.append(('eightThousand', (displayIndex, rowDisplayIndex)))
                scrn.blit(self.eightThousand, (displayIndex, rowDisplayIndex))
            elif i == Data.deck['nineThousand']:
                visibleTilesSpriteLocation.append(('nineThousand', (displayIndex, rowDisplayIndex)))
                scrn.blit(self.nineThousand, (displayIndex, rowDisplayIndex))
            elif i == Data.deck['oneStick']:
                visibleTilesSpriteLocation.append(('oneStick', (displayIndex, rowDisplayIndex)))
                scrn.blit(self.oneStick, (displayIndex, rowDisplayIndex))
            elif i == Data.deck['twoStick']:
                visibleTilesSpriteLocation.append(('twoStick', (displayIndex, rowDisplayIndex)))
                scrn.blit(self.twoStick, (displayIndex, rowDisplayIndex))
            elif i == Data.deck['threeStick']:
                visibleTilesSpriteLocation.append(('threeStick', (displayIndex, rowDisplayIndex)))
                scrn.blit(self.threeStick, (displayIndex, rowDisplayIndex))
            elif i == Data.deck['fourStick']:
                visibleTilesSpriteLocation.append(('fourStick', (displayIndex, rowDisplayIndex)))
                scrn.blit(self.fourStick, (displayIndex, rowDisplayIndex))
            elif i == Data.deck['fiveStick']:
                visibleTilesSpriteLocation.append(('fiveStick', (displayIndex, rowDisplayIndex)))
                scrn.blit(self.fiveStick, (displayIndex, rowDisplayIndex))
            elif i == Data.deck['sixStick']:
                visibleTilesSpriteLocation.append(('sixStick', (displayIndex, rowDisplayIndex)))
                scrn.blit(self.sixStick, (displayIndex, rowDisplayIndex))
            elif i == Data.deck['sevenStick']:
                visibleTilesSpriteLocation.append(('sevenStick', (displayIndex, rowDisplayIndex)))
                scrn.blit(self.sevenStick, (displayIndex, rowDisplayIndex))
            elif i == Data.deck['eightStick']:
                visibleTilesSpriteLocation.append(('eightStick', (displayIndex, rowDisplayIndex)))
                scrn.blit(self.eightStick, (displayIndex, rowDisplayIndex))
            elif i == Data.deck['nineStick']:
                visibleTilesSpriteLocation.append(('nineStick', (displayIndex, rowDisplayIndex)))
                scrn.blit(self.nineStick, (displayIndex, rowDisplayIndex))
            displayIndex += 24
        return visibleTilesSpriteLocation

    def displayPlayerPongKong(self, scrn, playerDeck):
        pongKongRowDisplayIndex = self.startingRow + 32
        pongKongDisplayIndex = self.startingCol
        for i in playerDeck.pongdeck:
            if i == Data.deck['east']:
                scrn.blit(self.east, (pongKongDisplayIndex, pongKongRowDisplayIndex))
            elif i == Data.deck['west']:
                scrn.blit(self.west, (pongKongDisplayIndex, pongKongRowDisplayIndex))
            elif i == Data.deck['north']:
                scrn.blit(self.north, (pongKongDisplayIndex, pongKongRowDisplayIndex))
            elif i == Data.deck['south']:
                scrn.blit(self.south, (pongKongDisplayIndex, pongKongRowDisplayIndex))
            elif i == Data.deck['center']:
                scrn.blit(self.center, (pongKongDisplayIndex, pongKongRowDisplayIndex))
            elif i == Data.deck['space']:
                scrn.blit(self.space, (pongKongDisplayIndex, pongKongRowDisplayIndex))
            elif i == Data.deck['fa']:
                scrn.blit(self.fa, (pongKongDisplayIndex, pongKongRowDisplayIndex))
            elif i == Data.deck['oneCircle']:
                scrn.blit(self.oneCircle, (pongKongDisplayIndex, pongKongRowDisplayIndex))
            elif i == Data.deck['twoCircle']:
                scrn.blit(self.twoCircle, (pongKongDisplayIndex, pongKongRowDisplayIndex))
            elif i == Data.deck['threeCircle']:
                scrn.blit(self.threeCircle, (pongKongDisplayIndex, pongKongRowDisplayIndex))
            elif i == Data.deck['fourCircle']:
                scrn.blit(self.fourCircle, (pongKongDisplayIndex, pongKongRowDisplayIndex))
            elif i == Data.deck['fiveCircle']:
                scrn.blit(self.fiveCircle, (pongKongDisplayIndex, pongKongRowDisplayIndex))
            elif i == Data.deck['sixCircle']:
                scrn.blit(self.sixCircle, (pongKongDisplayIndex, pongKongRowDisplayIndex))
            elif i == Data.deck['sevenCircle']:
                scrn.blit(self.sevenCircle, (pongKongDisplayIndex, pongKongRowDisplayIndex))
            elif i == Data.deck['eightCircle']:
                scrn.blit(self.eightCircle, (pongKongDisplayIndex, pongKongRowDisplayIndex))
            elif i == Data.deck['nineCircle']:
                scrn.blit(self.nineCircle, (pongKongDisplayIndex, pongKongRowDisplayIndex))
            elif i == Data.deck['oneThousand']:
                scrn.blit(self.oneThousand, (pongKongDisplayIndex, pongKongRowDisplayIndex))
            elif i == Data.deck['twoThousand']:
                scrn.blit(self.twoThousand, (pongKongDisplayIndex, pongKongRowDisplayIndex))
            elif i == Data.deck['threeThousand']:
                scrn.blit(self.threeThousand, (pongKongDisplayIndex, pongKongRowDisplayIndex))
            elif i == Data.deck['fourThousand']:
                scrn.blit(self.fourThousand, (pongKongDisplayIndex, pongKongRowDisplayIndex))
            elif i == Data.deck['fiveThousand']:
                scrn.blit(self.fiveThousand, (pongKongDisplayIndex, pongKongRowDisplayIndex))
            elif i == Data.deck['sixThousand']:
                scrn.blit(self.sixThousand, (pongKongDisplayIndex, pongKongRowDisplayIndex))
            elif i == Data.deck['sevenThousand']:
                scrn.blit(self.sevenThousand, (pongKongDisplayIndex, pongKongRowDisplayIndex))
            elif i == Data.deck['eightThousand']:
                scrn.blit(self.eightThousand, (pongKongDisplayIndex, pongKongRowDisplayIndex))
            elif i == Data.deck['nineThousand']:
                scrn.blit(self.nineThousand, (pongKongDisplayIndex, pongKongRowDisplayIndex))
            elif i == Data.deck['oneStick']:
                scrn.blit(self.oneStick, (pongKongDisplayIndex, pongKongRowDisplayIndex))
            elif i == Data.deck['twoStick']:
                scrn.blit(self.twoStick, (pongKongDisplayIndex, pongKongRowDisplayIndex))
            elif i == Data.deck['threeStick']:
                scrn.blit(self.threeStick, (pongKongDisplayIndex, pongKongRowDisplayIndex))
            elif i == Data.deck['fourStick']:
                scrn.blit(self.fourStick, (pongKongDisplayIndex, pongKongRowDisplayIndex))
            elif i == Data.deck['fiveStick']:
                scrn.blit(self.fiveStick, (pongKongDisplayIndex, pongKongRowDisplayIndex))
            elif i == Data.deck['sixStick']:
                scrn.blit(self.sixStick, (pongKongDisplayIndex, pongKongRowDisplayIndex))
            elif i == Data.deck['sevenStick']:
                scrn.blit(self.sevenStick, (pongKongDisplayIndex, pongKongRowDisplayIndex))
            elif i == Data.deck['eightStick']:
                scrn.blit(self.eightStick, (pongKongDisplayIndex, pongKongRowDisplayIndex))
            elif i == Data.deck['nineStick']:
                scrn.blit(self.nineStick, (pongKongDisplayIndex, pongKongRowDisplayIndex))
            pongKongDisplayIndex += 24