from flask import flash, Flask, redirect, render_template, request, session, url_for
from tictactoe.utils import game_over, computer_move
import os

app = Flask(__name__)
app.secret_key = os.urandom(16)


@app.before_request
def initialize_session():
    if 'squares' not in session:
        session['squares'] = {f'{key}' : " " for key in range(1,10)}

@app.route("/")
def index():
    return render_template('home.html')
    
@app.route('/play')
def play():
    squares = session['squares']
    print(game_over(squares))
    if game_over(squares):
        flash('Game over. Thanks for playing!', 'success')
        return redirect(url_for('index'))
    return render_template('play.html')
    
@app.route('/verify', methods=["POST"])
def verify():
    new_square = request.form['new_square']
    if not new_square in [str(num) for num in range(1, 10)]:
        flash('Number must be range 1-10', 'error')
        return render_template('play.html')
    session['squares'][new_square] = "X"
    session.modified = True
    return redirect(url_for('computer'))
        
@app.route('/computer')
def computer():
    squares = session.get('squares')
    if game_over(squares):
        flash('Game over. Thanks for playing!', 'success')
        return redirect(url_for('index'))
    move = computer_move(squares)
    session['squares'][move] = "O"
    session.modified = True
    return redirect(url_for('play'))
    
    
if __name__ == "__main__":
    if os.environ.get('FLASK_ENVIRON') == 'production':
        app.run(debug=False)
    else:
        app.run(debug=True, port=8080)
