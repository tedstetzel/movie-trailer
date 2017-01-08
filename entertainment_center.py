import fresh_tomatoes
import media

#  Create a list of movies using title, poster link, youtube trailer link

a_new_hope = media.Movie("Star Wars - A New Hope",
                         "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=1g3_CFmnU7k")

empire_strikes_back = media.Movie("The Empire Strikes Back",
                                  "https://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",  # NOQA
                                  "https://www.youtube.com/watch?v=xESiohGGP7g")    # NOQA

return_of_the_jedi = media.Movie("Return of the Jedi",
                                 "https://upload.wikimedia.org/wikipedia/en/b/b2/ReturnOfTheJediPoster1983.jpg",  # NOQA
                                 "https://www.youtube.com/watch?v=5UfA_aKBGMc")

phantom_menace = media.Movie("The Phantom Menace",
                             "https://upload.wikimedia.org/wikipedia/en/4/40/Star_Wars_Phantom_Menace_poster.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=I6hOlI9cg4o")

attack_of_the_clones = media.Movie("Attack of the Clones",
                                   "https://upload.wikimedia.org/wikipedia/en/3/32/Star_Wars_-_Episode_II_Attack_of_the_Clones_%28movie_poster%29.jpg",  # NOQA
                                   "https://www.youtube.com/watch?v=gYbW1F_c9eM")    # NOQA

revenge_of_the_sith = media.Movie("Revenge of the Sith",
                                  "https://upload.wikimedia.org/wikipedia/en/9/93/Star_Wars_Episode_III_Revenge_of_the_Sith_poster.jpg",  # NOQA
                                  "https://www.youtube.com/watch?v=MR1xo1tLyBk")    # NOQA

force_awakens = media.Movie("The Force Awakens",
                            "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=sGbxmsDFVnE")

rogue_one = media.Movie("Rogue One",
                        "https://upload.wikimedia.org/wikipedia/en/d/d4/Rogue_One%2C_A_Star_Wars_Story_poster.png",  # NOQA
                        "https://www.youtube.com/watch?v=frdj1zb9sMY")

# Put movies into an array to pass to fresh_tomatoes.py to create webpage
movies = [a_new_hope, empire_strikes_back, return_of_the_jedi, phantom_menace,
          attack_of_the_clones, revenge_of_the_sith, force_awakens, rogue_one]
fresh_tomatoes.open_movies_page(movies)
