from math import sqrt

class Page(object):

    def __init__(self, name):
        self.name = name
        self.auth = 1
        self.hub  = 1
        self.incoming_neighbors = []
        self.outgoing_neighbors = []

    def points_to(self, other_pages):
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

A = Page('A')
B = Page('B')
C = Page('C')
D = Page('D')

A.points_to([C])
B.points_to([A, C, D])
#C.points_to([A])
D.points_to([B])

hits = HITS([A, B, C, D])
hits.iterate(times = 1)

print A.auth
#assert A.auth == 1
#assert B.auth == 1
#assert C.auth == 1
#assert D.auth == 1
