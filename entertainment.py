import media
import fresh_tomatoes

# create different movie objects with movie class attributes
#such as movie name, storyline , movie image and reference to watch a movie trailer
toy_story = media.Movie("Toy Story",
                      "A story of a boy his toys that come to life",
                      "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar",
                     "A marine on a alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

school_of_rock = media.Movie("School of Rock", "Storyline",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

# Adding all our movies to array
array = [toy_story, avatar, school_of_rock]

# Transfer our movie array to our website, all movies from this array you will see on site
fresh_tomatoes.open_movies_page(array)
