from random import randint, seed


def getMax(moves,bestScore,scores,bestMove):
    for i in range(len(moves)):
            if scores[i] > bestScore:
                bestScore = scores[i]
                
                bestMove = moves[i]
    return bestMove, bestScore

def getMin(moves,bestScore,scores,bestMove):
    for i in range(len(moves)):
            if scores[i] < bestScore:
                bestScore = scores[i]
                
                bestMove = moves[i]
    return bestMove, bestScore

def minimax(newGame, game,depth):
   
    
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
        

            newGame.clearMove(emp[i])
            newGame.curPlayer = newGame.curPlayer % 2 + 1

    bestMove = None
    #max-block
    if newGame.curPlayer == game.curPlayer:

        bestScore = -10000
        bestMove, bestScore=getMax(moves,bestScore,scores,bestMove)
        
    #min-block
    else:
        bestScore = 10000
        bestMove, bestScore=getMin(moves,bestScore,scores,bestMove)
       
    
    return bestMove, bestScore



def playerMinimax(game,depth):
    
    #print(depth)
    newGame = game.getCopy()
    
    if len(game.getEmp()) == 9:
        seed()
        
        myMove = [randint(0, 8), None]
    else:
        myMove = minimax(newGame, game, depth)
    #print(myMove[0])
    #print(myMove[1])

    return myMove[0]