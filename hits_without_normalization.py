class Page(object):

    def __init__(self, name):
        self.name = name
        self.auth = 1
        self.hub  = 1
        self.incoming_neighbors = []
        self.outgoing_neighbors = []

    def points_to(self, other_pages):
        other_pages = [page for page in other_pages if page != self]
        for other_page in other_pages:
            other_page.incoming_neighbors.append(self)
            self.outgoing_neighbors.append(other_page)

    def __str__(self):
        return '{0}: Auth = {1}. Hub = {2}'.format(
            self.name, self.auth, self.hub
        )

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
