import numpy as np


class TicTacToeGame:

    def __init__(self, size):
        self.m_SizeSize = size;
        self.m_Grid = np.zeros((size, size), np.int8)
        self.m_Grid.fill(-1)
        self.m_CurentPlayer = 0

    def Move(self, player, row, col):
        if self.IsMoveAllowed(player, row, col) == True:
            self.m_Grid[row][col] = player

    def WillMoveWin(self, player, row, col):
        if not self.IsMoveAllowed(player, row, col):
            return False

        # check horizontal
        hasWon = True
        for i in range(self.m_SizeSize):
            colIdx = (col + i) % self.m_SizeSize
            hasWon = hasWon and self.m_Grid[row][colIdx] == player

            # Check vertical win
        if not hasWon:
            hasWon = True
            for i in range(self.m_SizeSize):
                rowIdx = (row + i) % self.m_SizeSize
                hasWon = hasWon and self.m_Grid[row][colIdx] == player

        if not hasWon and row == 1 and col == 1:
            hasWon = True
            # Test diagonal from upper left to lower right
            for i in range(self.m_SizeSize):
                hasWon = hasWon and self.m_Grid[i][i] == player
            if hasWon:
                return True

            # Test diagnol from lower left to upper right
            hasWon = True
            for i in range(self.m_SizeSize):
                hasWon = hasWon and self.m_Grid[2 - i][i] == player

        return hasWon

    def RankMove(self, player, row, col):
        reward = 0
        if not self.IsMoveAllowed(player, row, col):
            reward = reward + -100
        backup = self.m_Grid[row][col]
        self.m_Grid[row][col] = player

        if self.WillMoveWin(player, row, col):
            reward = reward + 1000

        self.m_Grid[row][col] = backup
        return reward

    def IsMoveAllowed(self, player, row, col):
        if int(row) in range(self.m_SizeSize) and int(col) in range(self.m_SizeSize):
            return self.m_Grid[row][col] == -1
        else:
            return False

    def NoEmptySpaces(self):
        for i in range(self.m_SizeSize):
            for j in range(self.m_SizeSize):
                if self.m_Grid[i][j] == -1:
                    return False
        return True

    def Render(self):
        # print (self.m_Grid)
        print("")
        for row in range(self.m_SizeSize):
            lineTxt = ""
            for col in range(self.m_SizeSize):
                if (self.m_Grid[row][col] == 0):
                    lineTxt += "   O"
                elif (self.m_Grid[row][col] == 0):
                    lineTxt += "   X"
                else:
                    lineTxt += "   _"
            print(lineTxt)
