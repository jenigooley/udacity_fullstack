import media 
import fresh_tomatoes

#several instances of class media.Movie

toy_story = media.Movie("Toy Story", "Anthropomorphized toys have neuroses,"
                        "hopes, and sexual tension", 
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc" )

buffalo_66 = media.Movie("Buffalo 66", "Lonely weirdo kidnaps doll girl to" 
                         "impress parents, avoids more jail time.",
                         "https://upload.wikimedia.org/wikipedia/en/b/b9/Buffalo_sixty_six_ver1.jpg", 
                         "https://www.youtube.com/watch?v=pY0H49c4q_Q")

they_live = media.Movie("They Live", "Man forgets to buy bubble gum, kicks" 
                        "fascist alien's asses.", 
                        "https://upload.wikimedia.org/wikipedia/en/3/3d/1988They_Live_poster300.jpg", 
                        "https://www.youtube.com/watch?v=KLRafyWhzG4")

the_descent = media.Movie("The Descent", "Tough women go into cave, fight" 
                          "mosters but who are the real monsters.", 
                          "https://upload.wikimedia.org/wikipedia/en/d/d5/Descentposter.jpg", 
                          "https://www.youtube.com/watch?v=WhZj0Q9rq9E")

two_brains = media.Movie("The Man with Two Brains", "Possible sociopath falls" 
                         "for woman's actual brain.", 
                         "https://upload.wikimedia.org/wikipedia/en/1/1f/Man_With_Two_Brains.jpg", 
                         "https://www.youtube.com/watch?v=vNQlFe9gCfE")

groundhog_day = media.Movie("Groundhog Day", "Man is trapped in existential" 
                            " crisis for ten thousand years, finds solution in mating.", 
                            "https://upload.wikimedia.org/wikipedia/en/b/b1/Groundhog_Day_%28movie_poster%29.jpg", 
                            "https://www.youtube.com/watch?v=tSVeDx9fk60")

#list of each instance
movies = [toy_story, buffalo_66, they_live, the_descent, two_brains, groundhog_day]
#creates simple website of each instance
fresh_tomatoes.open_movies_page(movies)
