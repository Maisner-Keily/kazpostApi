import json
from flask import Flask, request, make_response

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET', 'POST'])
def index(response):
    data = response.body
    with open('./logs.txt', 'a', encoding='utf-8') as fl:
        fl.write("getted")

    return make_response('sad', status_code=200)


if (__name__ == "__main__"):
    app.run(port=8000)