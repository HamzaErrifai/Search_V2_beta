import os
from classes.History import History
from classes.Search import Search
from classes.Alert import Alert

# TODO : make a way that the window will itself depending on the content
line_count = 0
with open("data\\data.json") as file:
    for line in file:
        if line != "\n":
            line_count += 1


MAX_Width = 77
consoleW = 77
consoleH = line_count+1


def main():
    try:
        os.system(f"mode con: cols={consoleW} lines={consoleH}") # set the size of the window
        print("Search_Beta_V2".center(MAX_Width, "_").upper(), end='\n\n')
        print("Type '--help' for help\t'--exit' to exit", end='\n\n')
        History().show() # Show the history
        word = input("Search >> ".upper())
        while(not word):  # To prevent searching null values
            word = input("Search >> ".upper())
        search = Search(word)
        return search.start()
    except:
        Alert("error",'UNKNOWN ERROR ENCOUNTERED')
        return False


if not os.path.exists("save"):
    os.mkdir("save")

while main():
    pass
