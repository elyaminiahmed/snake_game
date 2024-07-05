import turtle
import time
import random

# Game configuration
delay = 0.1
score = 0
high_score = 0

# Set up the screen
screen = turtle.Screen()
screen.title("Snake Game by Anonymous")
screen.bgcolor("#000090")
screen.setup(width=600, height=600)
screen.cv._rootwindow.resizable(False, False)
screen.tracer(0)

# Snake head
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food_colors = ["red", "green", "black"]
food_shapes = ["square", "circle"]
food.shape(random.choice(food_shapes))
food.color(random.choice(food_colors))
food.penup()
food.goto(0, 100)

# Score display
score_display = turtle.Turtle()
score_display.shape("square")
score_display.color("red")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 250)
score_display.write("Score: 0  High Score: 0", align="center", font=("Arial", 24, "bold"))

# Key bindings
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

screen.listen()
screen.onkeypress(go_up, "z")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_left, "q")
screen.onkeypress(go_right, "d")

# Snake body
segments = []

# Game reset function
def reset_game():
    global score, delay
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"
    food.shape(random.choice(food_shapes))
    food.color(random.choice(food_colors))
    for segment in segments:
        segment.goto(1000, 1000)  # Move off-screen
    segments.clear()
    score = 0
    delay = 0.1
    score_display.clear()
    score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Arial", 24, "bold"))

# Main game loop
while True:
    screen.update()

    # Check for border collision
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        reset_game()

    # Check for food collision
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # Add segment
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("orange")
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        score_display.clear()
        score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Arial", 24, "bold"))

    # Move segments in reverse order
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)
    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Check for body collision
    for segment in segments:
        if segment.distance(head) < 20:
            reset_game()

    time.sleep(delay)
