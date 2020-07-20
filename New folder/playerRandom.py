from random import choice, seed

def playerRandom(game):
    
    seed()
    myMove = choice(game.getEmp())
    
    return myMove