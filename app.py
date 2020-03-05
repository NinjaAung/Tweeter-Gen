from dictogram import Dictogram

from flask import Flask
app = Flask(__name__)
test = "one fish two fish red fish blue fish"

@app.route('/')
def randomized_word():
    histogram = Dictogram(test.split())
    random_words = ""
    n = "\n"
    for _ in range(0, histogram.tokens):
        random_words += f' {histogram.sample()}'
    return f'Sample text: {test}|Histogram of Words: {histogram}|Random words: {random_words}'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.getenv('PORT', 5000))



