import json
from flask import Flask, request, make_response

from getQuery import query_getDeliveryTarifInfoXML
from getters import getDeliveryTarifXML

app = Flask(__name__)
app.debug = False

@app.route('/api/getDeliveryTarivInfo', methods=['GET', 'POST'])
def index():
    data = json.loads(request.data)
    print(data)
    sndrCtg = data.sndrCtg
    product = data.product
    mailCat = data.mailCat
    sendMethod = data.sendMethod
    weight = data.weight
    fromIndex = data.fromIndex
    toIndex = data.toIndex

    contract, dimension, value, toCountry, postMark = None, None, None, None, None

    try:
        contract = data.contract
    except:
        pass
    
    try:
        dimension = data.dimension
    except:
        pass
    
    try:
        value = data.value
    except:
        pass
    
    try:
        toCountry = data.toCountry
    except:
        pass
    
    try:
        postMark = data.postMark
    except:
        pass
    

    isTest = data.isTestQuery == 1

    xml = query_getDeliveryTarifInfoXML(sndrCtg, product, mailCat, sendMethod, weight, fromIndex, toIndex, contract, dimension, value, toCountry, postMark)

    data = getDeliveryTarifXML(xml, isTest)

    return make_response(data)


if (__name__ == "__main__"):
    app.run(host="109.68.212.121", port=80)
