# (0,1),()


class point:
    def  _init_(self,x,y):
    self.x =x 
    self.y = y


    def distance(self, otherpoint):
        x1 =self.x
        y1 =self.y
        x2 = otherpoint.x
        y2 = otherpoint.y


        d =((x2 -x1)^2 + (y2-y1)^2)**(1/2)
        return d

p1 = point(0,1)   #initialization object
p = point(0,1) 