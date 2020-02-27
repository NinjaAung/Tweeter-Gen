from dictogram import Dictogram

from flask import Flask
app = Flask(__name__)
test = "one fish two fish red fish blue fish"

@app.route('/')
def randomized_word():
    return f'{Dictogram(test)}'



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.getenv('PORT', 5000))



