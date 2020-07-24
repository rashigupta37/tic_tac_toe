from random import randint, seed

#returns best move and best score if max is the player
def getMax(moves,bestScore,scores,bestMove):
    #traverse all the moves in the board
    for i in range(len(moves)):    
            
            #if curretnt score is better than the best score
            if scores[i] > bestScore:
                bestScore = scores[i]

                bestMove = moves[i]
                
    return bestMove, bestScore



#returns best move and best score if min is the player
def getMin(moves,bestScore,scores,bestMove):
    #traverse all the moves in the board
    for i in range(len(moves)):
            #if curretnt score is better than the best score
            if scores[i] < bestScore:
                bestScore = scores[i]
                
                bestMove = moves[i]
    return bestMove, bestScore


#minimax algorithm It considers all the possible ways the game can go and returns the best score and the best move of the board 
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
        #if depth is not zero, minimax is called 
        if depth!=0:
            result = minimax(newGame, game,depth-1)
            moves.append(emp[i])
            scores.append(result[1])
        

            newGame.clearMove(emp[i])
            #player changes
            newGame.curPlayer = newGame.curPlayer % 2 + 1
    
    bestMove = None
    #max player
    if newGame.curPlayer == game.curPlayer:
        #intialise bestScore with minimum value as it's max player's turn
        bestScore = -10000
        bestMove, bestScore=getMax(moves,bestScore,scores,bestMove)
        
    #min player
    else:
        #intialise bestScore with maximum value as it's min player's turn
        bestScore = 10000
        bestMove, bestScore=getMin(moves,bestScore,scores,bestMove)
       
    #returns best move and best score
    return bestMove, bestScore


#function is called when player chooses minimax player
def playerMinimax(game,depth):
    
    #print(depth)
    #copy the current state 
    newGame = game.getCopy()
    #if minimax player starts first, choose any box randomly to minimize the time
    if len(game.getEmp()) == 9:
        seed()
        
        myMove = [randint(0, 8), None]
    else:
        #if second turn is of minimax player's call minimax
        myMove = minimax(newGame, game, depth)
        
    #print(myMove[0]) is minimax move
    #print(myMove[1]) is minimax score
    #return minimax move 
    return myMove[0]
