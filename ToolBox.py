import pip._vendor.colorama
from pip._vendor.colorama import Fore

class Toolbox:
    def InputInt(self, inputMessage):
        inputString: str = ""
        while True:
            inputString = input(inputMessage)
            if inputString.isdigit:
                return int(inputString)
            else:
                print("This is not a number")
    def InputFloat(self, inputMessage):
        number: float = 0.0
        inputString: str = ""
        while True:
            inputString = input(inputMessage)
            if inputString.isdigit:
                return float(inputString)
            else:
                print("It is not a number!")

    def InputAny(self, inputMessage):
        inputString = input(inputMessage)
        return inputString

    def BoolInput(self, inputMessage):
        while True:
            inputString = input(inputMessage).lower()
            if inputString == "y" or inputString == "yes":
                return True
            elif inputString == "n" or inputString == "no":
                return False
            else:
                print("Wrong answer!")
    def InputIntBetween(self, message, min, max):
        while True:
            outNumber = InputInt(message)
            if outNumber >= min and outNumber <= max:
                return outNumber
    def WriteLineBlue(self, text):
        print(Fore.BLUE, text)

    def WriteBlue(self, text):
        print(Fore.BLUE, text, end="")

    def WriteLineRed(self, text):
        print(Fore.RED, text)

    def WriteRed(self, text):
        print(Fore.RED, text, end="")

    def WriteLineGreen(self, text):
        print(Fore.GREEN,text, end="")
        
    def WriteGreen(self, text):
        print(Fore.GREEN,text, end="")
