import numpy as np
from sympy import symbols, lambdify
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide2.QtWidgets import QApplication, QMainWindow
from matplotlib.figure import Figure
from PySide2.QtWidgets import QMessageBox

class Plotter:
    def __init__(self):

        # Creating Figure
        self.figure = Figure(facecolor='lightblue')
        self.canvas = FigureCanvas(self.figure)


    def get_values(self, expression, min_x, max_x):
        expression
        # Convert the function string to a lambda function
        x = symbols('x')
        function = lambdify(x, expression)

        # Convert the min and max input to floats
        min_val = float(min_x)
        max_val = float(max_x)

        # Generate x and y values for plotting
        self.x_vals = np.linspace(min_val, max_val, 100)
        self.y_vals = function(self.x_vals)


    def plot(self):
        # Plot the function
        fig = self.figure.add_subplot(111)
        fig.plot(self.x_vals, self.y_vals)
        fig.set_xlabel('x')
        fig.set_ylabel('y')
        fig.set_title('Function Plot')
        fig.set_facecolor('white')
        self.canvas.draw()
    
    def display_error(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle('Error')
        msg_box.setText("\nPlease make sure to use a valid math expression.\n\nNote: only variable 'x' is allowed.")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()
