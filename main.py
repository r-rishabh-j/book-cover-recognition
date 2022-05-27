import sys
if len(sys.argv) < 2:
    print(
        f"Usage: python {sys.argv[0]} [path to image or dir containing images] [(optional) output file path with extension xlsx]")
    sys.exit(-1)

from book_ocr import BookMetaData
from book_ocr.spreadsheet_manager import dump_to_xlsx

# process
files = sys.argv[1]
books = BookMetaData(files)
books.extract()
results = books.getFormattedResult()

# dump output
if len(sys.argv) > 2:
    dump_to_xlsx(results=results, file=sys.argv[2])
else:
    dump_to_xlsx(results=results)
