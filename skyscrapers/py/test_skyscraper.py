import unittest
# import logging

from skyscraper import Skyscraper


class Test_Skyscraper(unittest.TestCase):
    def setUp(self):
        # log = logging.getLogger()
        pass

    def tearDown(self):
        pass

    def test_generate_perm(self):
        test_row = [1, 2, 3, 4, 5]
        perm = Skyscraper.generate_perm(test_row)
        Skyscraper.print_rows(perm)

    def test_reduce_reversed(self):
        test_rows = [[1, 2, 3, 4, 5], [1, 2, 4, 3, 5], [5, 4, 3, 2, 1]]
        perm = Skyscraper.reduce_reversed(test_rows)
        Skyscraper.print_rows(perm)

    def test_append_calculations(self):
        test_rows = [[1, 2, 3, 4, 5], [1, 2, 4, 3, 5], [5, 4, 3, 1, 2],
                     [1, 5, 2, 3, 4], [2, 3, 1, 5, 2]]
        perm = Skyscraper.append_calculations(test_rows)
        Skyscraper.print_rows(perm)

    def test_export2csv(self):
        test_rows = [[1, 2, 3, 4, 5], [1, 2, 4, 3, 5], [5, 4, 3, 1, 2],
                     [1, 5, 2, 3, 4], [2, 3, 1, 5, 2]]
        Skyscraper.export2csv(test_rows, '')
        Skyscraper.export2csv(test_rows, 'export_test.csv')
        Skyscraper.print_rows(test_rows)

    def test_generate_all_permutations(self):
        Skyscraper.generate_all_permutations_2_csv(2, '')
        Skyscraper.generate_all_permutations_2_csv(5, 'export_test_5x5.csv')

    @unittest.skip("always fails")
    def test_fail(self):
        return self.assertTrue(False, 'This assertion must always fail')


if __name__ == "__main__":
    unittest.main()
