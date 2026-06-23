from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import winsound

screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()





screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

screen.update()
print(scoreboard.refresh_speed)
while game_on:
    screen.update()
    time.sleep(scoreboard.refresh_speed)
    snake.move()

    #Detect collision between snake and food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        winsound.Beep(5000,100)

    #Detect collision with wall
    if snake.head.xcor() >290 or snake.head.xcor() <-290 or snake.head.ycor() >290 or snake.head.ycor() <-290:
        scoreboard.reset()
        snake.reset()
        game_on = False
        winsound.PlaySound("Womp-Womp-Womp.wav", winsound.SND_FILENAME)

    #Detect collision between snake's head and tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            scoreboard.reset()
            snake.reset()
            game_on = False
            winsound.PlaySound("Womp-Womp-Womp.wav", winsound.SND_FILENAME)



screen.exitonclick()