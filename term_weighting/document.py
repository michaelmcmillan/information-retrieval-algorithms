class Document(object):

    def __init__(self, content):
        self.content = content

    @property
    def terms(self):
        return self.extract_terms()

    def extract_terms(self):
        content = self.content.lower()
        content = content.replace('.', '')
        terms = content.split(' ')
        return terms
