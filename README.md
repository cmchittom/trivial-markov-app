# A Trivial Markov App

## About
I wanted a web service that grabs another web page, and uses it as a corpus for a single Markov-chain generated sentence for a joke [Slack  slash command](https://api.slack.com/slash-commands).

This repository is mostly so that when it inevitably breaks somehow, the code is still around so I don't have to rewrite it. 

## Installation
1. Put `app.py` somewhere the webserver can read it.
2. Edit `app.py` to specify the verification token and corpus page. Note that the use of verification tokens has been deprecated by Slack, so this will probably eventually break.
3. Install the modules (probably in a virtualenv)
4. [Deploy it somewhere](http://flask.pocoo.org/docs/1.0/deploying/#deployment)
