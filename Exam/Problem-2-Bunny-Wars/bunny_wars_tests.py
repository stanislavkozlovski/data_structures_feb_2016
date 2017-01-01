import unittest
from bunny_wars import BunnyWars


class BunnyWarsAddBunnyTests(unittest.TestCase):
    def setUp(self):
        self.wars = BunnyWars()

    def test_add_bunny_to_a_non_existing_room(self):
        """ Should throw an exception"""
        with self.assertRaises(Exception):
            self.wars.add_bunny("Ivo", 0, 15)

    def test_add_bunny_with_an_existing_name(self):
        """ Should throw an exception """
        self.wars.add_room(15)
        self.wars.add_bunny("Ivo", 0, 15)
        with self.assertRaises(Exception):
            self.wars.add_bunny("Ivo", 0, 15)

    def test_add_bunny_with_negative_team_id(self):
        """ Should throw an exception """
        self.wars.add_room(15)
        with self.assertRaises(Exception):
            self.wars.add_bunny("Ivo", -1, 15)

    def test_add_bunny_with_an_incorrect_team_id(self):
        """ Should throw an exception """
        self.wars.add_room(15)
        with self.assertRaises(Exception):
            self.wars.add_bunny("Ivo", 5, 15)

    def test_add_bunny_with_no_bunnies_should_increase_count(self):
        self.wars.add_room(15)

        self.assertEqual(self.wars.bunny_count(), 0)

        self.wars.add_bunny("Ivo", 1, 15)

        self.assertEqual(self.wars.bunny_count(), 1)

    def test_add_bunny_with_existing_bunnies_should_increase_count(self):
        self.wars.add_room(15)
        self.wars.add_bunny("Ivo", 1, 15)
        self.wars.add_bunny("Andre", 1, 15)
        self.wars.add_bunny("Heard", 1, 15)
        self.wars.add_bunny("Dall", 1, 15)
        self.wars.add_bunny("Puddle", 1, 15)

        self.assertEqual(self.wars.bunny_count(), 5)
        self.wars.add_bunny('Turn', 2, 15)
        self.assertEqual(self.wars.bunny_count(), 6)

    def test_add_bunny_with_no_bunnies(self):
        """ Should add the bunny with correct parameters """
        bunny_name = "Dal"
        bunny_team = 3
        bunny_room = 15
        bunny_health = 100
        bunny_score = 0
        self.wars.add_room(bunny_room)
        self.wars.add_bunny(bunny_name, bunny_team, bunny_room)

        bunnies = self.wars.list_bunnies_by_team(bunny_team)
        result_bunny = next(bunnies)

        self.assertEqual(result_bunny.name, bunny_name)
        self.assertEqual(result_bunny.team, bunny_team)
        self.assertEqual(result_bunny.room, bunny_room)
        self.assertEqual(result_bunny.health, bunny_health)
        self.assertEqual(result_bunny.score, bunny_score)


if __name__ == '__main__':
    unittest.main()