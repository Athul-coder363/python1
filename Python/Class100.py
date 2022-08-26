class Cubiod:
    def __init__(self,l,b,h):
        self.l=l 
        self.b=b
        self.h=h
    def area(self):
        area = self.l*self.b+self.b*self.h+self.h*self.l
        print(area)
    def volume(self):
        v = self.l*self.b*self.h
        print(v)
s1 = Cubiod(2,3,4)
s1.area()
s1.volume()