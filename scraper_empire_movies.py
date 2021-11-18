from scraper import Scraper
from typing import List
import re


class ScraperEmpireMovies(Scraper):

    page_url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

    def __init__(self) -> None:
        super().__init__()


    def build_top_100_movies_list(self, class_: str="title") -> None:
        titles = self.get_elements_by_single_class(class_)
        actual_movies = self.filter_movies(titles)
        self.ranked_movies = self.reverse_order(actual_movies)


    def filter_movies(self, titles):
        regex = re.compile("^\d{1,3}[\)\:] ")
        actual_movies = list(filter(regex.match, titles))
        return actual_movies


    def reverse_order(self, actual_movies: List[str]) -> List[str]:
        ascending_movies = actual_movies[::-1]
        return ascending_movies

    
    def save_top_100_movies_list(self, file_path:str) -> None:
        with open(file_path, "w") as file:
            file.writelines("\n".join(self.ranked_movies))


if __name__ == "__main__":
    scraper = ScraperEmpireMovies()
    scraper.build_top_100_movies_list()
    scraper.save_top_100_movies_list("movie_rankings/empire_top_100_movies.txt")

