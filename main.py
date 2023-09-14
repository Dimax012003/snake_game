from turtle import Screen,Turtle
from snake import snake
from food import Food
from scoreboard import score
import time
screen=Screen()
screen.setup(width=600,height=600)

screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

score=score()
p=snake()
food=Food()
screen.listen()
screen.onkey(p.up,"Up")
screen.onkey(p.down,"Down")
screen.onkey(p.right,"Right")
screen.onkey(p.left,"Left")
gameon = True
while gameon:
    screen.update()
    time.sleep(0.1)

    p.move()
    if p.head.distance(food)<15:
        food.setLoc()
        score.setscore()
        score.gettext()
        p.extend()
    if p.head.ycor()>280 or p.head.ycor()<-280 or p.head.xcor()>280 or p.head.xcor()<-280:

        score.reset()
        p.reset()
    for segments in p.segments[1:]:

        if p.head.distance(segments)<10:
            score.reset()
            p.reset()
    with open("data.txt",mode="w") as file:
        file.write(str(score.highscore))
screen.exitonclick()