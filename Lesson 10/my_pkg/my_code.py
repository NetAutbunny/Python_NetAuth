# creating a module named` my_code.py` in the `my_pkg` package

# using _name_ to separate executable code from importable code

# Printing 'hello world' in the executable section
if __name__ == "__main__":
    print("hello world")

 # creating a function that prints the text 'some message' in the importable section
def print_message():
    """
    Prints a predefined message.
    """
    print("some message")

