import tkinter as tk

# Create a new class called Calculator that inherits from the tk.Tk class
class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set the title of the calculator window to "Calculator"
        self.title("Simple Calculator")
        self.geometry("400x300")

        # Create a StringVar object to store the current equation
        self.equation = tk.StringVar()

        # Call the create_widgets method to create the widgets for the calculator
        self.create_widgets()

    # Define the create_widgets method
    def create_widgets(self):
        # Create an Entry widget to serve as the screen of the calculator
        screen = tk.Entry(self, textvariable=self.equation, bd=8, font=("arial", 20, "bold"), justify="right")
        screen.grid(row=0, column=0, columnspan=4)

        # Define a list of tuples, where each tuple contains a button label and its grid coordinates
        buttons = [("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
                   ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
                   ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
                   ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3), ("C", 5, 3)]

        # Iterate over each tuple in the buttons list
        for button in buttons:
            # Create a Button widget with the specified label, size, and command
            b = tk.Button(self, text=button[0], width=6, height=2, command=lambda text=button[0]: self.click(text))
            b.grid(row=button[1], column=button[2])

    # Define the click method
    def click(self, text):
        # Check if the button label is "="
        if text == "=":
            # Evaluate the current equation and set the StringVar object self.equation to the result
            try:
                self.equation.set(eval(self.equation.get()))
            except:
                self.equation.set("Error")
        # Check if the button label is "C"
        elif text == "C":
            # Set the StringVar object self.equation to an empty string
            self.equation.set("")
        # If the button label is not "=" or "C", append the button label to the current equation
        else:
            self.equation.set(self.equation.get() + text)

# Create a new instance of the Calculator class and start the main event loop
if __name__ == "__main__":
    app = Calculator()
    app.mainloop()