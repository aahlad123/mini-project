# mini-project
game using python 
import turtle
import random

# Setup the animation screen
animation = turtle.Screen()
animation.bgpic("background.gif")
animation.addshape("player.gif")
animation.addshape("asteroid.gif")
animation.addshape("life.gif")
animation.tracer(0)

# Create turtles for start screen, score board, and game objects
Start_Screen = turtle.Turtle()
Start_Screen.hideturtle()
Start_Screen.penup()

Score_board = turtle.Turtle()
Score_board.hideturtle()
Score_board.penup()

animation.screensize(300, 300)
animation.setup(550, 550)
vertical, horizontal = animation.screensize()

# Game and player dictionaries
game = {'score': 0, 'remaining_lives': 3, 'present_level': 1, 'frames': 0, 'Positive_points': 100, 'level_increase': 400}
player = {'turtle': turtle.Turtle(), 'image': 'player.gif', 'speed': 13, 'radius': 80, 'type': 'player'}
player['turtle'].shape(player['image'])
player['turtle'].goto(0, 0)

asteroid_object = {'turtle': turtle.Turtle(), 'image': 'asteroid.gif', 'speed': 0.4, 'radius': 30, 'type': 'asteroid'}
asteroid_object['turtle'].shape(asteroid_object['image'])
asteroid_object['turtle'].goto(150, 250)

Positive_object = {'turtle': turtle.Turtle(), 'image': 'life.gif', 'speed': 0.7, 'radius': 20, 'type': 'Positive'}
Positive_object['turtle'].shape(Positive_object['image'])
Positive_object['turtle'].goto(-150, 250)

def move_up():
    new_y = player['turtle'].ycor() + player['speed']
    player['turtle'].sety(new_y)

def move_down():
    new_y = player['turtle'].ycor() - player['speed']
    player['turtle'].sety(new_y)

def move_right():
    new_x = player['turtle'].xcor() + player['speed']
    player['turtle'].setx(new_x)

def move_left():
    new_x = player['turtle'].xcor() - player['speed']
    player['turtle'].setx(new_x)

animation.onkey(move_left, "Left")
animation.onkey(move_left, "a")
animation.onkey(move_right, "Right")
animation.onkey(move_right, "d")
animation.onkey(move_up, "Up")
animation.onkey(move_up, "w")
animation.onkey(move_down, "Down")
animation.onkey(move_down, "s")
animation.listen()

def game_data():
    Score_board.clear()
    Score_board.goto(-100, 250)
    Score_board.write('Score: ' + str(game['score']), font=('Times New Roman', 12, 'normal'))
    Score_board.goto(140, 250)
    Score_board.write('Lives: ' + str(game['remaining_lives']), font=('Times New Roman', 12, 'normal'))
    Score_board.goto(-10, 250)
    Score_board.write('Frames: ' + str(game['frames']), font=('Times New Roman', 12, 'normal'))
    Score_board.goto(-220, 250)
    Score_board.write('Level: ' + str(game['present_level']), font=('Times New Roman', 12, 'normal'))

def collision(obj1, obj2):
    distance = obj1['turtle'].distance(obj2['turtle'])
    return distance <= obj1['radius'] + obj2['radius']

def animating():
    Start_Screen.clear()
    game_loop()

def game_loop():
    if game['remaining_lives'] < 1:
        show_game_over()
        return

    Score_board.clear()
    Positive_object['turtle'].clear()
    player['turtle'].clear()
    asteroid_object['turtle'].clear()

    game['frames'] += 1

    if player['turtle'].ycor() > (vertical / 2) + player['radius']:
        player['turtle'].sety((-vertical / 2) - player['radius'])
    elif player['turtle'].ycor() < (-vertical / 2) - player['radius']:
        player['turtle'].sety((vertical / 2) + player['radius'])

    if player['turtle'].xcor() > (horizontal / 2) + player['radius']:
        player['turtle'].setx((-horizontal / 2) - player['radius'])
    elif player['turtle'].xcor() < (-horizontal / 2) - player['radius']:
        player['turtle'].setx((horizontal / 2) + player['radius'])

    new_y_cordinate = asteroid_object['turtle'].ycor() - asteroid_object['speed'] * game['present_level']
    new_x_cordinate = random.randint(-int(horizontal / 2), int(horizontal / 2))
    asteroid_object['turtle'].goto(asteroid_object['turtle'].xcor(), new_y_cordinate)

    if asteroid_object['turtle'].ycor() <= (-vertical / 2):
        asteroid_object['turtle'].goto(new_x_cordinate, vertical / 2)

    new_y2_cordinate = Positive_object['turtle'].ycor() - Positive_object['speed'] * game['present_level']
    new_x2_cordinate = random.randint(-int(horizontal / 2), int(horizontal / 2))
    Positive_object['turtle'].goto(Positive_object['turtle'].xcor(), new_y2_cordinate)

    if Positive_object['turtle'].ycor() <= (-vertical / 2):
        Positive_object['turtle'].goto(new_x2_cordinate, vertical / 2)

    for obj in [asteroid_object, Positive_object]:
        if collision(obj, player):
            if obj['type'] == 'asteroid':
                game['remaining_lives'] -= 1
            elif obj['type'] == 'Positive':
                game['score'] += game['Positive_points']
                if game['score'] % game['level_increase'] == 0:
                    game['present_level'] += 1
                    Positive_object['speed'] += 0.2
                    player['speed'] += 0.2
                    asteroid_object['speed'] += 0.2
                elif game['frames'] % 4000 == 0:
                    player['speed'] += 0.2
                    asteroid_object['speed'] += 0.2
                    Positive_object['speed'] += 0.2
            newxcordinate = random.randint(-int(horizontal / 2), int(horizontal / 2))
            newycordinate = vertical / 2
            obj['turtle'].penup()
            obj['turtle'].goto(newxcordinate, newycordinate)
            obj['turtle'].pendown()

    game_data()
    animation.update()
    animation.ontimer(game_loop, 1000 // 60)

def show_instructions():
    Start_Screen.hideturtle()
    Start_Screen.penup()
    Start_Screen.color("blue")
    Start_Screen.goto(0, 220)
    Start_Screen.pendown()
    Start_Screen.write("Project - 2 Game.", align="center", font=('Times New Roman', 14, 'normal'))
    Start_Screen.penup()
    Start_Screen.sety(Start_Screen.ycor() - 30)
    Start_Screen.pendown()
    Start_Screen.write("Collect lives to gain points, collision ends the game.", align="center", font=('Times New Roman', 14, 'normal'))
    Start_Screen.penup()
    Start_Screen.sety(Start_Screen.ycor() - 30)
    Start_Screen.pendown()
    Start_Screen.write("Press Space Bar to start the game.", align="center", font=('Times New Roman', 14, 'normal'))
    Start_Screen.penup()
    Start_Screen.sety(Start_Screen.ycor() - 430)
    Start_Screen.pendown()
    Start_Screen.color("black")
    Start_Screen.write("Use W, A, S, D or Arrow keys to move across", align="center", font=('Times New Roman', 14, 'normal'))

def show_game_over():
    for obj in [asteroid_object, Positive_object, player]:
        obj["turtle"].clear()
        if obj.get("image", "") != "":
            obj["turtle"].hideturtle()

    animation.update()
    Score_board.clear()
    Start_Screen.clear()
    Start_Screen.hideturtle()
    Start_Screen.penup()
    Start_Screen.color("red")
    Start_Screen.goto(0, 0)
    Start_Screen.pendown()
    Start_Screen.write("Game Over.", align="center", font=('Times New Roman', 26, 'normal'))
    Start_Screen.penup()
    Start_Screen.sety(Start_Screen.ycor() - 30)
    Start_Screen.pendown()
    Start_Screen.write("Score: " + str(game['score']), align="center", font=('Times New Roman', 16, 'normal'))

def main():
    show_instructions()

animation.onkey(animating, "space")
animation.listen()
main()

animation.mainloop()
