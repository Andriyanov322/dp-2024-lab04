import unittest
from datetime import datetime
from clocks.digital_clock_adapter import DigitalClockAdapter


class TestDigitalClockAdapter(unittest.TestCase):
    def setUp(self):
        """Создает экземпляр DigitalClockAdapter перед каждым тестом."""
        self.adapter = DigitalClockAdapter()

    def test_set_date_time(self):
        """Проверяет правильность установки времени через адаптер."""
        test_time = datetime(2024, 11, 5, 15, 30, 45)  # 3:30:45 PM
        self.adapter.set_date_time(test_time)

        # Проверяем, что часы установлены правильно
        self.assertEqual(self.adapter.get_hour_angle(), 90)  # 3 PM -> 90 degrees
        self.assertEqual(self.adapter.get_minute_angle(), 180)  # 30 minutes -> 180 degrees
        self.assertEqual(self.adapter.get_second_angle(), 270)  # 45 seconds -> 270 degrees

    def test_get_date_time(self):
        """Проверяет корректность получения времени из адаптера."""
        test_time = datetime(2024, 11, 5, 15, 30, 45)  # 3:30:45 PM
        self.adapter.set_date_time(test_time)

        result = self.adapter.get_date_time()
        self.assertEqual(result, test_time)

    def test_invalid_set_date_time(self):
        """Проверяет, что возникает ошибка при передаче некорректного типа."""
        with self.assertRaises(ValueError):
            self.adapter.set_date_time("Некорректный ввод")

    def test_edge_case_midnight(self):
        """Проверяет установку времени на полночь (00:00:00)."""
        test_time = datetime(2024, 11, 5, 0, 0, 0)  # 12:00 AM
        self.adapter.set_date_time(test_time)

        # Проверяем, что углы установлены корректно
        self.assertEqual(self.adapter.get_hour_angle(), 0)   # 0 degrees
        self.assertEqual(self.adapter.get_minute_angle(), 0)  # 0 degrees
        self.assertEqual(self.adapter.get_second_angle(), 0)  # 0 degrees

    def test_edge_case_noon(self):
        """Проверяет установку времени на полдень (12:00:00)."""
        test_time = datetime(2024, 11, 5, 12, 0, 0)  # 12:00 PM
        self.adapter.set_date_time(test_time)

        # Проверяем, что углы установлены корректно
        self.assertEqual(self.adapter.get_hour_angle(), 0)   # 0 degrees
        self.assertEqual(self.adapter.get_minute_angle(), 0)  # 0 degrees
        self.assertEqual(self.adapter.get_second_angle(), 0)  # 0 degrees


if __name__ == '__main__':
    unittest.main()
