from unittest import TestCase

from checkout import checkout


class CheckoutTests(TestCase):
    def test_rejects_negative_quantity(self):
        with self.assertRaises(ValueError):
            checkout([(2_500, -1)], discount_pct=0)
    def test_accepts_positive_quantity(self):
        self.assertEqual(checkout([(1_000, 2)], discount_pct=0), 2_499)
    def test_rejects_discount_above_100_percent(self):
        with self.assertRaises(ValueError):
            checkout([(1_000, 2)], discount_pct=101)
