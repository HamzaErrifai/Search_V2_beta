import os

class Window:
    def __init__(self):
        self.MAX_Width = 77
        self.consoleW = 77
        self.consoleH = self.countFileLn("data\\data.json")
        os.system(f"mode con: cols={self.consoleW} lines={self.consoleH}")

    def countFileLn(self, fName):
        line_count = 0
        with open(fName) as file:
            for line in file:
                if line != "\n":
                    line_count += 1
        return line_count
        
