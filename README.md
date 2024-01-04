# Word Count in PDF

A simple Python script to count the number of words in a PDF file, updated and modified from the original version by [adityashrm21](https://github.com/adityashrm21/Pdf-Word-Count/tree/master). It can process the entire document or a specific range of pages.

## Prerequisites

To use this script, you need Python installed on your system along with the PyPDF2 library. If you don't have PyPDF2 installed, you can install it via pip:

```bash
pip install PyPDF2
```

# Usage
To run the script, navigate to the directory containing the script and execute it using Python from the command line. You can specify the PDF file along with optional start and end pages.

* Count words in the entire document:
```bash
python3 word_count.py path/to/pdf
```

* Count words in a specific range of pages, i.e. from start to finish (e.g., pages 15 to 134):
```bash
python3 word_count.py path/to/pdf 15 134
```

# Notes
* Ensure the path to the PDF file is correct.
* The page numbers are 1-indexed, just like in most documents, it looks at the index of the page in the pdf document, not the page number on the document.

# Acknowledgements
This script is an updated version of the original work found at [[https://github.com/adityashrm21/Pdf-Word-Count/tree/master](adityashrm21's Pdf-Word-Count).
