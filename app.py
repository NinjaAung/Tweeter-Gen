from dictogram import Dictogram
from markov import MarkovChain
from flask import request
from flask import Flask

app = Flask(__name__)
test = "one fish two fish red fish blue fish"

@app.route('/')
def send_to():
    return '''
<html>
    <style>

    </style>
        <head>
            <title>Route to Code</title>
        </head>
   <body>
   
      <button onclick="window.location.href = '/histogram';">Histogram Example</button>
      <button onclick="window.location.href = '/markov/book.txt';">Markov Chain example</button>
   </body>
'''


@app.route('/histogram')
def randomized_word():
    histogram = Dictogram(test.split())
    random_words = ""
    n = "\n"
    for _ in range(0, histogram.tokens):
        random_words += f' {histogram.sample()}'
    return f'''
    <html>
        <head>
            <title> Histogram </title>
        </head>
    <body>
    Sample text: {test}
    <br>
    Histogram of Words: {histogram}
    <br>
    Random words: {random_words}
    <br>
    <button onclick="window.location.href = '/markov/book.txt/5';">Markov Chain example</button>
    <button onclick="window.location.href = '/';">Home</button>
    </body>
    '''

@app.route('/markov/<word_list>/<num>')
def randomized_markov(word_list, num):
    markov_chain = MarkovChain(word_list)
    return f'''
    <html>
        <head>
            <title> Markov Chain </title>
        </head>
    <body>
    Generated words: {markov_chain.walk(int(num))}
    </body>
    <br>
    <button onclick="window.location.href = '/histogram';">Histogram</button>
    <button onclick="window.location.href = '/';">Home</button>
    '''

    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.getenv('PORT', 5000))



