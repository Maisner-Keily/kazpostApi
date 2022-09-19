from flask import Flask, request, make_response

from getQuery import query_getDeliveryTarifInfoXML
from getters import getDeliveryTarifXML

app = Flask(__name__)
app.debug = False

@app.route('/', methods=['GET', 'POST'])
def index():
    sndrCtg = request.data.sndrCtg
    product = request.data.product
    mailCat = request.data.mailCat
    sendMethod = request.data.sendMethod
    weight = request.data.weight
    fromIndex = request.data.fromIndex
    toIndex = request.data.toIndex

    contract, dimension, value, toCountry, postMark = None, None, None, None, None

    try:
        contract = request.data.contract
    except:
        pass
    
    try:
        dimension = request.data.dimension
    except:
        pass
    
    try:
        value = request.data.value
    except:
        pass
    
    try:
        toCountry = request.data.toCountry
    except:
        pass
    
    try:
        postMark = request.data.postMark
    except:
        pass
    

    isTest = request.data.isTestQuery == 1

    xml = query_getDeliveryTarifInfoXML(sndrCtg, product, mailCat, sendMethod, weight, fromIndex, toIndex, contract, dimension, value, toCountry, postMark)

    data = getDeliveryTarifXML(xml, isTest)

    return make_response(data)


if (__name__ == "__main__"):
    app.run(host="109.68.212.121", port=80)
