from turtle import Turtle
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
class snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segments=[]
        self.createsnakes()
        self.head=self.segments[0]
    def createsnakes(self):
        for position in starting_positions:
            self.add_seg(position)

    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            new_x=self.segments[i-1].xcor()
            new_y=self.segments[i-1].ycor()
            self.segments[i].goto(new_x,new_y)
        self.segments[0].forward(20)
    def up(self):
        if self.segments[0].heading()!=270:
            self.segments[0].setheading(90)
    def left(self):
        if self.segments[0].heading()!=0:
            self.segments[0].setheading(180)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def right(self):
        if self.segments[0].heading()!=180:
            self.segments[0].setheading(0)
    def add_seg(self,position):
        new_seg = Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(position)
        self.segments.append(new_seg)
    def extend(self):
        self.add_seg(self.segments[-1].position())
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.createsnakes()
        self.head=self.segments[0]

