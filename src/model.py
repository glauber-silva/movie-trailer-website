import webbrowser

from dataclasses import dataclass, field
from typing import List


@dataclass
class Movie:
    """
    This is to store movie's data related
    """
    title: str
    trailer_youtube_url: str
    plot: str = ""
    poster_image: str = ""
    director: str = ""
    actors: str = ""
    released: str = ""


    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


@dataclass
class Movies:
    """
    It will store a List of the movies
    """
    movies: List = field(default_factory=list)
