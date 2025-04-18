import unittest
from temperature_converter import convert_temperature

class TestTemperatureConverter(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        self.assertEqual(convert_temperature(0, 'C'), "0.0°C is 32.0°F")
        self.assertEqual(convert_temperature(100, 'C'), "100.0°C is 212.0°F")

    def test_fahrenheit_to_celsius(self):
        self.assertEqual(convert_temperature(32, 'F'), "32.0°F is 0.0°C")
        self.assertEqual(convert_temperature(212, 'F'), "212.0°F is 100.0°C")

    def test_invalid_unit(self):
        self.assertEqual(convert_temperature(0, 'K'), "Please input the correct unit: 'C' for Celsius or 'F' for Fahrenheit")

    def test_invalid_temperature(self):
        with self.assertRaises(ValueError):
            convert_temperature('abc', 'C')

if __name__ == '__main__':
    unittest.main()