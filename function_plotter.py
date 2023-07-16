import sys
import numpy as np
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from sympy import symbols, lambdify
from utils.UI_MainWIndow import Ui_MainWindow
from utils.validation import Validation

class FunctionPlotterWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Link the plot button to method PLOT
        self.plot_button.clicked.connect(self.plot)


    def plot(self):
        
        function_str = self.function_input.text().lower().strip()
        min_input = self.min_input.text()
        max_input = self.max_input.text()
        input = Validation(function_str, min_input, max_input)

        # function input string : replacing ^ with ** for exp operation in python
        function_str = function_str.replace("^", "**")
        # Plotting section 
        if input.validate():
            try:
                x = symbols('x')
                function = lambdify(x, function_str)
                min_val = float(min_input)
                max_val = float(max_input)
                x_vals = np.linspace(min_val, max_val, 100)
                y_vals = function(x_vals)
                self.figure = Figure(facecolor='lightblue')
                self.canvas = FigureCanvas(self.figure)
                self.gridLayout_3.addWidget(self.canvas, 0, 0, 1, 1)  # Add the canvas to the canvas widget
                self.figure.clear()
                ax = self.figure.add_subplot(111)
                ax.plot(x_vals, y_vals)
                ax.set_xlabel('x')
                ax.set_ylabel('y')
                ax.set_title('Function Plot')
                ax.set_facecolor('white')
                self.canvas.draw()

            except Exception :
                msg = "\nPlease make sure of using a valid math expression.\n\nNote: only variable 'x' is allowed."
                self.display_error(msg)


    # error message function
    def display_error(self, message):
        QMessageBox.warning(self, 'Error', message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FunctionPlotterWindow()
    window.show()
    sys.exit(app.exec_())
