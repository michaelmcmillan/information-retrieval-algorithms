def term_frequency(document, term):
    terms_in_document = document.terms
    term_we_are_searching_for = term.lower()
    return terms_in_document.count(term_we_are_searching_for)
