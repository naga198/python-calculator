import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)

    def test_square_root(self):
        self.assertEqual(self.calc.square_root(64), 8)

    def test_percentage(self):
        self.assertEqual(self.calc.percentage(25, 200), 12.5)

    def test_simple_interest(self):
        self.assertEqual(self.calc.simple_interest(1000, 5, 2), 100)

    def test_compound_interest(self):
        self.assertAlmostEqual(self.calc.compound_interest(1000, 10, 1, 1), 100, places=2)

    def test_emi(self):
        emi_value = self.calc.emi(500000, 8.5, 10)
        self.assertGreater(emi_value, 0)

    def test_sip_returns(self):
        sip_value = self.calc.sip_returns(5000, 12, 10)
        self.assertGreater(sip_value, 0)

    def test_cagr(self):
        self.assertAlmostEqual(self.calc.cagr(1000, 2000, 5), 14.87, places=1)

    def test_irr(self):
        irr_value = self.calc.irr([-100, 50, 60])
        self.assertAlmostEqual(irr_value, 0.064, places=2)

if __name__ == '__main__':
    unittest.main()