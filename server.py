from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "great game key"

# @app.route('/', methods = ['POST'])
@app.route('/')
def index():
    if 'random_number' not in session:
        session['random_number'] = random.randint(1, 100)
    return render_template("index.html")

@app.route('/guess', methods = ['POST'])
def users_guess():
    if 'attempt' not in session:
        session['attempt'] = 0
    session['guess'] = int(request.form['guess'])
    
    if 'guess' in session:
        session['attempt'] +=1
        
    return redirect('/')

@app.route('/submit', methods = ['POST'])
def submit_info():
    session['leaderboard'] = []
    session['leaderboard'].append(request.form['user_info'])
    return redirect('/')

@app.route('/reset', methods = ['POST'])
def reset():
    session.clear()
    return redirect('/')
    

if __name__=="__main__":
    app.run(debug=True)