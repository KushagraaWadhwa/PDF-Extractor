import PyPDF2
from PyPDF2 import PdfReader
import os
import pandas as pd
from pathlib import Path
import csv
import openpyxl
from csv import reader,DictReader
import glob

path=(r"C:\Users\KushagraWadhwa\Desktop\PDFextract\ALLpdf")

filenames=os.listdir(path)
for filename in filenames:
    x=path+ "\\"+filename
 
 #<--------------------------------------------------------------------------------------------------------------------------------->   
    
    reader=PdfReader(x)               #creating an object 'reader'
    num=len(reader.pages)
    
    with open(filename+".txt","w") as output_file:
        
        text=''
        for page in reader.pages:
            text+=page.extract_text()              #extract_text() is a defined method in PyPDF2 class, to extract text from the pdf.
        output_file.write(text)

# #<--------------------------------------------------------------------------------------------------------------------------------->
os.chdir(r"C:\Users\KushagraWadhwa\Desktop\PDFextract")
req_files=glob.glob('*txt')                  #puts all the files ending with txt in a list


print(req_files)
                
#--------------------------------------------------TYPE-1--------------------------------------------------------------------
# with open(r'C:\Users\KushagraWadhwa\Desktop\PDFextract\E_Ticket1.pdf.txt', 'r') as file1:
#     LINES = file1.readlines()
    
#     # for index,val in enumerate(LINES):                        TO CHECK REQUIRED DATA AT WHICH LINE NUMBER
#     #     print(index,val)

# dict1={'COMPANY_NAME':LINES[58],'COMPANY_GSTIN':LINES[57],'PNR':LINES[13],'BOOKING_REF_NO':LINES[16],'DEPARTURE':LINES[26],'ARRIVAL':LINES[31],'PASSENGER_NAME'=LINES[2],'GST_EMAIL':LINES[60],'ACTUAL_PRICE':LINES[70],'AMOUNT_PAID':LINES[73]}
# for key in dict1:
#     print(key+":-"+dict1[key])
    
#------------------------------------------------------------------------------------------------------------------------------
with open(r'C:\Users\KushagraWadhwa\Desktop\PDFextract\E_Ticket3.pdf.txt', 'r') as file2:
    LINES = file2.readlines()
    # for index,val in enumerate(LINES):                       
    #     print(index,val)

dict1={"COMPANY_NAME": LINES[17],

                 "STATE": LINES[2],

                 "COMPANY_GSTN": "null",

                  "INVOICE_SOURCE": "null",

                  "SUPPLIER_NAME": LINES[0],

                 "SUPPLIER_ADDRESS": LINES[1],

                  "SUPPLIER_CITY":LINES[2],

                  "SUPPLIER_CITY_PINCODE": "null",

                 "SITE_NAME": "null",

                  "SITE_STATE_CODE": "null",

                  "SITE_STATE": "null",

                 "SITE_GSTIN": "null",

                  "INVOICE_TYPE":"null",

                  "SUPPLIER_INVOICE_NO": "null",

                 "SUPPLIER_INVOICE_DATE": "null",

                  "QTY":"null",

                  "UOM": "null",

                  "UNIT_PRICE": "null",

                 "SUPPLIER_TAXABLE_VALUE_INR": LINES[25][38:45]+LINES[26][34:40],

                  "CGST_RATE": LINES[25][54:60],

                 "CGST_AMT":LINES[25][61:67],

                  "SGST_RATE": LINES[25][68:],

                  "SGST_AMT": LINES[25][75:],

                 "IGST_RATE": "NULL",

                  "IGST_AMT": "null",

                  "IRN_CODE": "null",

                  "EINV_STATUS": "null",

                 "IRN_CREATION_DATE": "null",

                  "INVOICE_AMOUNT_INR": LINES[27][52:],

                  "INVOICE_CURRENCY_CODE": "null",

                 "INVOICE_AMOUNT": LINES[28][50:],

                  "HSNSAC_CODE": "null",

                  "ITEM_DESCRIPTION":LINES[31:34]}

df=pd.DataFrame(data=dict1)

df.to_excel("type2.xlsx",index=False)


        
        
