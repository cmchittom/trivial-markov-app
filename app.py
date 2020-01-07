from flask import Flask, jsonify, request
import markovify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/', methods=['POST'])
def make_sentence():
    # Needs to be supplied by Slack
    verification_token = ''
    if request.form['token'] == verification_token:
        slack_response_type = 'in_channel'

        corpus_html = requests.get(
            'https://www.gutenberg.org/files/100/100-h/100-h.htm').text
        corpus_parsed = BeautifulSoup(corpus_html, 'html.parser')
        corpus_text = corpus_parsed.get_text()
        corpus_markovified = markovify.Text(corpus_text)
        new_sentence = corpus_markovified.make_sentence()

        return jsonify(response_type=slack_response_type,
                       text=new_sentence)
    else:
        return 'No', 403
