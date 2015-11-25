import unittest
from page_ranking.hits_without_normalization import Page, HITS

class TestHitsWithoutNormalization(unittest.TestCase):

    def test_page_should_have_a_default_hub_of_1(self):
        page = Page('A')
        self.assertEquals(page.hub, 1)

    def test_page_should_have_a_default_auth_of_1(self):
        page = Page('A')
        self.assertEquals(page.auth, 1)

    def test_outgoing_neighbors_contains_neighbors_being_pointed_to(self):
        first_page = Page('A')
        second_page = Page('B')
        first_page.points_to([second_page])
        self.assertEquals(first_page.outgoing_neighbors[0], second_page)

    def test_page_can_not_point_to_itself(self):
        first_page = Page('A')
        first_page.points_to([first_page])
        self.assertEquals(first_page.outgoing_neighbors, [])
        self.assertEquals(first_page.incoming_neighbors, [])

    def test_page_being_pointed_to_gets_an_incoming_neighbor(self):
        first_page = Page('A')
        second_page = Page('B')
        first_page.points_to([second_page])
        self.assertEquals(second_page.incoming_neighbors[0], first_page)

    def test_hub_to_page_pointing_to_another_page_is_one_on_first_iteration(self):
        first_page = Page('A')
        second_page = Page('B')
        first_page.points_to([second_page])
        HITS([first_page, second_page]).iterate(times = 1)
        self.assertEquals(first_page.hub, 1)

    def test_hub_to_page_pointing_to_two_pages_is_two_on_first_iteration(self):
        first_page = Page('A')
        second_page = Page('B')
        third_page = Page('C')
        first_page.points_to([second_page, third_page])
        HITS([first_page, second_page, third_page]).iterate(times = 1)
        self.assertEquals(first_page.hub, 2)

    def test_hub_to_page_being_pointed_to_by_no_pages_is_0_on_first_iteration(self):
        first_page = Page('A')
        HITS([first_page]).iterate(times = 1)
        self.assertEquals(first_page.hub, 0)

    def test_auth_to_page_being_pointed_to_by_no_pages_is_0_on_first_iteration(self):
        first_page = Page('A')
        HITS([first_page]).iterate(times = 1)
        self.assertEquals(first_page.auth, 0)
