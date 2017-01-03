import fresh_tomatoes
import media

a_new_hope = media.Movie("Star Wars - A New Hope",
                         "Luke Skywalker and a motley group of rebels and robots battle the evil Darth Vadar",
                         "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
                         "https://www.youtube.com/watch?v=1g3_CFmnU7k")

empire_strikes_back = media.Movie("The Empire Strikes Back",
                                  "After the rebels have been brutally overpowered by the Empire on their newly established base, Luke Skywalker takes advanced Jedi training with Master",
                                  "https://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",
                                  "https://www.youtube.com/watch?v=xESiohGGP7g")

return_of_the_jedi = media.Movie("Return of the Jedi",
                                 "After rescuing Han Solo from the palace of Jabba the Hutt, the rebels attempt to destroy the second Death Star",
                                 "https://upload.wikimedia.org/wikipedia/en/b/b2/ReturnOfTheJediPoster1983.jpg",
                                 "https://www.youtube.com/watch?v=5UfA_aKBGMc")

phantom_menace = media.Movie("The Phantom Menace",
                             "Two Jedi Knights escape a hostile blockade to find allies and come across a young boy who may bring balance to the Force.",
                             "https://upload.wikimedia.org/wikipedia/en/4/40/Star_Wars_Phantom_Menace_poster.jpg",
                             "https://www.youtube.com/watch?v=I6hOlI9cg4o")

attack_of_the_clones = media.Movie("Attack of the Clones",
                                   "Ten years after initially meeting, Anakin Skywalker investigates an assassination attempt on the Senator and discovers a secret clone army crafted for the Jedi.",
                                   "https://upload.wikimedia.org/wikipedia/en/3/32/Star_Wars_-_Episode_II_Attack_of_the_Clones_%28movie_poster%29.jpg",
                                   "https://www.youtube.com/watch?v=gYbW1F_c9eM")

revenge_of_the_sith = media.Movie("Revenge of the Sith",
                                  "Darth Sidious has revealed himself and is ready to execute the last part of his plan to rule the Galaxy.",
                                  "https://upload.wikimedia.org/wikipedia/en/9/93/Star_Wars_Episode_III_Revenge_of_the_Sith_poster.jpg",
                                  "https://www.youtube.com/watch?v=MR1xo1tLyBk")

force_awakens = media.Movie("The Force Awakens",
                            "Three decades after the defeat of the Galactic Empire, a new threat arises",
                            "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",
                            "https://www.youtube.com/watch?v=sGbxmsDFVnE")

rogue_one = media.Movie("Rogue One",
                        "A Star Wars Story, in which Jyn Erso leads a group of rebels",
                        "https://upload.wikimedia.org/wikipedia/en/d/d4/Rogue_One%2C_A_Star_Wars_Story_poster.png",
                        "https://www.youtube.com/watch?v=frdj1zb9sMY")

movies = [a_new_hope, empire_strikes_back, return_of_the_jedi, phantom_menace,
          attack_of_the_clones, revenge_of_the_sith, force_awakens, rogue_one]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__doc__)
