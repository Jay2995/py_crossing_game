from turtle import Turtle;

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__();
        self.pu();
        self.hideturtle()
        self.score = 0
        self.color("black");
        self.update_score();
        
    def update_score(self):
        self.goto(-250, 250);
        self.write(f"SCORE: {self.score}", align="center", font=("Courier",12, "normal"));

    def add_score(self):
        self.clear();
        self.score += 1;
        self.update_score();

    def game_over(self):
        # self.clear();
        self.goto(0,0);
        self.write(f"GAME OVER", align="center", font=("Courier",12, "normal"));



