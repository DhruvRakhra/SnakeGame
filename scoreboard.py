from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 24, 'bold')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data") as file:
            self.high_score = file.read()
            self.high_score = int(self.high_score)
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score = {self.score}  High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.update_score()

    def end_game(self):
        self.clear()
        self.goto(0, 0)
        if self.score >= self.high_score:
            if self.score != 0:
                self.write(arg=f'New High Score!! \n Your Score : {self.high_score}', align=ALIGNMENT, font=FONT)
                with open("data", "w") as f:
                    f.write(f'{self.high_score}')
            else:
                self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
                self.goto(0, -30)
                self.write(arg=f"Final Score = {self.score}", align=ALIGNMENT, font=FONT)

        else:
            self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
            self.goto(0, -30)
            self.write(arg=f"Final Score = {self.score}", align=ALIGNMENT, font=FONT)

    def thankyou(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg="THANK YOU!!", align=ALIGNMENT, font=FONT)
