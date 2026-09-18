import turtle
import pandas
import namewriter

screen = turtle.Screen()
tim = turtle.Turtle()
name_writer = namewriter.NameWriter()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)
tim.shape(image)

states_data = pandas.read_csv("50_states.csv")
# print(states_data)

states_name_list = states_data["state"].to_list()
# print(states_name_list)

correct_guesses = 0
correct_states = []
while correct_guesses < 51:

    input_title = f"{correct_guesses}/50 States Correct"
    answer_state = screen.textinput(title=input_title, prompt="What's another state's name?")
        # print(answer_state)

    title_answer_state = answer_state.title()

    if title_answer_state == "Exit":
        break
    # print(title_answer_state)

    if title_answer_state in states_name_list:
        # print("You got it!")
        correct_guesses += 1
        screen.title(f"{correct_guesses}/50 States Correct")
        name_writer.write_name(title_answer_state, int(states_data[states_data["state"] == title_answer_state]["x"].iloc[0]), int(states_data[states_data["state"] == title_answer_state]["y"].iloc[0]))
        correct_states.append(title_answer_state)

# states_to_learn

states_to_learn = []
for state in states_name_list:
    if state not in correct_states:
        states_to_learn.append(state)

print(states_to_learn)
new_data = pandas.DataFrame(states_to_learn, columns=["States to Learn"])
print(new_data)
new_data.to_csv("states_to_learn.csv")