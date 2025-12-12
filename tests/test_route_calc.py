import unittest
from route_calc import calculate_route

class TestRouteCalc(unittest.TestCase):
    def test_A_to_B_route(self):
        r = calculate_route("A", "B")
        self.assertEqual(r["origin"], "A")
        self.assertEqual(r["destination"], "B")
        self.assertEqual(r["stops"], ["A", "X", "B"])
        self.assertAlmostEqual(r["distance_km"], 12.5)
        self.assertEqual(r["time_min"], 20)

    def test_B_to_C_route(self):
        r = calculate_route("B", "C")
        self.assertEqual(r["stops"], ["B", "Y", "C"])
        self.assertAlmostEqual(r["distance_km"], 8.0)
        self.assertEqual(r["time_min"], 12)

if __name__ == "__main__":
    unittest.main()
