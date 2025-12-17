class Room:


    width = None
    height = None
    length = None

    #init is for initialization
    #self is for a reference to a specific initialization
    def __init__(self, w, h, l):
        #apparently pass defines an empty class
        self.width = w
        self.height = h
        self.length = l


    def calculateVolume(self):
        volume = None
        volume = self.length * self.width * self.height
        return volume

    def returnWidth(self):
        return self.width
    
    def returnHeight(self):
        return self.height
    
    def returnLength(self):
        return self.length
    
