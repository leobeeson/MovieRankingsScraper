from scraper_empire_movies import ScraperEmpireMovies


def get_empire_movies_top_100(file_path):
    scraper = ScraperEmpireMovies()
    scraper.build_top_100_movies_list()
    scraper.save_top_100_movies_list(file_path)


if __name__ == "__main__":
    file_path_to_save_list = "movie_rankings/empire_top_100_movies.txt"
    get_empire_movies_top_100(file_path_to_save_list)



