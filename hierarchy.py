class shape:
    def info(self):
        return "this is a shape"
class circle(shape):
    def draw_circle(self):
        return "this is a circle"
class square(shape):
    def draw_sqaure(self):
        return " thiss is a sqaure"
class triangle(shape):
    def draw_triangle(self):
        return "this is a triangle"
s= shape()
c= circle()
sq = square()
t = triangle()
print(s.info())
print(c.draw_circle())
print(c.info())
