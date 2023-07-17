from PySide2.QtWidgets import QMessageBox, QApplication
import re

class Validation:
    def __init__(self, function_input, min_input, max_input):
        self.function_input = function_input.lower().strip()
        self.min_input = min_input
        self.max_input = max_input
    
    def validate(self):
        if self.function_input == "" or self.function_input == " ":
            raiseError('The Function Input Cannot Be Empty', "Empty Function")
            return False
        if self.min_input == "" or self.min_input == " ":
            raiseError('The Minimum Value Input Cannot Be Empty', "Empty Min Value")
            return False
        
        if self.max_input == "" or self.max_input == " ":
            raiseError('The Maximum Value Input Cannot Be Empty', "Empty Max Value")
            return False
        
        try:
            self.min_input = float(self.min_input)
        except Exception:
            raiseError("Please enter numbers in Minimum Value Input Field.", "Invalid Input")
            return False
        
        try:
            self.max_input = float(self.max_input)
        except Exception:
            raiseError("Please enter numbers in Maximum value Input Field.", "Invalid Input")
            return False
    
        if self.min_input >= self.max_input:
            raiseError("Minimum value must be less than Maximum value.", "Invalid Input")
            return False
        
        if self.isDoubleAst(self.function_input):
            raiseError("Please make sure to use a valid math expression", "Invalid Expression")
            return False

        if not self.security_check() : 
            return False

        self.function_input = self.function_input.replace("^", "**")
        return True

    def isDoubleAst(self, str):
        return "**" in str
    
    def security_check(self):
        dangerous_keywords = [
            'eval',
            'exec',
            'pickle',
            'subprocess',
            'os',
            'open',
            'fileinput',
            'execfile',
            'reload',
            '__import__',
            ';'
        ]
        for word in dangerous_keywords:
            if word in self.function_input :
                raiseError(f"'{word}' is blocked. Be Ethical!!!\n\nUse Mathematical Expressions Only.", "Security Alert")
                return False
        return True


def raiseError(errMsg, title):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Critical)
    msg_box.setWindowTitle(title)
    msg_box.setText(errMsg)
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.exec_()


if __name__ == "__main__":
    input = Validation("x", -10, 10)
    print(input.function_input)
    print(input.min_input)
    print(input.max_input)
    print(input.validate())