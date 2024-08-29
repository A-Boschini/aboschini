# Using Dunder init and instance atributes
class Snake:
    """Snake main blueprint"""
    def __init__(self, name):
        self.name = name

    def modifyName(self, newName):
        self.name = newName

#Objects
anaconda01 = Snake("Anaconda")
python01 = Snake("Python")  

#Printing the value of name for the two objects
print(anaconda01.name)
print(python01.name)