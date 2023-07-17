import numpy as np
from sympy import symbols, lambdify
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Plotter():
    def __init__(self, function_str, min_input, max_input):
        self.function_str = function_str
        self.min_input = min_input
        self.max_input = max_input

        # Creating Figure
        self.figure = Figure(facecolor='lightblue')
        self.canvas = FigureCanvas(self.figure)

    def getValues(self):
        x = symbols('x')
        function = lambdify(x, self.function_str)
        min_val = float(self.min_input)
        max_val = float(self.max_input)
        self.x_vals = np.linspace(min_val, max_val, 100)
        self.y_vals = function(self.x_vals)

    def plot(self):
        fig = self.figure.add_subplot(111)
        fig.plot(self.x_vals, self.y_vals)
        fig.set_xlabel('x')
        fig.set_ylabel('y')
        fig.set_title('Function Plot')
        fig.set_facecolor('white')
        self.canvas.draw()

