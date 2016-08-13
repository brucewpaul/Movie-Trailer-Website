import fresh_tomatoes
import media

#
# Create Movie Instances
#

being_john_malkovich = media.Movie("Being John Malkovich",
                                   "https://upload.wikimedia.org/wikipedia/en/5/55/Being_John_Malkovich_poster.jpg",
                                   "https://www.youtube.com/watch?v=K7ahIGLNNwo")

the_400_blows = media.Movie("The 400 Blows",
                            "http://s3.amazonaws.com/auteurs_production/post_images/9736/400Blows_Grinsson_MPOTW.jpg?1328764461",
                            "https://www.youtube.com/watch?v=15SEzC5dqZQ")

paris_texas = media.Movie("Paris, Texas",
                          "https://www.cinematerial.com/media/posters/sm/jy/jygyjhy8.jpg?v=1456260387",
                          "https://www.youtube.com/watch?v=9e590FeeGCM")

#
# Put Movie Instances in list
#

movies = [being_john_malkovich, the_400_blows, paris_texas]

#
# Send Movie list to render function
#

fresh_tomatoes.open_movies_page(movies)