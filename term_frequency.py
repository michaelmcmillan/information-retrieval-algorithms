def term_frequency(document, term):
    content = document.content.replace('.', '')

    term = term.lower()
    content = content.lower()
    terms_in_document = content.split(' ')

    return terms_in_document.count(term)
