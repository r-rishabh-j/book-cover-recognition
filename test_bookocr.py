from pytest import fixture
from book_ocr import BookMetaData
from book_ocr.spreadsheet_manager import dump_to_xlsx

def test_dir():
    files = './pics'
    books = BookMetaData(files)
    books.extract()
    results = books.getFormattedResult()
    dump_to_xlsx(results, file='./outtest1.xlsx')
    dump_to_xlsx(results, file='./outtest1.csv')
    
def test_file():
    files = './pics/test10.png'
    books = BookMetaData(files)
    books.extract()
    results = books.getFormattedResult()
    dump_to_xlsx(results, file='./outtest2.xlsx')
    dump_to_xlsx(results, file='./outtest2.csv')