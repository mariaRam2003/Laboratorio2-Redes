from unittest import TestCase
from Hamming import calculate_parity_bits, encode


class Test(TestCase):
    def test_calculate_parity_bits(self):
        res = calculate_parity_bits([1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1], 1)
        self.assertEqual(res, 1)

        res = calculate_parity_bits([1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1], 2)
        self.assertEqual(res, 0)

        res = calculate_parity_bits([1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1], 4)
        self.assertEqual(res, 0)

        res = calculate_parity_bits([1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1], 8)
        self.assertEqual(res, 0)

    def test_encode(self):
        message = [1, 0, 0, 0, 0, 0, 1]
        res = encode(message)
        expected = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1]
        self.assertEqual(res, expected)

        message = [1, 0, 0, 1, 1, 0, 0]
        res = encode(message)
        expected = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0]
        self.assertEqual(res, expected)
