from turtle import Turtle;
import random;

STARTING_POSITION =(0,-280);
MOVE_DISTANCE = 10;
FINISH_LINE_Y = 280;

# functions
def random_colour():
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF));
    return color;

class Player(Turtle):
    def __init__(self):
        super().__init__();
        self.penup();
        self.reset_position();

        self.shape("turtle");
        self.color("black");
        self.setheading(90);
    

    def move_up(self):
        new_y = self.ycor() + 20;
        self.sety(new_y);



    def reset_position(self):
        self.goto(STARTING_POSITION);

    def is_at_finishing_line(self):
        return self.ycor() > FINISH_LINE_Y
