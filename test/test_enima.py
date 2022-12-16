import unittest

from main import Enima
from main import animals, elements, stats


class TestEnima(unittest.TestCase):
    def setUp(self) -> None:
        self.enima1 = Enima(animals, elements, stats)
        self.enima2 = Enima(animals, elements, stats)

    def test_element_should_be_within_the_element_list(self):
        self.assertIn(self.enima1.get_element(), elements)
        self.assertIn(self.enima2.get_element(), elements)

    def test_animal_should_be_within_the_animal_list(self):
        self.assertIn(self.enima1.get_animal(), animals)
        self.assertIn(self.enima2.get_animal(), animals)

    def test_enima_name(self):
        self.assertEqual(self.enima1.get_name(), f'{self.enima1.get_element()} {self.enima1.get_animal()}o')
        self.assertEqual(self.enima2.get_name(), f'{self.enima2.get_element()} {self.enima2.get_animal()}o')

    def test_health_should_be_in_between_200_to_400(self):
        self.assertIn(self.enima1.get_health(), range(200, 401))
        self.assertIn(self.enima2.get_health(), range(200, 401))

    def test_attack_should_be_in_between_50_to_150(self):
        self.assertIn(self.enima1.get_attack(), range(50, 151))
        self.assertIn(self.enima2.get_attack(), range(50, 151))

    def test_defense_should_be_in_between_50_to_150(self):
        self.assertIn(self.enima1.get_defense(), range(50, 151))
        self.assertIn(self.enima2.get_defense(), range(50, 151))

    def test_speed_should_be_in_between_50_to_150(self):
        self.assertIn(self.enima1.get_speed(), range(50, 151))
        self.assertIn(self.enima2.get_speed(), range(50, 151))

    def test_enima_is_alive_by_default(self):
        self.assertEqual(self.enima1.is_alive, True)
        self.assertEqual(self.enima2.is_alive, True)

    def test_take_correct_amount_of_damage(self):
        remaining_health = self.enima1.get_health() - 50
        self.enima1.take_damage(50)
        self.assertEqual(self.enima1.get_health(), remaining_health)

    def test_should_return_1_if_dead(self):
        self.enima1.take_damage(self.enima1.get_health())
        self.assertEqual(self.enima1.check_if_dead(), 1)
