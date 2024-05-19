import turtle
import pandas

screen=turtle.Screen()
screen.title("US States Game")

image="blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")

states=data["state"].to_list()      #create a list of states from csv file

guessed_states=[]


while len(guessed_states)<50:
    answer_state=screen.textinput(f"{len(guessed_states)}/50 States","What's another state's name?").title()        #create an input for state guess, make it first letter Capital
    
    if answer_state=="Exit":    #if you type "Exit" program will end and create a csv file of states that you didn't guess
        states_to_learn=[]      #create an empty list of not guessed states
        
        for state in states:
            if state not in guessed_states:
                states_to_learn.append(state)
                
        new_data=pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")      #create states to learn file
        break       #end this program
    
    if answer_state in states:      #if you guessed a state
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data["state"]==answer_state]
        t.goto(x=int(state_data["x"]),y=int(state_data["y"]))       #add a name of the guessed state on a map
        t.write(answer_state)
        
        
        


screen.exitonclick()