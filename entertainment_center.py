#!/usr/bin/python

import media
import fresh_tomatoes

# Constructors of class Movie with information on favorite movies
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys",
                        "http://www.heyuguys.com/images/2010/08/Toy-Story-3" +
                        "-Poster2.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A story about weirdos",
                     "http://www.heyuguys.com/images/2010/08/Toy-Story-3-" +
                     "Poster2.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")


school_of_rock = media.Movie("School of Rock",
                             "A story about weirdos",
                             "http://www.heyuguys.com/images/2010/08/Toy-" +
                             "Story-3-Poster2.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatuille = media.Movie("Ratatuille",
                         "A story about weirdos",
                         "http://www.heyuguys.com/images/2010/08/Toy-Story" +
                         "-3-Poster2.jpg",
                         "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "A story about weirdos",
                                "http://www.heyuguys.com/images/2010/08/Toy" +
                                "-Story-3-Poster2.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger games",
                           "A story about weirdos",
                           "http://www.heyuguys.com/images/2010/08/Toy-" +
                           "Story-3-Poster2.jpg",
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY")

all_movies = [toy_story, avatar, school_of_rock, ratatuille,
              midnight_in_paris, hunger_games]

# Run function, to create fresh_tomatoes.html
fresh_tomatoes.open_movies_page(all_movies)
