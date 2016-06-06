import webbrowser

#class takes data for a movie, assigns movie data to corresponding variable and 
#uses data to play movie trailer in browser. This is to be used for creating a 
#simple movie website 

class Movie():
    '''constructor takes information about a movie and assigns it to 
       corresponding variable'''
    def __init__(self, movie_title, movie_storyline, poster_image, 
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #opens movie trailer url in browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
