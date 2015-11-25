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
