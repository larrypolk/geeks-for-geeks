import random
import unittest


from segregate_zeroes_and_ones_solution.segregate_zeroes_and_ones import segregate


class GetSegregateZeroesAndOneTests(unittest.TestCase):
    def test_all_zeroes(self):
        values = [0] * 5
        expected = [0] * 5
        self.assertEqual(segregate(values), expected)

    def test_all_ones(self):
        values = [1] * 5
        expected = [1] * 5
        self.assertEqual(segregate(values), expected)

    def test_mixed(self):
        values = [0, 0, 0, 1, 1]
        self.assertEqual(segregate(values), values)

        self.assertEqual(segregate(values[::-1]), values)

    def test_max_elements(self):
        max_elements = 10000000
        values = [random.choice([0, 1]) for _ in range(max_elements)]
        self.assertTrue(len(values) == max_elements)
        actual = segregate(values)

        zero_count = values.count(0)
        self.assertTrue(not any(actual[0:zero_count]))
        self.assertTrue(all(actual[zero_count:]))

    def test_many_elements(self):
        max_elements = 3000
        values = [random.choice([0, 1]) for _ in range(max_elements)]
        self.assertTrue(len(values) == max_elements)

        actual = segregate(values)
        self.assertTrue(segregate(values), sorted(values))


if __name__ == '__main__':
    unittest.main()
