class Movie:
    def __init__(self,Movie_name, year, director):
        self.name=Movie_name
        self.year=year
        self.director=director
        self.metadata=dict()
        self.temp=[]
    def __str__(self):
        return self.name
    
    def show_info(self):
        print('Movie_name:',self.name)
        print('Year:',self.year)
        print('Director:',self.director)
        for i in self.temp:
            print(i,':',self.metadata[i])
        
    def add_metadata(self,tag, value):
        self.metadata[tag]=value
        self.temp.append(tag)

class Database:
    def __init__(self,*Movie):
        self.movies=list(Movie)
        self.len=len(self.movies)

    def add(self,Movie):
        self.movies.append(Movie)
        self.len+=1
    
    def list_movie(self):
        print("There are %d movies in Database"%self.len)
        for i in self.movies:
            i.show_info()
            print()

