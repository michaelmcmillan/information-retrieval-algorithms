import unittest
from document import Document
from document_frequency import document_frequency

class TestDocumentFrequency(unittest.TestCase):

    def test_DF_of_a_term_not_mentioned_in_any_documents_is_zero(self):
        document_collection = []
        term = 'sweden'
        self.assertEquals(document_frequency(document_collection, term), 0)

    def test_DF_of_a_term_mentioned_in_two_different_documents_is_two(self):
        document_collection = [Document('Sweet Norway.'), Document('Hei Norway.')]
        term = 'norway'
        self.assertEquals(document_frequency(document_collection, term), 2)

    def test_DF_mentioned_four_times_in_three_different_documents_is_three(self):
        document_collection = [
            Document('sweden sweden'), Document('sweden'), Document('sweden')
        ]
        term = 'sweden'
        self.assertEquals(document_frequency(document_collection, term), 3)
