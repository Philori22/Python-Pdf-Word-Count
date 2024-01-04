#!/usr/bin/env python3
# word_count.py: A script to count words in a PDF file.
# This script is an updated version based on the original work by adityashrm21
# Original Repository: https://github.com/adityashrm21/Pdf-Word-Count/tree/master


import os
import sys
import re
import time
import PyPDF2

def getPageCount(pdf_file):
    """
    Returns the total number of pages in the given PDF file.
    """
    with open(pdf_file, 'rb') as pdfFileObj:
        pdfReader = PyPDF2.PdfReader(pdfFileObj)
        pages = len(pdfReader.pages)
        return pages

def extractData(pdf_file, page):
    """
    Extracts text from a given page in the PDF file.
    """
    with open(pdf_file, 'rb') as pdfFileObj:
        pdfReader = PyPDF2.PdfReader(pdfFileObj)
        pageObj = pdfReader.pages[page]
        data = pageObj.extract_text()
        return data

def getWordCount(data):
    """
    Returns the word count of the given text data.
    """
    data = data.split()
    return len(data)
    
def main():
    """
    Main function to handle command-line arguments and execute word counting.
    """
    if len(sys.argv) < 2:
        print('Command usage: python word_count.py FileName StartPage EndPage')
        exit(1)
    else:
        pdfFile = sys.argv[1]
        numPages = getPageCount(pdfFile)

        # Default to the entire document if start and end pages are not provided
        startPage = 0
        endPage = numPages

        if len(sys.argv) == 4:
            startPage = max(int(sys.argv[2]) - 1, 0)  # Pages are 0-indexed
            endPage = min(int(sys.argv[3]), numPages)

        # Check if the specified file exists or not
        try:
            if os.path.exists(pdfFile):
                print("File found!")
        except OSError as err:
            print(err.reason)
            exit(1)

        # Count words in the specified range of pages
        totalWords = 0
        for i in range(startPage, endPage):
            text = extractData(pdfFile, i)
            totalWords += getWordCount(text)

        time.sleep(1)

        print(totalWords)

if __name__ == '__main__':
    main()
