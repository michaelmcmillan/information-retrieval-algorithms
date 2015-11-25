import unittest

from document import Document 
from term_frequency import term_frequency

class TestTermFrequency(unittest.TestCase):

    def test_TF_of_a_term_not_mentioned_is_zero(self):
        document = Document('I live in norway.')
        term = 'sweden'
        self.assertEquals(term_frequency(document, term), 0)

    def test_TF_of_a_term_mentioned_smushed_up_many_times_is_zero(self):
        document = Document('norwaynorwaynorway')
        term = 'norway'
        self.assertEquals(term_frequency(document, term), 0)

    def test_TF_of_a_term_mentioned_once_is_one(self):
        document = Document('I live in norway.')
        term = 'norway'
        self.assertEquals(term_frequency(document, term), 1)

    def test_IF_is_not_case_insensitive_on_content(self):
        document = Document('I live in Norway.')
        term = 'norway'
        self.assertEquals(term_frequency(document, term), 1)

    def test_IF_is_not_case_insensitive_on_query(self):
        document = Document('I live in norway.')
        term = 'Norway'
        self.assertEquals(term_frequency(document, term), 1)

    def test_TF_of_a_term_mentioned_twice_is_two(self):
        document = Document('I live in norway. I like norway.')
        term = 'norway'
        self.assertEquals(term_frequency(document, term), 2)
