from PySide2.QtWidgets import QMessageBox
import re

# ================ Validation Class ================
class Validation:
    def __init__(self, function_input, min_input, max_input):
        self.function_input = function_input.lower().strip()
        self.min_input = min_input
        self.max_input = max_input


    def validate(self):
        # Check if the function input is empty or whitespace
        if self.function_input == "" or self.function_input == " ":
            raise_error('The Function Input Cannot Be Empty', "Empty Function")
            return False
        

        # Check if the min input is empty or whitespace
        if self.min_input == "" or self.min_input == " ":
            raise_error('The Minimum Value Input Cannot Be Empty', "Empty Min Value")
            return False
        

        # Check if the max input is empty or whitespace
        if self.max_input == "" or self.max_input == " ":
            raise_error('The Maximum Value Input Cannot Be Empty', "Empty Max Value")
            return False
        

        # Check if the min value contains a numeric value
        if not self.is_numeric(self.min_input):
            raise_error("Please enter numbers in Minimum Value Input Field.", "Invalid Input")
            return False
        else:
            self.min_input = float(self.min_input)
        

        # Check if the max value contains a numeric value
        if not self.is_numeric(self.max_input):
            raise_error("Please enter numbers in Maximum value Input Field.", "Invalid Input")
            return False
        else:
            self.max_input = float(self.max_input)
    

        # Check if the min value is greater than or equal to the max value
        if self.min_input >= self.max_input:
            raise_error("Minimum value must be less than Maximum value.", "Invalid Input")
            return False
        

        # Check if the function input contains double asterisks
        if self.contains_double_ast(self.function_input):
            raise_error("Please make sure to use a valid math expression", "Invalid Expression")
            return False


        if not self.security_check(): 
            return False


        # Replace '^' with '**' for exponentiation
        self.function_input = self.function_input.replace("^", "**")
        return True



    def is_numeric(self, input_str):
        numeric_pattern = r'^[-+]?[0-9]*\.?[0-9]+$'
        return re.match(numeric_pattern, input_str) is not None
    


    def contains_double_ast(self, string):
        return "**" in string
    


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
            if word in self.function_input:
                raise_error(f"'{word}' is blocked. Be Ethical!!!\n\nUse Mathematical Expressions Only.", "Security Alert")
                return False
        return True

# ================ End of Class ================

def raise_error(err_msg, title):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Critical)
    msg_box.setWindowTitle(title)
    msg_box.setText(err_msg)
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.exec_()

