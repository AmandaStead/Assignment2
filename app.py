import random

from flask import Flask, request, jsonify, make_response

app = Flask(__name__)


@app.route('/joke/')
def joke():
    jokes = [
        {"Joke1": "I’ve got this disease where I can’t stop making airport puns. The doctor says it terminal."},
        {"Joke2": "Why are mummy's scared of vacation? They're afraid to unwind."},
        {"Joke3": "Want to hear a chimney joke? Got stacks of em! First ones on the house"},
        {"Joke4": "Want to hear my pizza joke? Never mind, its too cheesy."},
        {"Joke5": "What’s the difference between an African elephant and an Indian elephant? About 5000 miles."},
        {"Joke6": "A red and a blue ship have just collided in the Caribbean. Apparently the survivors are marooned."},
        {"Joke7": "Have you heard the rumor going around about butter? Never mind, I shouldn't spread it."},
        {"Joke8": "How are false teeth like stars? They come out at night!"},
        {"Joke9": "'Ill call you later.' Don't call me later, call me Dad."},
        {"Joke10": "what happens when you cross a sheep with a kangaroo ? A woolly jumper!"},
        {"Joke11": "What did the Red light say to the Green light? Don't look at me I'm changing!"}
    ]

    return random.choice(jokes)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

