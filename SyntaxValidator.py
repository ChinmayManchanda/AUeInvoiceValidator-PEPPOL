import os
import time
from os import path
import xml.etree.ElementTree as ET
        

class SyntaxValidator:

    def __init__(self):
        self.SRC_UBL_PATH = (os.getcwd() + '\\SyntaxValidation\\AUNZ-UBL-validation.xsl')
        self.SRC_PEPPOL_PATH = (os.getcwd() + '\\SyntaxValidation\\PEPPOL-validation.xsl')
        self.SRC_UBL_OUT_PATH = (os.getcwd() + '\\SyntaxValidation\\Output\\UBL\\')
        self.SRC_PEPPOL_OUT_PATH = (os.getcwd() + '\\SyntaxValidation\\Output\\PEPPOL\\')
        
        self.NODE_FAILED_ASSERT = '{http://purl.oclc.org/dsdl/svrl}failed-assert'
        self.NODE_FAILED_TEXT = '{http://purl.oclc.org/dsdl/svrl}text'
        
    def generateOutputFile(self, xml_path, validation):
        self.SRC_UBL_OUT_PATH = (os.getcwd() + '\\SyntaxValidation\\Output\\UBL\\')
        self.SRC_PEPPOL_OUT_PATH = (os.getcwd() + '\\SyntaxValidation\\Output\\PEPPOL\\')
        head, file_name = os.path.split(xml_path)
        file_name = file_name.rsplit('.', 1)[0]
        
        timestr = time.strftime("%Y%m%d-%H%M%S")
        self.SRC_UBL_OUT_PATH =  self.SRC_UBL_OUT_PATH + file_name +  timestr +'.xml'
        self.SRC_PEPPOL_OUT_PATH =  self.SRC_PEPPOL_OUT_PATH + file_name +  timestr +'.xml'
        import sys
        #sys.path.append("C:\Program Files\Saxonica\SaxonHEC1.2.1\Saxon.C.API\python-saxon")
        sys.path.append("\\Saxonica\\SaxonHEC1.2.1\\Saxon.C.API\\python-saxon")
        
        import saxonc
        
        proc = saxonc.PySaxonProcessor(license=False)
        
        xslt30_processor = proc.new_xslt30_processor()

        xslt30_processor.transform_to_file(source_file=xml_path, 
                                           stylesheet_file=self.SRC_UBL_PATH if validation == 'UBL' else self.SRC_PEPPOL_PATH,
                                           output_file=self.SRC_UBL_OUT_PATH if validation == 'UBL' else self.SRC_PEPPOL_OUT_PATH)



    def validate(self, validation) -> bool:
        output_file=self.SRC_UBL_OUT_PATH if validation == 'UBL' else self.SRC_PEPPOL_OUT_PATH
        tree = ET.parse(output_file)
        root = tree.getroot()
        passresult = 1
        for nodes in root.findall(self.NODE_FAILED_ASSERT):
            node = nodes.find(self.NODE_FAILED_TEXT).text
            print(node)
            passresult = 0

        return passresult == 1
    
    
        
        
        
