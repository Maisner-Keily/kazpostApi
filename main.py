import json
from flask import Flask, request, make_response

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET', 'POST'])
def index():
    print(request.data)

    return make_response({'sad': 'sad'})


if (__name__ == "__main__"):
    app.run(host="109.68.212.121", port=80)
