"""
Project:
This program is use to read table data from a pdf file.The create_folder function will create a folder name called'csv'
in the current working directory.
Author: <Hashimabdulla> <hashimabdulla69@gmail.com> , April 18 2020
Version: 0.1
Module: Pdf table data extractor.
"""

import os
import shutil
import camelot

"""This module create folder to save csv files."""

def create_folder(foldername):
    pathaddress = os.getcwd()
    newfolder = pathaddress +"/"+foldername
    foldercheck = os.path.exists(newfolder)
    if foldercheck==False:
        os.mkdir(foldername)
        return "new folder, {} created.".format(foldername)
    else:
        shutil.rmtree(newfolder)
        os.mkdir(foldername)
        return "folder already exist"

"""This module extract data from tables from each pages of input pdf file."""

def pdf_table_reader(file):
    create_folder("csv")
    pathaddress = os.getcwd()
    csv_folder = pathaddress + '/csv'
    tables=camelot.read_pdf(file,pages='all')
    for i in range(tables.n):
        tables[i].to_csv('{}/table_{}.csv'.format(csv_folder,i))
    index = os.listdir(pathaddress + "/csv")
    return index

pdf_table_reader("replace here with your pdffile path.")