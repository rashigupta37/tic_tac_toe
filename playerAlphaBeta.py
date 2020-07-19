from random import randint, seed

def alphabeta(newGame, game, alpha, beta,depth):
    emp = newGame.getEmp()
    if newGame.checkForWinner() == game.curPlayer:
        return -1, 100
    elif newGame.checkForWinner() == game.curPlayer % 2 + 1:  
        return -1, -100
    elif not emp:
        return -1, -5

    bestMove = None
    if newGame.curPlayer == game.curPlayer:
        bestScore = -10000
        for i in emp:
            
            newGame.move(i)
            newGame.curPlayer = newGame.curPlayer % 2 + 1
            
            if depth!=0:
              result = alphabeta(newGame, game, alpha, beta,depth-1)
           
              newGame.clearMove(i)
              newGame.curPlayer = newGame.curPlayer % 2 + 1
            
              if result[1] > bestScore:
                bestScore = result[1]
                bestMove = i
                
            # alpha beta pruning
            alpha = max(bestScore, alpha)
            if beta <= alpha:
                break
    else:
        bestScore = 10000
        for i in emp:
            
            newGame.move(i)
            newGame.curPlayer = newGame.curPlayer % 2 + 1
           
            if depth!=0 :
               result = alphabeta(newGame, game, alpha, beta,depth-1)
        
               newGame.clearMove(i)
               newGame.curPlayer = newGame.curPlayer % 2 + 1
            
               if result[1] < bestScore:
                bestScore = result[1]
                bestMove = i
                
            # alpha beta pruning
            beta = min(bestScore, beta)
            if beta <= alpha:
                break
    
    return bestMove, bestScore



def playerAlphaBeta(game,depth):
   
    newGame = game.getCopy()
   
    if len(game.getEmp()) == 9:
        seed()
        # myMove = [0, None]
        myMove = [randint(0, 8), None]
    else:
        myMove = alphabeta(newGame, game, -float('inf'), float('inf'),depth)
    # print("My minimax move:", myMove[0]+1)
    
    return myMove[0]