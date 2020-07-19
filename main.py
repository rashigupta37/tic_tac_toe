from flask import Flask, render_template, request, redirect, url_for

from playerRandom import *
from playerMinimax import *
from playerAlphaBeta import *
from Game import *
app = Flask(__name__)
ttt = Game()



@app.route('/start', methods=['GET'])
def start():
   
    return render_template('start.html')


@app.route('/turn1', methods=['POST'])
def firstplay():
        
    
        ttt.depth = int(request.form['options'])
        #print(ttt.depth)
        ttt.p1 = str(request.form.get('player1'))
        ttt.p2 = str(request.form.get('player2'))
        if ttt.p1 == 'h':
            return render_template('index.html',
                                   game=ttt,
                                   move=-1)
        else:
            
            if ttt.p1 == "1":
                    myMove = playerRandom(ttt)
            elif ttt.p1 == "2":
                    myMove = playerMinimax(ttt,ttt.depth)
            elif ttt.p1 == "3":
                    myMove = playerAlphaBeta(ttt,ttt.depth)
            return render_template('index.html',
                                       game=ttt,
                                       move=myMove)
        return redirect(url_for('start'))


@app.route('/', methods=['GET'])
def main():
    global ttt
    
    if request.args.get('gameover') == "1":
        del ttt
        ttt = Game()
        return redirect(url_for('start'))
    if ttt.p1 is ttt.p2 is None:  
        return redirect(url_for('start'))
    return render_template('index.html',
                           game=ttt,
                           move=-1)
@app.route('/hint/',methods=['POST'])
def hint():
   m=playerMinimax(ttt,9)
   row=m//3
   col=m%3
   return render_template('index.html',
                           game=ttt,
                           move=-1,row=row+1,col=col+1)

@app.route("/", methods=['POST'])
def play():
    # process 'click'
    
    clicked = int(request.form['play'][0])
    ttt.move(clicked)
    # if we have a winner, set winnerVar and return to HTML
    if ttt.checkForWinner() > 0:
        ttt.win = ttt.checkForWinner()
        return render_template('index.html',
                               game=ttt,
                               move=-1)
    # next player
    ttt.curPlayer = ttt.curPlayer % 2 + 1
    # check if next player is computer, if so send computer's choice
    if (ttt.curPlayer == 1 and ttt.p1 != 'h') or (ttt.curPlayer == 2 and ttt.p2 != 'h'):
        if ttt.curPlayer == 1:
            if ttt.p1 == "1":
                myMove = playerRandom(ttt)
            elif ttt.p1 == "2":
                myMove = playerMinimax(ttt,ttt.depth)
            elif ttt.p1 == "3":
                myMove = playerAlphaBeta(ttt,ttt.depth)
        else:
            if ttt.p2 == "1":
                myMove = playerRandom(ttt)
            elif ttt.p2 == "2":
                myMove = playerMinimax(ttt,ttt.depth)
            elif ttt.p2 == "3":
                myMove = playerAlphaBeta(ttt,ttt.depth)
            if ttt.checkForWinner() > 0:
                ttt.win = ttt.checkForWinner()
    else: # otherwise it's a human and they'll make their own choice, return move=-1:
        

        myMove = -1
    # return to the HTML
    return render_template('index.html',
                           game=ttt,
                           move=myMove)


if __name__ == "__main__":
    app.run(debug=True)


