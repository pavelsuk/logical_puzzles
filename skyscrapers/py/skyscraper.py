import csv
import pathlib

from enum import Enum
from itertools import permutations
from typing import List


class SkyscraperTypes(Enum):
    C_SKSCR_SUM = 1
    C_SKSCR_COUNT = 2


class Skyscraper(object):
    """
    Class generating the list of permutations for skyscraper puzzle
    The only important method is:
        Skyscraper.generate_all_permutations_2_csv(<grid_size>, csv_filename)
    All methods from this class are static.

    """

    @staticmethod
    def generate_perm(row: List) -> List:
        """Generates permutations, based on input row, converts them to the list of lists

        Args:
            row (List):

        Returns:
            List: Permutations, converted to List
        """
        perm = list(permutations(row))
        ret_list = [list(row) for row in perm]  # convert tuples into lists
        for i in list(ret_list):
            print(i)
        return ret_list

    @staticmethod
    def reduce_reversed(perm: List) -> List:
        """ Reduces the original permutation list to filter out duplicated caused by reverse permutations
        Not used anymore

        Args:
            perm (List): Original list of permutations

        Returns:
            List: reduced permutations
        """
        reduced_perm = []
        for i in list(perm):
            rev = list(i)
            rev.reverse()
            if rev in reduced_perm:
                print('{} in the list already'.format(rev))
            else:
                reduced_perm.append(i)
        return reduced_perm

    @staticmethod
    def get_sum(row: List) -> int:
        """Calculates the sum, based on visibility in the skyscraper
        If one of the preceding numbers is higher, current number in the list can't be used for sum

        Args:
            row (List): row in the skyscraper

        Returns:
            int: sum, based on skyscraper rules
        """
        max_num = 0
        ret_sum = 0
        for i in list(row):
            if (i > max_num):
                ret_sum += i
                max_num = i
        return ret_sum

    @staticmethod
    def append_sums(perm):
        ret_list = []
        for i in list(perm):
            rev = list(i)
            rev.reverse()
            sum_left = Skyscraper.get_sum(i)
            sum_right = Skyscraper.get_sum(rev)
            i.insert(0, sum_left)
            i.insert(1, sum_right)
            ret_list.append(i)
        return ret_list

    @staticmethod
    def get_count(row: List) -> int:
        """Calculates the count, based on visibility in the skyscraper
        If one of the preceding numbers is higher, current number in the list can't be counted

        Args:
            row (List): row in the skyscraper

        Returns:
            int: count, based on skyscraper rules
        """
        max_num = 0
        ret_count = 0
        for i in list(row):
            if (i > max_num):
                ret_count+= 1
                max_num = i
        return ret_count

    @staticmethod
    def append_count(perm):
        ret_list = []
        for i in list(perm):
            rev = list(i)
            rev.reverse()
            count_left = Skyscraper.get_count(i)
            count_right = Skyscraper.get_count(rev)
            i.insert(0, count_left)
            i.insert(1, count_right)
            ret_list.append(i)
        return ret_list

    @staticmethod
    def print_rows(rows):
        print('Printing table of rows')
        for i in list(rows):
            print(i)

    @staticmethod
    def get_field_names(rows):
        ret_field_names = ['sum_left', 'sum_right']
        if (len(rows) > 0):
            field_cnt = len(rows[1])
            if (field_cnt > 2):
                for i in range(2, field_cnt):
                    ret_field_names.append('n{}'.format(i - 1))
        return ret_field_names

    @staticmethod
    def export2csv(rows, csv_filename: str = None, csv_path: str = None):
        if (csv_filename):
            if (csv_path):
                csv_filename = pathlib.Path(csv_path).joinpath(csv_filename)
            print('Exporting to {}'.format(csv_filename))
            with open(csv_filename, "w", newline='') as output:
                field_names = Skyscraper.get_field_names(rows)
                writer = csv.writer(output)
                writer.writerow(field_names)
                writer.writerows(rows)

    @staticmethod
    def generate_all_permutations_2_csv(grid_size,
                                        csv_filename: str = None,
                                        csv_path: str = None,
                                        skyscraper_type: int = SkyscraperTypes.C_SKSCR_SUM):
        """ Generate all permutations, including sums and save it to csv file

        Args:
            grid_size: Size of Skyscraper grid
            csv_filename (String, optional):
                File name of exported csv.
                If None, no csv file will be created
        """
        if (grid_size > 0):
            initial_row = list(range(1, grid_size + 1))
            perm = Skyscraper.generate_perm(initial_row)
            print('Permutations ')
            print(perm)
            # I decided not to reduce the results and use full list
            # perm = Skyscraper.reduce_reversed(perm)
            # print('Permutations reduced')
            # Skyscraper.print_rows(perm)
            if (skyscraper_type == SkyscraperTypes.C_SKSCR_SUM):
                perm = Skyscraper.append_sums(perm)
            elif (skyscraper_type == SkyscraperTypes.C_SKSCR_COUNT):
                perm = Skyscraper.append_count(perm)
            else:
                print('Invalid option')
                return

            print('Added calculation')
            Skyscraper.print_rows(perm)
            Skyscraper.export2csv(perm, csv_filename, csv_path)
