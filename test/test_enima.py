import unittest

import main
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

    def test_should_show_stats_correctly(self):
        self.enima1.health = 400
        self.enima1.attack = 150
        self.enima1.defense = 150
        self.enima1.speed = 150
        expected_response = f'Health: 400  Attack: 150  Defense: 150  Speed: 150'
        actual_response = self.enima1.show_stats()
        self.assertEqual(actual_response, expected_response)

    def test_bonus_for_neutral_effectiveness(self):
        self.enima1.element = 'Fire'
        self.enima2.element = 'Fire'
        _, bonus = self.enima1.deal_damage(self.enima2, elements)
        self.assertEqual(bonus, 1.0)

    def test_bonus_for_super_effectiveness(self):
        self.enima1.element = 'Fire'
        self.enima2.element = 'Metal'
        _, bonus = self.enima1.deal_damage(self.enima2, elements)
        self.assertEqual(bonus, 1.5)

    def test_bonus_for_non_effectiveness(self):
        self.enima1.element = 'Fire'
        self.enima2.element = 'Earth'
        _, bonus = self.enima1.deal_damage(self.enima2, elements)
        self.assertEqual(bonus, 0.5)

    def test_deal_correct_amount_of_damage(self):
        self.enima1.element = 'Fire'
        self.enima2.element = 'Fire'
        self.enima1.attack = 100
        self.enima2.defense = 50
        damage_dealt, _ = self.enima1.deal_damage(self.enima2, elements)
        self.assertEqual(damage_dealt, main.Combat.calc_damage(100, 50, 1.0))

    def test_take_correct_amount_of_damage(self):
        remaining_health = self.enima1.get_health() - 50
        self.enima1.take_damage(50)
        self.assertEqual(self.enima1.get_health(), remaining_health)

    def test_should_return_1_if_dead(self):
        self.enima1.take_damage(self.enima1.get_health())
        self.assertEqual(self.enima1.check_if_dead(), 1)
