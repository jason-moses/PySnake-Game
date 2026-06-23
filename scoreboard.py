from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")
ANNOUNCEMENT_FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.game_mode = self.screen.textinput("Choose Mode", "easy/normal/hard ")
        print(self.game_mode)
        if self.game_mode == "easy":
            self.refresh_speed = 0.2

        elif self.game_mode == "normal":
            self.refresh_speed = 0.1

        elif self.game_mode == "hard":
            self.refresh_speed = 0.07
        with open(f"data_{self.game_mode}.txt") as data:
            self.highscore = int(data.read())
        self.color((8,255,8))
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
         self.goto(0,0)
         self.write("Game Over", align=ALIGNMENT, font=ANNOUNCEMENT_FONT)
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(f"data_{self.game_mode}.txt", mode="w") as data:
                data.write(str(self.highscore))
        self.update_scoreboard()
        self.game_over()