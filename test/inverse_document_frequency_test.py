import unittest
from document import Document
from inverse_document_frequency import inverse_document_frequency

class TestInverseDocumentFrequency(unittest.TestCase):

    def test_is_high_when_the_term_is_rare(self):
        document_collection = [
            Document('this document contains the rare term'),
            Document('this document does not contain it'),
            Document('neither does this one'),
            Document('or this one'),
            Document('not even this one'),
            Document('my god, just one document contains it'),
            Document('out of 10 documents, only one contains it'),
            Document('i am not looking forward to my exam'),
            Document('on the other hand, it is not so bad'),
            Document('no it definetely is'),
        ]
        term = 'rare'
        idf = inverse_document_frequency(document_collection, term)
        self.assertEquals(idf, 2.302585092994046)

    def test_is_low_when_the_term_is_common(self):
        document_collection = [
            Document('this *beep* contains the rare term'),
            Document('this document does not contain it'),
            Document('neither does this document one'),
            Document('or this document'),
            Document('not even this document'),
            Document('my god, just one document contains it'),
            Document('out of 10 documents, only document contains it'),
            Document('i am not looking forward to my exam. document'),
            Document('on the other hand, it is not so bad. document'),
            Document('no it definetely is. document'),
        ]
        term = 'document'
        idf = inverse_document_frequency(document_collection, term)
        self.assertEquals(idf, 0)
