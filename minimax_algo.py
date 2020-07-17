from random import randint, seed
flag=0

def getMax(moves,bestScore):
    for i in range(len(moves)):
            if scores[i] > bestScore:
                bestScore = scores[i]
                
                bestMove = moves[i]
    return bestMove, bestScore

def getMin(moves,bestScore):
    for i in range(len(moves)):
            if scores[i] < bestScore:
                bestScore = scores[i]
                
                bestMove = moves[i]
    return bestMove, bestScore

def minimax(newGame, game,depth):
    global flag
    flag+=1
    game.masterFC += 1
    #print(depth)

    emp = newGame.getEmp()

    if newGame.checkForWinner() == game.curPlayer:
        return -1, 100
    elif newGame.checkForWinner() == game.curPlayer % 2 + 1:
        return -1, -100

    elif not emp:
        return -1, -5
    

    moves = []
    scores = []
    for i in range(len(emp)):
        newGame.move(emp[i])
        newGame.curPlayer = newGame.curPlayer % 2 + 1
        if depth!=0:
            result = minimax(newGame, game,depth-1)
            moves.append(emp[i])
            scores.append(result[1])
        

            newGame.clearMove(empt[i])
            newGame.curPlayer = newGame.curPlayer % 2 + 1

    bestMove = None
    #max-block
    if newGame.curPlayer == game.curPlayer:

        bestScore = -10000
        bestMove, bestScore=getMax(moves,bestScore)
        
    #min-block
    else:
        bestScore = 10000
        bestMove, bestScore=getMin(moves,bestScore)
       
    
    return bestMove, bestScore



def computerMinimax(game,depth):
    global flag
    flag = 0
    newGame = game.getCopy()
    
    if len(game.getEmp()) == 9:
        seed()
        
        myMove = [randint(0, 8), None]
    else:
        myMove = minimax(newGame, game, depth)
    
    return myMove[0]
