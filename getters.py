# -*- coding: utf-8 -*-
import requests
from parser import parseXmlToJson

def getDeliveryTarifXML(xmlQuery: str, test=False) -> dict:
    url = None
    if (test):
        url = "http://rates.kazpost.kz/postratesws/postratesws.wsdl"
    else:
        url = "http://rates.kazpost.kz/postratesprod/postratesws.wsdl"

    headers = {'content-type': 'text/xml'}
    response = requests.post(url, data = xmlQuery, headers = headers)
    jsonResponse = parseXmlToJson(response.content.decode('utf-8'))

    return jsonResponse
