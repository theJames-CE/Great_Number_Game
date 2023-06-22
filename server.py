from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'James wuz here!'

# root route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        guess = int(request.form['guess'])

        if 'random_number' not in session:
            session['random_number'] = random.randint(1, 100)
            session['attempts'] = 0

        session['attempts'] += 1

        if guess < session['random_number']:
            status = 'Too low!'
        elif guess > session['random_number']:
            status = 'Too high!'
        else:
            status = 'Congratulations! You guessed the correct number!'
            session.pop('random_number')
            session.pop('attempts')

        if session['attempts'] == 5:
            status = 'You Lose! The correct number was {}'.format(session['random_number'])
            session.pop('random_number')
            session.pop('attempts')

        return {'status': status}

    return render_template('index.html', status='')

@app.route('/restart', methods=['POST'])
def restart():
    session.pop('random_number', None)
    session.pop('attempts', None)
    return {}

if __name__ == '__main__':
    app.run()
