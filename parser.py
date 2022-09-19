import xmltodict, json

def parseXmlToJson(XML: str) -> dict:
    dictStr = xmltodict.parse(XML)
    resultDict = json.dumps(dictStr)

    return resultDict