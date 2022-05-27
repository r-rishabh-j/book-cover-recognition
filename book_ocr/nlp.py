import en_core_web_trf


class NLP:
    """
    NLP class to determine nature of detected text
    """

    def __init__(self):
        self.nlp = en_core_web_trf.load()

    def processText(self, text):
        """
        Extract person and org
        """
        doc = self.nlp(text)
        result = {
            "PERSON": [],
            "ORG": []
        }

        for token in doc.ents:
            if token.label_ == 'PERSON':
                result['PERSON'].append(token)
            elif token.label_ == 'ORG':
                result['ORG'].append(token)

        return result
