import unittest

from main import Combat, Enima
from main import animals, elements, stats


class TestSpeedComparison(unittest.TestCase):
    def setUp(self) -> None:
        self.player_enima = Enima(animals, elements, stats)
        self.opp_enima = Enima(animals, elements, stats)

    def test_when_both_enima_equal_speed(self):
        self.player_enima.speed = 100
        self.opp_enima.speed = 100
        speed_comparison_result = Combat.compare_speed(self.player_enima.speed,
                                                       self.opp_enima.speed)
        self.assertIn(speed_comparison_result, [0, 1])

    def test_when_player_enima_higher_speed(self):
        self.player_enima.speed = 100
        self.opp_enima.speed = 99
        speed_comparison_result = Combat.compare_speed(self.player_enima.speed,
                                                       self.opp_enima.speed)
        self.assertEqual(speed_comparison_result, 1)

    def test_when_player_enima_lower_speed(self):
        self.player_enima.speed = 99
        self.opp_enima.speed = 100
        speed_comparison_result = Combat.compare_speed(self.player_enima.speed,
                                                       self.opp_enima.speed)
        self.assertEqual(speed_comparison_result, 0)


if __name__ == '__main__':
    unittest.main()
