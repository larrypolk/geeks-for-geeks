import unittest


from rotate_array_solution.rotate_array import rotate


class GetRotateArrayTests(unittest.TestCase):
    def test_no_rotation(self):
        rotation = 0
        values = [1, 2, 3, 4, 5]
        self.assertEqual(rotate(rotation, values), values)

    def test_one_rotation(self):
        rotation = 1
        values = [1, 2, 3, 4, 5]
        expected = [2, 3, 4, 5, 1]
        self.assertEqual(rotate(rotation, values), expected)

    def test_two_rotation(self):
        rotation = 2
        values = [1, 2, 3, 4, 5]
        expected = [3, 4, 5, 1, 2]
        self.assertEqual(rotate(rotation, values), expected)

    def test_three_rotation(self):
        rotation = 3
        values = [1, 2, 3, 4, 5]
        expected = [4, 5, 1, 2, 3]
        self.assertEqual(rotate(rotation, values), expected)

    def test_four_rotation(self):
        rotation = 4
        values = [1, 2, 3, 4, 5]
        expected = [5, 1, 2, 3, 4]
        self.assertEqual(rotate(rotation, values), expected)

    def test_five_rotation(self):
        rotation = 5
        values = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(rotate(rotation, values), expected)

    def test_max_values_no_rotation(self):
        rotation = 0
        values = range(1, 10000001)
        expected = values
        self.assertEqual(rotate(rotation, values), expected)

    def test_max_values_full_rotation(self):
        rotation = 10000000
        values = range(1, 10000001)
        expected = values
        self.assertEqual(rotate(rotation, values), expected)

    def test_max_values_partial_rotation(self):
        max_vals = 10000000
        rotation = max_vals / 2
        values = range(1, max_vals + 1)
        expected = values[rotation:] + values[0:rotation]
        actual = rotate(rotation, values)
        self.assertTrue(len(actual) == len(expected))
        self.assertTrue(all([actual[i] == expected[i] for i in range(0, max_vals)]))

        rotation = max_vals - 1
        values = range(1, max_vals + 1)
        expected = values[rotation:] + values[0:rotation]
        actual = rotate(rotation, values)
        self.assertTrue(len(actual) == len(expected))
        self.assertTrue(all([actual[i] == expected[i] for i in range(0, max_vals)]))

    def test_edge_cases(self):
        rotation = 0
        values = range(1, 2)
        expected = [1]
        self.assertTrue(len(values) == 1)
        self.assertEqual(rotate(0, values), expected)
        self.assertEqual(rotate(1, values), expected)

        rotation = 0
        values = []
        expected = []
        self.assertTrue(len(values) == 0)
        self.assertEqual(rotate(0, values), expected)


if __name__ == '__main__':
    unittest.main()
