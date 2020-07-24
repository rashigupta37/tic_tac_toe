from random import randint, seed
# returns best score and the best move of the board
#depth is a terminating condition

def alphabeta(newGame, game, alpha, beta,depth):
    
    emp = newGame.getEmp()
    
    if newGame.checkForWinner() == game.curPlayer:
        return -1, 100
    elif newGame.checkForWinner() == game.curPlayer % 2 + 1:  
        return -1, -100
    elif not emp:
        return -1, -5

    bestMove = None
    #if max is player
    if newGame.curPlayer == game.curPlayer:
        bestScore = -10000
        
        for i in emp:
            
            newGame.move(i)
            #next level for searching the best move
            newGame.curPlayer = newGame.curPlayer % 2 + 1
            #terminates when depth=0
            if depth!=0:
              #alphabeta is called in the next level
              result = alphabeta(newGame, game, alpha, beta,depth-1)
           
              newGame.clearMove(i)
              newGame.curPlayer = newGame.curPlayer % 2 + 1
              #best move and best score is calculated for max player
              if result[1] > bestScore:
                bestScore = result[1]
                bestMove = i
                
            # alpha beta pruning
            #alpha when max is the player
            alpha = max(bestScore, alpha)
            
            if beta <= alpha:
                break
    else:
        #if min is the player
        bestScore = 10000
        for i in emp:
            
            newGame.move(i)
            #next level for searching the best move
            newGame.curPlayer = newGame.curPlayer % 2 + 1
            #terminates when depth=0
            if depth!=0 :
               #alphabeta is called in the next level
               result = alphabeta(newGame, game, alpha, beta,depth-1)
        
               newGame.clearMove(i)
               newGame.curPlayer = newGame.curPlayer % 2 + 1
               #best move and best score is calculated for min player
               if result[1] < bestScore:
                bestScore = result[1]
                bestMove = i
                
            # alpha beta pruning
            #beta when min is the player
            beta = min(bestScore, beta)
            if beta <= alpha:
                break
    
    return bestMove, bestScore


#it is called when player selects alphabeta player 
def playerAlphaBeta(game,depth):
    
    newGame = game.getCopy()
    #if alphabeta player starts first, choose any box randomly to minimize the time
    if len(game.getEmp()) == 9:
        seed()
        
        myMove = [randint(0, 8), None]
    else:
        myMove = alphabeta(newGame, game, -float('inf'), float('inf'),depth)
    #print(myMove[0]) is minimax move
    #print(myMove[1]) is minimax score
    #return minimax move 
    
    return myMove[0]
