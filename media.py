import webbrowser
class Movie():
    """" This class will help you to make your own movie objects with couple of different attributes such as
    title, storyline and it will show you trailer of the chosen movie"""
    def __init__(self,movie_title,movie_storyline,movie_image,
                 movie_trailer):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=movie_image
        self.trailer_youtube_url=movie_trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
