class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
        area=length*width
    def area(self):
        return self.length*self.width
rect=rectangle(6,9)
print("area",rect.area())
