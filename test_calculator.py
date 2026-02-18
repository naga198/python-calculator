import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)
        self.assertEqual(self.calc.subtract(10, 3), 7)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(5, 4), 20)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(15, 3), 5)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)
        self.assertEqual(self.calc.modulo(20, 7), 6)

    def test_simple_interest(self):
        # SI = (P × R × T) / 100
        # P=1000, R=5, T=2 => SI=100
        self.assertEqual(self.calc.simple_interest(1000, 5, 2), 100)
        # P=5000, R=10, T=3 => SI=1500
        self.assertEqual(self.calc.simple_interest(5000, 10, 3), 1500)
        # P=500, R=2, T=5 => SI=50
        self.assertEqual(self.calc.simple_interest(500, 2, 5), 50)

    def test_compound_interest(self):
        # A = P(1 + r/n)^(nt), CI = A - P
        # P=1000, R=10, T=1, compounds=1 => A=1100, CI=100
        self.assertAlmostEqual(self.calc.compound_interest(1000, 10, 1, 1), 100, places=2)
        # P=1000, R=10, T=2, compounds=1 => A=1210, CI=210
        self.assertAlmostEqual(self.calc.compound_interest(1000, 10, 2, 1), 210, places=2)
        # P=1000, R=12, T=1, compounds=12 (monthly) => CI≈126.83
        self.assertAlmostEqual(self.calc.compound_interest(1000, 12, 1, 12), 126.83, places=1)

    def test_irr(self):
        # IRR for simple investment: [-100, 50, 60]
        # Should return approximately 0.064 (6.4%)
        irr_value = self.calc.irr([-100, 50, 60])
        self.assertAlmostEqual(irr_value, 0.064, places=2)
        
        # IRR for another cash flow: [-1000, 300, 300, 300, 300]
        irr_value2 = self.calc.irr([-1000, 300, 300, 300, 300])
        self.assertGreater(irr_value2, 0)
        self.assertLess(irr_value2, 1)

if __name__ == '__main__':
    unittest.main()