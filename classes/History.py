import os
from .Shortcut import Shortcut

class History(Shortcut):
    def __init__(self):
        self.saveFile = "save/history.json"
        super().__init__("History", self.saveFile)

    def clear(self):
        f = open(self.saveFile, 'w')
        f.close()
        os.system('cls')
        return True

    def add(self, word):
        try:
            listHisto = super().get()
            if not (word in listHisto):
                listHisto.append(word)
                
        except:
            listHisto = []
            listHisto.append(word)
        finally:
            super().save(listHisto)

    def show(self):
        ps = super().get()  # this time its a list
        if ps:
            print("history : ".upper())
            for p in ps:
                print("\t"+p)
