from random import choice, seed
#when player chooses to play against random player 
def playerRandom(game):
    #to initialize the random number generator
    seed()
    #choice() is used to returns a random item from a list
    myMove = choice(game.getEmp())
    
    return myMove
