import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys",
                        "http://www.heyuguys.com/images/2010/08/Toy-Story-3-Poster2.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A story about weirdos",
                     "http://www.heyuguys.com/images/2010/08/Toy-Story-3-Poster2.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")


school_of_rock = media.Movie("School of Rock",
                             "A story about weirdos",
                             "http://www.heyuguys.com/images/2010/08/Toy-Story-3-Poster2.jpg",
                             "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

ratatuille = media.Movie("School of Rock",
                             "A story about weirdos",
                             "http://www.heyuguys.com/images/2010/08/Toy-Story-3-Poster2.jpg",
                             "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

midnight_in_paris = media.Movie("School of Rock",
                             "A story about weirdos",
                             "http://www.heyuguys.com/images/2010/08/Toy-Story-3-Poster2.jpg",
                             "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

hunger_games = media.Movie("School of Rock",
                             "A story about weirdos",
                             "http://www.heyuguys.com/images/2010/08/Toy-Story-3-Poster2.jpg",
                             "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

movies = [toy_story,avatar,school_of_rock, ratatuille, midnight_in_paris, hunger_games]

#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
print(media.Movie.__bases__)
