import webbrowser

class Movie():
  """ This class Provides a way to store movie related informatin"""

  def __init__(self, movie_title, poster_image, trailer_youtube):
    self.title = movie_title
    self.poster_image_url = poster_image
    self.trailer_youtube_url = trailer_youtube

  def show_trailer(self):
    webbrowser.open(self.trailer_youtube_url)

