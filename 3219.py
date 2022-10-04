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
