import webbrowser


class Movie():
    """This Class provided a way to store movie related information"""

    def __init__(self, title, plot, poster_image, director, actors, released
        , trailer_youtube):
        self.title = title
        self.plot = plot
        self.poster_image = poster_image
        self.director = director
        self.actors = actors
        self.released = released
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
