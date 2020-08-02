import pathlib

from skyscraper import Skyscraper

if __name__ == "__main__":
    current_dir = pathlib.Path(__file__).parent.parent
    Skyscraper.generate_all_permutations_2_csv(4, 'grids/4x4.csv', current_dir)
    Skyscraper.generate_all_permutations_2_csv(5, 'grids/5x5.csv', current_dir)
    Skyscraper.generate_all_permutations_2_csv(6, 'grids/6x6.csv', current_dir)
