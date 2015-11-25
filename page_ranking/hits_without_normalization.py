from page import Page

class HITS(object):

    def __init__(self, pages = []):
        self.pages = pages

    def iterate(self, times = 1):
        for iteration in range(0, times):
            self.update_auth_values()
            self.update_hub_values()

    def update_auth_values(self):
        for page in self.pages:
            page.auth = 0
            for neighbor in page.incoming_neighbors:
                page.auth += neighbor.hub

    def update_hub_values(self):
        for page in self.pages:
            page.hub = 0
            for neighbor in page.outgoing_neighbors:
                page.hub += neighbor.auth

    def __str__(self):
        representation = ''
        for page in self.pages:
            representation += str(page) + '\n'
        return representation
