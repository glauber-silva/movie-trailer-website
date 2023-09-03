import json
import csv
import re

import requests
from src.model import Movie, Movies
from src.media import main_page_head, main_page_content, movie_tile_content


class EntertaimentCenterServices:
    @classmethod
    def omdb_url(cls, title):
        # return f"http://www.omdbapi.com/?t={title}&y=&plot=short&r=json"
        return f"http://www.omdbapi.com/?i=tt3896198&apikey=dc6d4014&t={title}&y=&plot=short&r=json"

    @classmethod
    def get_prefered_movies(cls) -> Movies:
        movies = Movies()
        with open("./preferred_movies.csv", "r") as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                movies.movies.append(
                    Movie(title=row["title"], trailer_youtube_url=row["link"])
                )

        return movies

    @classmethod
    def retrieve_data_from_omdb(cls, movie: Movie) -> dict:
        title = movie.title.replace(" ", "+")
        response = requests.get(cls.omdb_url(title))
        json_data = json.loads(response.text)
        return json_data

    @classmethod
    def populate_movie_data(cls, omdb_data: dict, movie: Movie):
        movie.plot = omdb_data.get("Plot", "")
        movie.actors = omdb_data.get("Actors", "")
        movie.director = omdb_data.get("Director", "")
        movie.released = omdb_data.get("Released", "")
        movie.released = omdb_data.get("Poster", "")


class ContentService:
    @classmethod
    def create_movie_tiles_content(cls, movies: Movies) -> str:
        content = ""

        for movie in movies:
            # Extract the youtube ID from the URL
            yt_id_match = re.search(r"(?<=v=)[^&#]+", movie.trailer_youtube_url)
            yt_id_match = yt_id_match or re.search(
                r"(?<=be/)[^&#]+", movie.trailer_youtube_url
            )
            trailer_yt_id = yt_id_match.group(0) if yt_id_match else None

            content += movie_tile_content.format(
                movie_title=movie.title,
                poster_image_url=movie.poster_image,
                trailer_youtube_id=trailer_yt_id,
                actors=movie.actors,
                director=movie.director,
                released=movie.released,
                plot=movie.plot,
            )

        return content

    @classmethod
    def generate_movies_page(cls, movies: Movies):
        # Create or overwrite the output file
        output = open("../fresh_tomatoes.html", "w")

        # Replace the placeholder for the movie tiles with the actual dynamically generated content
        movie_tiles_content = cls.create_movie_tiles_content(movies.movies)
        rendered_content = main_page_content.format(movie_tiles=movie_tiles_content)

        # Output the file
        output.write(main_page_head + rendered_content)
        output.close()

    @classmethod
    def create_main_page(cls):
        entertainment = EntertaimentCenterServices()
        content = ContentService()
        movies = entertainment.get_prefered_movies()
        for movie in movies.movies:
            omdb_data = entertainment.retrieve_data_from_omdb(movie)
            entertainment.populate_movie_data(omdb_data, movie)

        content.generate_movies_page(movies)
