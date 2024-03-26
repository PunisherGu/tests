import unittest

def dividir(dividendo, divisor):
    # if divisor == 0:
    #     raise ValueError("Não é possível dividir por zero.")
    return dividendo / divisor

class TestDividir(unittest.TestCase): 
    def test_dividir_inteiros(self):
        self.assertEqual(dividir(10, 2), 5) 
        self.assertEqual(dividir(0, 2), 0)
        self.assertEqual(dividir(-10, 2), -5)
        self.assertEqual(dividir(10, -2), -5)
        self.assertEqual(dividir(-10, -2), 5)

    def test_dividir_floats(self):
        self.assertAlmostEqual(dividir(5.0, 2.0), 2.5)
        self.assertAlmostEqual(dividir(0.5, 0.25), 2.0)

    def test_dividir_por_zero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)
unittest.main()