import turtle
import pandas

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
screen = turtle.Screen()
screen.title("U.S.States game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
guessed = []
missed = []
score = 0
while len(guessed) < 50:
    answer_state = screen.textinput(title=f"{len(guessed)}/50 are correct", prompt="What is other state name")
    answer = answer_state.title()
    if answer == "Exit":
        break
    if answer in all_states:
        guessed.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)

for state in all_states:
    if state not in guessed:
        missed.append(state)

new_data = pandas.DataFrame(missed)
new_data.to_csv("Missed states.csv")
