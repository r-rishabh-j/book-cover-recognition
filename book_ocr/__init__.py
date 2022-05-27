from .ocr import BookOCR
from .nlp import NLP
import os
from fuzzywuzzy import fuzz, process


class BookMetaData:
    """
    Class to extract metadata from images
    """

    def __init__(self, path):
        self.path = path
        self.ocr = BookOCR()  # ocr object
        self.nlp = NLP()  # nlp object
        self.files = []  # file store
        # extract images
        if os.path.isdir(path):
            for file in os.listdir(path):
                self.files.append(os.path.abspath(os.path.join(path, file)))
        else:
            self.files.append(os.path.abspath(path))

    def getFormattedResult(self):
        """
        Method to get formatted output to dump to xlsx or csv file.
        Run extract() method first
        """
        for i, result in enumerate(self.results):
            authors = ''
            publishers = ''
            total_authors = len(result['authors'])
            if total_authors == 1:
                authors = result['authors'][0]
            else:
                for j, author in enumerate(result['authors']):
                    authors += str(author)
                    if j < total_authors-1:
                        authors += ', '
            self.results[i]['authors'] = authors

            total_publishers = len(result['publishers'])
            if total_publishers == 1:
                publishers = result['publishers'][0]
            else:
                for j, publisher in enumerate(result['publishers']):
                    publishers += str(publisher)
                    if j < total_publishers-1:
                        publishers += ', '
            self.results[i]['publishers'] = publishers

        return self.results

    def __personAdded(self, array, key):
        for person in array:
            if fuzz.ratio(str(person).lower(), str(key).lower()) > 95:
                return True
        return False

    def extract(self):
        """
        Run analysis algorithm on input
        """
        self.results = []
        """
        Format:
        [
            {
                "title": "title",
                "authors": "a1, a2",
                "publishers": "publisher",
                "isbn": "isbn"
            },
        ]
        """
        for file in self.files:
            print('File: ', file)
            self.results.append({
                "title": None,
                "authors": [],
                "publishers": [],
                "isbn": None,
            })
            self.ocr.loadFile(file_path=file)
            sections = self.ocr.getMetaData()
            for idx, section in enumerate(sections):
                """
                First, extract ISBN number if found
                """
                text: str = section[-1]
                isbn_loc = text.lower().find('isbn')
                if isbn_loc != -1:
                    res = 'ISBN '
                    i = 4
                    while isbn_loc+i < len(text) and text[isbn_loc+i] == ' ':
                        i += 1
                    if isbn_loc+i < len(text) and text[isbn_loc+i].isdigit():
                        while isbn_loc+i < len(text) and (text[isbn_loc+i].isdigit() or not text[isbn_loc+i].isalpha()):
                            res += text[isbn_loc+i]
                            i += 1
                    self.results[-1]['isbn'] = res
                    self.ocr.removeResultAtIndex(idx)
                    break

            """
            Extract title, which occupies largest area on the book
            """
            idx, title = self.ocr.largestAreaComponent()
            if idx != -1:
                self.results[-1]['title'] = self.ocr.getTextPart(title)
                self.ocr.removeResultAtIndex(idx)
            # get authors and publishers here
            for section in sections:
                """
                Extract authors and publishers
                """
                text: str = section[-1]
                nlp_processed = self.nlp.processText(text)

                # author
                for author in nlp_processed['PERSON']:
                    if not self.__personAdded(self.results[-1]['authors'], author):
                        self.results[-1]['authors'].append(author)
                # publishers
                for author in nlp_processed['ORG']:
                    if not self.__personAdded(self.results[-1]['publishers'], author):
                        self.results[-1]['publishers'].append(author)

            print(self.results[-1])

        return self.results
