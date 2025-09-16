import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.ops['add'](2, 3), 5)

    def test_sub(self):
        self.assertEqual(calculator.ops['sub'](5, 2), 3)

    def test_mul(self):
        self.assertEqual(calculator.ops['mul'](3, 4), 12)

    def test_div(self):
        self.assertAlmostEqual(calculator.ops['div'](10, 2), 5)

    def test_pow(self):
        self.assertAlmostEqual(calculator.ops['pow'](2, 3), 8)

    def test_mod(self):
        self.assertAlmostEqual(calculator.ops['mod'](10, 3), 1)

if __name__ == '__main__':
    unittest.main()
