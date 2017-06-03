import media
import fresh_tomatoes

toy_story = media.Movie("TRANSFORMERS 5 Final Trailer", "Here is the Final Trailer for Transformers 5", "https://i.ytimg.com/vi/TogrG-UZxWE/hqdefault.jpg?sqp=-oaymwEXCPYBEIoBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLA9477jiNK8eS7RUesZ9aQay5v1lg", "https://www.youtube.com/watch?v=TogrG-UZxWE")
alien = media.Movie("Alien: Covenant Trailer", "Here is the Final Trailer for Alien: Covenant Trailer", "https://i.ytimg.com/vi/u5KPP6lxRVg/hqdefault.jpg?sqp=-oaymwEXCPYBEIoBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLAQnw94ZMI3CvD_lUI1cWS-wkpMCA","https://www.youtube.com/watch?v=u5KPP6lxRVg")
#toy_story.show_trailer()
thor = media.Movie("Thor: Ragnarok Teaser", "This November, Thor: Ragnarok. Watch the teaser trailer now! ", "https://i.ytimg.com/vi/v7MGUNV8MxU/hqdefault.jpg?sqp=-oaymwEXCPYBEIoBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLAYvb3o_jlSfnE1CgIU2-mZm7BTUA", "https://www.youtube.com/watch?v=v7MGUNV8MxU")

movies = [toy_story, alien, thor]

fresh_tomatoes.open_movies_page(movies)