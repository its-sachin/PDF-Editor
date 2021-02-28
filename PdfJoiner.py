from PyPDF2 import PdfFileReader, PdfFileWriter
import os,shutil

folder_path = input('Please write the path of folder: ')
startpt = int(input("Start page number : "))
endpt = int(input("End page number : "))



def pdf_cutter(folder_path,startpt,endpt):
    os.chdir(folder_path)

    inputpdf = PdfFileReader(open("Fundamentals of Digital Logic with Verilog Design by Stephen Brown, Zvonko Vranesic (z-lib.org).pdf", "rb"))
    output = PdfFileWriter()
    for i in range(startpt,endpt):
        output.addPage(inputpdf.getPage(i-1))

    with open("COL215(3).pdf", "wb") as outputStream:
                output.write(outputStream)        

pdf_cutter(folder_path, startpt, endpt)