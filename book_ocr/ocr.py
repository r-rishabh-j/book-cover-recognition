import easyocr


class BookOCR:
    """
    OCR class to detect text from images
    """

    def __init__(self,):
        self.reader = easyocr.Reader(['en'])

    def loadFile(self, file_path):
        self.result = self.reader.readtext(file_path, paragraph=True)
        for r in self.result:
            print(r[-1])

    def getMetaData(self):
        return self.result

    def largestAreaComponent(self):
        # return title(component with largest area and having less than 25 words)
        max_area = None
        index = -1
        for i, result in enumerate(self.result):
            words = len(str(result[1]).split())
            if words > 25:
                continue
            area = abs(result[0][1][0]-result[0][0][0]) * \
                abs(result[0][2][1]-result[0][1][1])
            if max_area == None or area > max_area:
                max_area = area
                index = i

        if index == -1:
            return index, False

        return index, self.result[index]

    def getTextPart(self, result):
        return result[-1]

    def removeResultAtIndex(self, index):
        self.result.pop(index)
