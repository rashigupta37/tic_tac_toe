import copy

class Game:
    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.win = 0
        self.curPlayer = 1
        self.boardSize = 3
        self.moveHistory = []
        self.masterFC = 0
        self.p1 = None
        self.p2 = None

    def isBoardFull(self):
        ans = True
        for i in self.board:
            if i.count(0) > 0:
                ans = False
                break

        return ans

    def move(self, n):
        if n not in range(0, 9):
            return -2
        if self.board[n//3][n%3] == 0:
            self.board[n//3][n%3] = self.curPlayer
            self.moveHistory.append(n+1)
            return 1
        else:
            return -1

    

    def clearMove(self, n):
        if n not in range(0, 9):
            return -2
        else:
            self.board[n//3][n%3] = 0
            return 1

    def getEmp(self):
        emp = []
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if self.board[i][j] == 0:
                    emp.append((i*3)+j)
        return emp

    def getCopy(self):
        return copy.deepcopy(self)

    def checkForWinner(self):
       
    
        if self.board[0][0] == self.board[0][1] == self.board[0][2] != 0:
            return self.board[0][1]
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] != 0:
            return self.board[1][1]
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] != 0:
            return self.board[2][1]
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] != 0:
            return self.board[0][0]
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] != 0:
            return self.board[0][1]
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] != 0:
            return self.board[0][2]
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            return self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            return self.board[0][2]
        else:
            return 0

    
