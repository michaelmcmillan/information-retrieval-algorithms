from math import log

def term_frequency(document, term):
    terms_in_document = document.terms
    term_we_are_searching_for = term.lower()
    occurences = terms_in_document.count(term_we_are_searching_for)
    return 0 if not occurences else 1 + log (occurences) 
