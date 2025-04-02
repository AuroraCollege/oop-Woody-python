class Car:
    def __init__(self, make, model, year):
        self.make = make 
        self.model = model
        self.year = year 

def display_info(self):
    print(self.year, self.make, self.model)


Falcon = Car('Ford', 'G6E', 2014)
display_info(Falcon)