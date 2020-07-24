import copy
#game class
class Game:
    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.win = 0 #winner
        self.curPlayer = 1  #current player
        self.boardSize = 3  #board-size
        self.moveHistory = [] #stores move history
        self.p1 = None #first player
        self.p2 = None  #second player
        self.depth=0
        
    # checks whether board is full or not
    def isBoardFull(self):
        ans = True
        for i in self.board:
            
            if i.count(0) > 0:
                ans = False
                break

        return ans
    #stores moves of current player in the board
    def move(self, n):
        if n not in range(0, 9):
            return -2
        if self.board[n//3][n%3] == 0:
            self.board[n//3][n%3] = self.curPlayer
            self.moveHistory.append(n+1)
            return 1
        else:
            return -1

    
    #clears the move from the table
    def clearMove(self, n):
        if n not in range(0, 9):
            return -2
        else:
            self.board[n//3][n%3] = 0
            return 1
    #filling the position of board in emp[] after flattening
    #ex: board[0][0]=0, board[0][1]=1.... board[2][2]=8   
    def getEmp(self):
        emp = []
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if self.board[i][j] == 0:
                    emp.append((i*3)+j)
        return emp

    def getCopy(self):
        return copy.deepcopy(self)
    
    
    #checks for the winner
    def checkForWinner(self):
        
        #checks first row for victory
        if self.board[0][0] == self.board[0][1] == self.board[0][2] != 0:
            return self.board[0][1]
         #checks second row for victory
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] != 0:
            return self.board[1][1]
         #checks third row for victory
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] != 0:
            return self.board[2][1]
        #checks leading diagnol for victory
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            return self.board[0][0] 
        #checks first column for victory
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] != 0:
            return self.board[0][0]
        #checks second column for victory
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] != 0:
            return self.board[0][1]
        #checks third column for victory
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] != 0:
            return self.board[0][2]
        #checks the other diagnol for victory
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            return self.board[0][2]
        else:
            return 0

    
