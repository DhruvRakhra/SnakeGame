from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


def snake_game():
    my_screen = Screen()
    my_screen.setup(width=600, height=600)
    my_screen.bgcolor("black")
    my_screen.title("My Snake Game")
    my_screen.tracer(0)

    snake = Snake()
    food = Food()
    score_board = ScoreBoard()

    my_screen.listen()
    my_screen.onkey(key="Up", fun=snake.up)
    my_screen.onkey(key="Down", fun=snake.down)
    my_screen.onkey(key="Left", fun=snake.left)
    my_screen.onkey(key="Right", fun=snake.right)

    game_is_on = True

    while game_is_on:
        my_screen.update()
        time.sleep(0.1)

        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score_board.increase_score()
            score_board.reset_score()

        # Detect collision with wall
        if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
            score_board.reset_score()
            score_board.end_game()
            game_is_on = False

        # Detection with the body
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                score_board.reset_score()
                score_board.end_game()
                game_is_on = False

    play_again = my_screen.textinput(title="Play Again", prompt="Do You want to play again?")
    if play_again == "yes":
        my_screen.clear()
        snake_game()
    if play_again == "no":
        score_board.thankyou()

    my_screen.exitonclick()


snake_game()
