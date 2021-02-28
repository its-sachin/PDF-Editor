from PyPDF2 import PdfFileReader, PdfFileWriter
import os,shutil

file_path = input('Please write the path of file: ')
startpt = int(input("Start page number : "))
endpt = int(input("End page number : "))

folder_path = file_path[:file_path.rindex("\\")]



def pdf_cutter(folder_path,startpt,endpt):
    os.chdir(folder_path[1:])

    inputpdf = PdfFileReader(open(file_path[1:-1], "rb"))
    output = PdfFileWriter()
    for i in range(startpt,endpt):
        output.addPage(inputpdf.getPage(i-1))

    output_name = input("Please write the output name: ")

    with open(output_name +".pdf", "wb") as outputStream:
                output.write(outputStream)        

pdf_cutter(folder_path, startpt, endpt)