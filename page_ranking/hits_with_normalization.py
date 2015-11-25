from math import sqrt
from page import Page

class HITS(object):

    def __init__(self, pages = []):
        self.pages = pages
        self.normalization = 0

    def iterate(self, times = 1):
        for iteration in range(0, times):
            self.calculate_and_normalize_auth_values()
            self.calculate_and_normalize_hub_values()
            
    def calculate_and_normalize_auth_values(self):
        self.normalization = 0
        self.update_auth_values()
        self.normalization = sqrt(self.normalization)
        self.normalize_auth_values()

    def calculate_and_normalize_hub_values(self):
        self.normalization = 0
        self.update_hub_values()
        self.normalization = sqrt(self.normalization)
        self.normalize_hub_values()

    def normalize_auth_values(self):
        for page in self.pages:
            page.auth = page.auth / self.normalization

    def normalize_hub_values(self):
        for page in self.pages:
            page.hub = page.hub / self.normalization

    def update_auth_values(self):
        for page in self.pages:
            page.auth = 0
            for neighbor in page.incoming_neighbors:
                page.auth += neighbor.hub
                self.normalization += sqrt(page.auth)

    def update_hub_values(self):
        for page in self.pages:
            page.hub = 0
            for neighbor in page.outgoing_neighbors:
                page.hub += neighbor.auth
                self.normalization += sqrt(page.hub)

    def __str__(self):
        representation = ''
        for page in self.pages:
            representation += str(page) + '\n'
        return representation 
