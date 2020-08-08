import pathlib

from skyscraper import Skyscraper, SkyscraperTypes  # C_SKSCR_COUNT, C_SKSCR_SUM

if __name__ == "__main__":
    current_dir = pathlib.Path(__file__).parent.parent
    Skyscraper.generate_all_permutations_2_csv(4, 'grids/4x4_sum.csv', current_dir)
    Skyscraper.generate_all_permutations_2_csv(5, 'grids/5x5_sum.csv', current_dir)
    Skyscraper.generate_all_permutations_2_csv(6, 'grids/6x6_sum.csv', current_dir)
    Skyscraper.generate_all_permutations_2_csv(4, 'grids/4x4_count.csv', current_dir, SkyscraperTypes.C_SKSCR_COUNT)
    Skyscraper.generate_all_permutations_2_csv(5, 'grids/5x5_count.csv', current_dir, SkyscraperTypes.C_SKSCR_COUNT)
    Skyscraper.generate_all_permutations_2_csv(6, 'grids/6x6_count.csv', current_dir, SkyscraperTypes.C_SKSCR_COUNT)
