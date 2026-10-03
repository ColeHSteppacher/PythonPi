import random as random
import PySimpleGUI as sg

# Function to calculate the value of pi using the Monte Carlo method
# This uses the area of a circle to calculate pi
# x^2 + y^2 = 1 graphs a circle with radius 1. Values of x and y are generated between 0 and 1. if x^2 + y^2 <=1, then the point is inside the circle.
#By dividing the points inside by the total number of points, we can calculate an approximation of pi/4.

def calculate_pi(num_samples):
    inside_circle = 0
    for sample in range(num_samples):
        x,y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            inside_circle += 1
    return (inside_circle / num_samples) * 4

introlayout = [[sg.Text("Monte Carlo Simulation to Calculate Pi")], [sg.Input(default_text="10000")], [sg.Button("Calculate")]]

window = sg.Window("Monte Carlo Simulation", introlayout)

while True:
    event, values = window.read()
    if event == "Calculate":
        pi = calculate_pi(int(values[0]))
        sg.popup(pi)
    if event == sg.WIN_CLOSED:
        break