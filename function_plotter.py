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
        # Get input data from the UI
        function_str = self.function_input.text()
        min_input = self.min_input.text()
        max_input = self.max_input.text()

        # Perform input validation
        input_data = Validation(function_str, min_input, max_input)
        if input_data.validate():
            # Create a Plotter instance
            plotter = Plotter(input_data.function_input, input_data.min_input, input_data.max_input)
            try:
                # Generate plot
                plotter.get_values()
                self.gridLayout_3.addWidget(plotter.canvas, 0, 0, 1, 1)
                plotter.figure.clear()
                plotter.plot()
            except Exception:
                # Display error message if an exception occurs during plotting
                plotter.figure.clear()
                plotter.display_error()


def main():
    # Create the application and window instance
    app = QApplication(sys.argv)
    window = FunctionPlotterWindow()

    # Show the window and start the application event loop
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
