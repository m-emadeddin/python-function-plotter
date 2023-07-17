import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from utils.UI_MainWIndow import Ui_MainWindow
from utils.validation import Validation
from plotter import Plotter

class FunctionPlotterWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.plot_button.clicked.connect(self.plot)

    def plot(self):
        function_str = self.function_input.text()
        min_input = self.min_input.text()
        max_input = self.max_input.text()
        input = Validation(function_str, min_input, max_input)

        # Plotting section 
        if input.validate():
                plotter = Plotter(input.function_input, input.min_input, input.max_input)
                try:
                    plotter.getValues()
                    self.gridLayout_3.addWidget(plotter.canvas, 0, 0, 1, 1)  # Add the canvas to the canvas widget
                    plotter.figure.clear()
                    plotter.plot()
                except Exception :
                    plotter.figure.clear()
                    plotter.display_error()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FunctionPlotterWindow()
    window.show()
    sys.exit(app.exec_())
