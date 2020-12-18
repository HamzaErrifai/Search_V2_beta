import os
import pathlib
from classes.History import History
from classes.Search import Search
from classes.Alert import Alert

def main():
    try:
        MAX_Width = 70
        # MAX_HEIGHT = 40
        # line_count = 0
        # set the size of the window
        # with open(str(pathlib.Path(__file__).parent.absolute())+"\\data\\data.json") as file:
        #     for line in file:
        #         if line != "\n":
        #             line_count += 1
        # consoleH = line_count+1

        # set the size of the window
        # os.system(f"mode con: cols={MAX_Width} lines={MAX_HEIGHT}")
        print("Search_Beta_V2".center(MAX_Width, "_").upper(), end='\n\n')
        print("Type '--help' for help\t'--exit' to exit", end='\n\n')
        History().show()  # Show the history
        word = input("Search >> ".upper())
        while(not word):  # To prevent searching null values
            word = input("Search >> ".upper())
        search = Search(word)
        return search.start()
    except:
        Alert("error", 'UNKNOWN ERROR ENCOUNTERED')
        return False


if not os.path.exists("save"):
    os.mkdir("save")

while main():
    pass
