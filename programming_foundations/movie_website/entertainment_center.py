import fresh_tomatoes
import media


citizenfour = media.Movie("Citizenfour",
                        "A documentary about Edward Snowden post the NSA scandal",
                        "https://upload.wikimedia.org/wikipedia/en/3/37/Citizenfour_poster.jpg",
                        "https://www.youtube.com/watch?v=XiGwAvd5mvM")


internets_own_boy = media.Movie("The Internet's Own Boy",
                     "A documentary about Aaron Swartz, a computer programmer and activist",
                     "https://upload.wikimedia.org/wikipedia/en/a/a1/TOBSAS_poster.jpg",
                     "https://www.youtube.com/watch?v=RvsxnOg0bJY")


HUMAN = media.Movie("HUMAN",
                    "A documentary of men and women from the world telling their stories in front of a camera.",
                    "https://upload.wikimedia.org/wikipedia/en/f/fc/Human_2015_film_Official_Poster.jpg",
                    "https://www.youtube.com/watch?v=0-Retnj3TsA")


eternal_sunshine = media.Movie("Eternal Sunshine of the Spotless Mind",
                             "Scifi meets romance meets intellectual scripts",
                             "https://upload.wikimedia.org/wikipedia/en/6/62/Eternal_sunshine_of_the_spotless_mind_ver3.jpg",
                             "https://www.youtube.com/watch?v=rb9a00bXf-U")

stranger_than_fiction = media.Movie("Stranger than fiction",
                                    "A comedy about a man who is hearing voices narrating his life as he's living it.",
                                    "https://upload.wikimedia.org/wikipedia/en/f/ff/Stranger_Than_Fiction_%282006_movie_poster%29.jpg",
                                    "http://www.youtube.com/watch?v=c3sBBRxDAqk")
midnight_in_paris = media.Movie("Midnight in Paris", "Going back in time to meet authors",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "http://www.youtube.com/watch?v=atLg2wQQxvU")
jeux_denfants = media.Movie("Love me if you dare", "A french romantic movie about two friends who grew to become lovers",
                           "https://upload.wikimedia.org/wikipedia/en/e/e7/Love_Me_If_You_Dare_movie.jpg",
                           "https://www.youtube.com/watch?v=5buvvd5z7Gw")

#create an array of the above movies

movies = [citizenfour, internets_own_boy, HUMAN, eternal_sunshine, stranger_than_fiction, midnight_in_paris, jeux_denfants]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__) # returns "This class provides a way to store movie related information"
#print(media.Movie.__name__) # returns Movie
#print(media.Movie.__module__) # returns media
