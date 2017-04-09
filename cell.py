class Point ():
    def __init__(self):
        self.row = 0
        self.col = 0


class Cell ():
    def __init__(self, theNLocations, theBandLength):
        self.theNLocations = theNLocations
        self.theBandLength = theBandLength
        self.active = False
        self.tracked = False
        self.generation = 0
        self.centerRow = 0
        self.centerCol = 0
        self.radius = 0
        self.boundary = Point()
