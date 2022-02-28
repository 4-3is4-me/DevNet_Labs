class Location:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def myLocation(self):
        print("Hello, I am " + self.name + ", and I live in " + self.country + ".")


myloc1 = Location("Tim", "UK")
myloc1.myLocation()
myloc2 = Location("Paul", "Germany")
myloc3 = Location("Alan", "France")
myloc2.myLocation()
myloc3.myLocation()