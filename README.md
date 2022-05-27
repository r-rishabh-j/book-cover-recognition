
### A. What does this program do?
This program is a CLI tool for extracting metadata from book cover images. The tool takes an image as input and outputs the results to a .xslx or .csv file(as specified by the user). The tool uses OCR with easyocr along with NLP algorithms with spacy library to generate the results.
### B. Description of the program-
The user may input a single image, or a combination of images in a directory. The tool takes the path and figures out on itself whether the input is an image or directory.
For each image, first, the OCR tool processes the image and extracts the text present, along with the bounding boxes. Then, the ISBN number is extracted with a simple search throughout the text. After this, the bounding box with the largest area, and having less than 25 words is considered to be the title of the book.
The author and the publishers are detected using an NLP library called spacy. The remaining text obtained from OCR is run through the NLP pipeline. The pipeline extracts the named entities, i.e a ‘PERSON’ which is an author, and an ‘ORG’, which is a publisher.
The results thus obtained are dumped to an output file.

###  C. Software architecture:
Classes have been used to employ software SOLID principles. 
```
├── book_ocr/
│ ├── __init__.py
│ ├── nlp.py
│ ├── ocr.py
│ └── spreadsheet_manager.py ├── install.txt
├── main.py
└── test_bookocr.py
```

### Description of modules:
The book_ocr module has been created to contain the necessary classes for metadata processing.
1. __init__contains the class BookMetaData which implements the methods required to operate with the OCR and the NLP library.
2. nlp.py contains the class NLP which implements the methods required to extract named entities from the text.
3. ocr.py contains BookOCR class, which is responsible for extracting text from the book image.
4. spreadsheet_manager contains the method to dump output results to a file.

Note: This project was a part of the course CS305 @IIT Ropar

### D. Compile and run:
This program has been developed with python 3.9.12.
1. First, install the dependencies of the program. A file install.txt has been
submitted along with the code containing commands to install the deps.
Run the commands in a python virtual environment.
2. main.py file is the entry point to the program.To run the program, execute:
```
python main.py <path to dir or image> <(optional) output file path with extension>
```
Here <path to dir or image> can be the path to a single image file, or path to a directory containing multiple images.
Path to an output file is optional. By default the output is saved to output.xlsx
