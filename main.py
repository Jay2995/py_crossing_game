from turtle import Turtle;
from turtle import Screen;
from player import Player;
from cars import *;
from scoreboard import Scoreboard;
import time;

screen = Screen();
screen.setup(width= 600, height=600);
# screen.bgcolor("black");
screen.tracer(0)

moving_car = Moving_car();
player = Player();
scoreboard = Scoreboard();

screen.listen()
screen.onkey(player.move_up,"Up");






game_is_active = True;
while game_is_active:
    screen.update()
    time.sleep(0.1)
    moving_car.create_car();
    moving_car.move_car();

    for car in moving_car.all_cars:
        if car.distance(player) < 20:
            game_is_active = False; 
            scoreboard.game_over();

    if player.is_at_finishing_line():
        scoreboard.add_score(); 
        player.reset_position();
        moving_car.add_speed();
    
    # print(moving_car.car_speed)


screen.exitonclick();