import os

from lxml import etree
from lxml.etree import DocumentInvalid
from os.path import isfile, join

class SchemaValidator:

    def __init__(self):
        self.CC_XSD_PATH = (os.getcwd() + '\\SchemaValidation\\UBL-CreditNote-2.1.xsd')
        self.INV_XSD_PATH = (os.getcwd() + '\\SchemaValidation\\UBL-Invoice-2.1V1.xsd')

    def setDocType(self, docType):
        path = self.INV_XSD_PATH if docType == 'INV' else self.CC_XSD_PATH
        xmlschema_doc = etree.parse(path)
        self.xmlschema = etree.XMLSchema(xmlschema_doc)

    def validate(self, xml_path: str) -> bool:
        xml_doc = etree.parse(xml_path)
        try:
            result = self.xmlschema.validate(xml_doc)        
            self.xmlschema.assertValid(xml_doc)
        except DocumentInvalid:
            errors = []
            for error in self.xmlschema.error_log:
                errors.append((error.message, error.line))
                print(errors)
        return result
    
    
