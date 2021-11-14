import os
from SchemaValidator import SchemaValidator
from SyntaxValidator import SyntaxValidator

class Controller:
    def __init__(self):
         self.XML_DIR = os.getcwd() + '\\XML\\UBL\\'

    def validateFiles(self):

        schemaValidator = SchemaValidator()
        syntaxValidator = SyntaxValidator()

        # The directory with XML files
        for file_name in os.listdir(self.XML_DIR):
            schV = 0
            synV = 0
            pepV = 0
            print('{}: '.format(file_name), end='')

            file_path = '{}/{}'.format(self.XML_DIR, file_name)
            schemaValidator.setDocType('INV')
            if schemaValidator.validate(file_path):
                #print('Valid')
                schV = 1
            else:
                #print('Not valid')
                schV = 0
            syntaxValidator.generateOutputFile(file_path, 'UBL')
            if syntaxValidator.validate('UBL'):
                #print('Valid')
                synV = 1
            else:
                #print('Not valid')
                synV = 0

            syntaxValidator.generateOutputFile(file_path, 'PEPPOL')
            if syntaxValidator.validate('PEPPOL'):
                #print('Valid')
                peppolV = 1
            else:
                #print('Not valid')
                peppolV = 0

            if (schV == 1 & synV == 1 & peppolV == 1):
                print('Valid')
            else:
                print('Invalid')

        