from math import log  
from document_frequency import document_frequency

def inverse_document_frequency(document_collection, term):
    N = len(document_collection)
    dt = document_frequency(document_collection, term)
    return log(N/dt)
