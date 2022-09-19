# -*- coding: utf-8 -*-
import xml.etree.ElementTree as xml

def query_getDeliveryTarifInfoXML(sndrCtg: int, product: str, mailCat: int, sendMethod: int, weight: int, from_: int, to_: int, contract='', dimension='', value=0, toCountry='', postMark=''):
    xml.register_namespace('soapenv', 'http://schemas.xmlsoap.org/soap/envelope/')
    xml.register_namespace('pos', 'http://webservices.kazpost.kz/postratesws')
    root = xml.Element("{http://schemas.xmlsoap.org/soap/envelope/}Envelope")
    
    header = xml.Element("{http://schemas.xmlsoap.org/soap/envelope/}Header")
    root.append(header)

    body = xml.Element("{http://schemas.xmlsoap.org/soap/envelope/}Body")
    root.append(body)

    GetPostRateRequest = xml.SubElement(body, "{http://webservices.kazpost.kz/postratesws}GetPostRateRequest")
    GetPostRateInfo = xml.SubElement(GetPostRateRequest, "{http://webservices.kazpost.kz/postratesws}GetPostRateInfo")

    SndrCtg = xml.SubElement(GetPostRateInfo, "{http://webservices.kazpost.kz/postratesws}SndrCtg")
    SndrCtg.text = str(sndrCtg)

    Product = xml.SubElement(GetPostRateInfo, "{http://webservices.kazpost.kz/postratesws}Product")
    Product.text = str(product)

    MailCat = xml.SubElement(GetPostRateInfo, "{http://webservices.kazpost.kz/postratesws}MailCat")
    MailCat.text = str(mailCat)

    SendMethod = xml.SubElement(GetPostRateInfo, "{http://webservices.kazpost.kz/postratesws}SendMethod")
    SendMethod.text = str(sendMethod)
    
    Weight = xml.SubElement(GetPostRateInfo, "{http://webservices.kazpost.kz/postratesws}Weight")
    Weight.text = str(weight)
    
    From = xml.SubElement(GetPostRateInfo, "{http://webservices.kazpost.kz/postratesws}From")
    From.text = str(from_)

    To = xml.SubElement(GetPostRateInfo, "{http://webservices.kazpost.kz/postratesws}To")
    To.text = str(to_)

    if (contract):
        Contract = xml.SubElement(GetPostRateInfo, "{http://webservices.kazpost.kz/postratesws}Contract")
        Contract.text = str(contract)

    if (dimension):
        Dimension = xml.SubElement(GetPostRateInfo, "{http://webservices.kazpost.kz/postratesws}Dimension")
        Dimension.text = str(dimension)
    
    if (value):
        Value = xml.SubElement(GetPostRateInfo, "{http://webservices.kazpost.kz/postratesws}Value")
        Value.text = str(value)
    
    if (toCountry):
        ToCountry = xml.SubElement(GetPostRateInfo, "{http://webservices.kazpost.kz/postratesws}ToCountry")
        ToCountry.text = str(toCountry)
    
    if (postMark):
        PostMark = xml.SubElement(GetPostRateInfo, "{http://webservices.kazpost.kz/postratesws}PostMark")
        PostMark.text = str(postMark)

    tree = xml.ElementTree(root)
    stringXml = xml.tostring(tree.getroot(), encoding='unicode', method='xml')
    
    return stringXml
    # tree.write("page.xml",
    #         xml_declaration=True,encoding='utf-8',
    #         method="xml")