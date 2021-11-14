import xml.etree.ElementTree as ET

import os
import xml.etree.ElementTree as ET

class Adapter:
    def __init__(self):
        self.XML_DIR = os.getcwd() + '\\UBL\\'
        

# The directory with XML files
    def convertFiles(self):
        for file_name in os.listdir(self.XML_DIR):
            file_path = '{}/{}'.format(self.XML_DIR, file_name)

            tree = ET.parse(file_path)
            root = tree.getroot()

            custom =root.findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}CustomizationID')
            for node in custom:
                if(node.text != None):
                    node.text = 'urn:cen.eu:en16931:2017#conformant#urn:fdc:peppol.eu:2017:poacc:billing:international:aunz:3.0'


            elementpro = root.makeelement('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ProfileID', {})
            elementpro.text = 'urn:fdc:peppol.eu:2017:poacc:billing:01:1.0'
            root.insert(2, elementpro)



            elementDD = root.makeelement('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}DueDate', {})
            elementDD.text = '2021-10-29'
            root.insert(5, elementDD)



            for asp in tree.findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}AccountingSupplierParty'):
                aaids = asp.findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}AdditionalAccountID')
                if(aaids):
                    asp.remove((aaids[0]))
                partys = asp.findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}Party')
                eps = partys[0].findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}EndpointID')
                eps[0].set('schemeID', '0151')
                eps[0].text = '47555222000'

                ptss = partys[0].findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PartyTaxScheme')
                cids = ptss[0].findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}CompanyID')
                cids[0].text = '47555222000'

                tss = ptss[0].findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxScheme')
                ids = tss[0].findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID')
                ids[0].text = 'GST'

                elements = partys[0].makeelement('{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PostalAddress', {})
                partys[0].insert(2, elements)
                sname = elements.makeelement('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}StreetName', {})
                sname.text = 'Main Street 1'
                elements.append(sname)

                cname = elements.makeelement('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}CityName', {})
                cname.text = 'Harrison'
                elements.append(cname)

                pname = elements.makeelement('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}PostalZone', {})
                pname.text = '2912'
                elements.append(pname)

                ctname = elements.makeelement('{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}Country', {})
                elements.append(ctname)

                idname = ctname.makeelement('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}IdentificationCode', {})
                idname.text = 'AU'
                ctname.append(idname)


                ples = partys[0].findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PartyLegalEntity')
                cid = ples[0].makeelement('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}CompanyID', {})
                cid.set('schemeID', '0151')
                cid.text = '47555222000'
                ples[0].append(cid)


                ples = partys[0].findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PartyLegalEntity')
                clf = ples[0].findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}CompanyLegalForm')
                textValue = clf[0].text
                ples[0].remove(clf[0])

                clfc = ples[0].makeelement('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}RegistrationName', {})

                clfc.text = textValue
                ples[0].insert(0, clfc)


            for acp in tree.findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}AccountingCustomerParty'):
                aaidc = acp.findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}AdditionalAccountID')
                if (aaidc):
                    acp.remove((aaidc[0]))
                partyc = acp.findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}Party')
                epc = partyc[0].findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}EndpointID')
                epc[0].set('schemeID', '0151')
                epc[0].text = '91888222000'

                ptsc = partyc[0].findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PartyTaxScheme')
                cidc = ptsc[0].findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}CompanyID')
                cidc[0].text = '91888222000'

                tsc = ptsc[0].findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxScheme')
                idc = tsc[0].findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID')
                idc[0].text = 'GST'

                elementc = partyc[0].makeelement('{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PartyLegalEntity', {})
                partyc[0].append(elementc)
                rname = elementc.makeelement('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}RegistrationName', {})
                rname.text = 'Buyer Official Name'
                elementc.append(rname)

                cidc = elementc.makeelement('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}CompanyID', {})
                cidc.set('schemeID', '0151')
                cidc.text = '91888222000'
                elementc.append(cidc)



            for acpt in tree.findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxRepresentativeParty'):
                elementct = acpt.makeelement('{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PartyName', {})
                acpt.insert(0, elementct)
                rnamet = elementct.makeelement('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Name', {})
                rnamet.text = 'Mr Wilson'
                elementct.append(rnamet)

                ptsct = acpt.findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PartyTaxScheme')
                cidct = ptsct[0].findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}CompanyID')
                cidct[0].text = '47555222000'

                tsct = ptsct[0].findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxScheme')
                idct = tsct[0].findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID')
                idct[0].text = 'GST'


            for delvd in tree.findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}Delivery'):
                dlocd = delvd.findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}DeliveryLocation')
                addrd = dlocd[0].findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}Address')

                elementcd = addrd[0].makeelement('{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}Country', {})

                addrd[0].append(elementcd)
                icoded = elementcd.makeelement('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}IdentificationCode', {})
                icoded.text = 'AU'
                elementcd.insert(0, icoded)

                dpd = delvd.findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}DeliveryParty')
                pld = dpd[0].findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PartyIdentification')
                dpd[0].remove(pld[0])


            for pt in tree.findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}PaymentTerms'):

                root.remove(pt)



            for taxtotalt in tree.findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxTotal'):
                taxamountt = taxtotalt.findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}TaxAmount')
                taxSubTotalt = taxtotalt.findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxSubtotal')
                taxableamountt = taxSubTotalt[0].findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}TaxableAmount')
                taxamountst = taxSubTotalt[0].findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}TaxAmount')
                percentt = taxSubTotalt[0].findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Percent')
                taxCategoryt = taxSubTotalt[0].findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxCategory')
                taxIdt = taxCategoryt[0].findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID')
                taxSchemet = taxCategoryt[0].findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxScheme')
                taxIdst = taxSchemet[0].findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID')
                taxTypeCodet = taxSchemet[0].findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}TaxTypeCode')

                taxSubTotalt[0].remove(percentt[0])

                taxamountt[0].text = str(round(float(taxableamountt[0].text) * 0.1, 2))
                taxamountst[0].text = str(round(float(taxableamountt[0].text) * 0.1, 2))
                taxIdt[0].text = 'S'
                taxIdst[0].text = 'GST'

                pcentt = taxCategoryt[0].makeelement('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Percent', {})
                pcentt.text ='10'
                taxCategoryt[0].insert(1, pcentt)

                taxSchemet[0].remove(taxTypeCodet[0])



            for lmt in tree.findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}LegalMonetaryTotal'):
                lea = lmt.findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}LineExtensionAmount')
                tia = lmt.findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}TaxInclusiveAmount')
                pa = lmt.findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}PayableAmount')

                tia[0].text = str(round(float(lea[0].text) + round(float(lea[0].text) * 0.1, 2), 2))
                pa[0].text = str(round(float(lea[0].text) + round(float(lea[0].text) * 0.1, 2), 2))





            for invoicelinei in tree.findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}InvoiceLine'):
                deliveryi = invoicelinei.findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}Delivery')
                itemi = invoicelinei.findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}Item')
                sidi = itemi[0].findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}StandardItemIdentification')
                idsi = sidi[0].findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID')
                ctci = itemi[0].findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}ClassifiedTaxCategory')
                percenti = ctci[0].findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}Percent')
                taxSchemei = ctci[0].findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2}TaxScheme')
                idtsi = taxSchemei[0].findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID')
                idi = ctci[0].findall('{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID')


                percenti[0].text = '10'
                idtsi[0].text = 'GST'
                idsi[0].set('schemeID', '0002')

                if (idi[0] != None):
                    idi[0].text = 'S'

                invoicelinei.remove(deliveryi[0])




            tree.write(file_path)