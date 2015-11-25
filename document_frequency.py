from term_frequency import term_frequency

def document_frequency(document_collection, term):
    occurences = [term_frequency(document, term) > 0
                  for document in document_collection]
    return occurences.count(True)
