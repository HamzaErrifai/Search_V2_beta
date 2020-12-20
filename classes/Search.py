import os
import webbrowser
from .Alert import Alert
from .Path import Path
from .Sc import Sc
from .History import History
from .Help import Help
from .GetJson import GetJson
from .File import File


class Search:
    def __init__(self, word):
        self.cmds = GetJson.parse("data/data.json")
        self.word = str(word).strip()
        self.histo = History()
        self.path = Path()  # all the paths
        self.sc = Sc()  # all the scs
        self.file = File()
        self.domains = ['.com', '.tv', '.net', '.org']

    def private(self):
        url = input('enter a url: ')
        os.system("start chrome /incognito {}".format(url))
        return False

    def exit(self):
        return False

    def rm(self, what):
        stmt = "rm -"+what+" "
        print(stmt)
        stop = self.word.find(stmt) + len(stmt)
        getattr(self, what).delete(self.word[stop:])
        return True

    def add(self, what):
        stop = self.word.find(f"{what} ") + len(f"{what} ")
        getattr(self, what).add(self.word[stop:])
        return True

    def getWhat(self, what):
        whatDict = getattr(self, what).get()
        try:
            if(what == "sc"):
                webbrowser.open(
                    'https://{}'.format(whatDict[self.word.lower()]), new=2)
                return False
            if(what == "path"):
                os.startfile(whatDict[self.word.lower()])
                return False
        except:
            pass
        return True

    def showWhat(self, what):
        if(what == "clc" or what == "cls"):
            return self.histo.clear()
        elif(what == "yt"):
            return self.getYt()
        elif what.startswith("--"):
            stop = what.find("--") + len("--")
            return getattr(self, what[stop:])()
        else:
            getattr(self, what).show()
        return True

    def getYt(self):
        if(self.word.startswith("yt ")):
            stop = self.word.find("yt") + len("yt ")
            webbrowser.open(
                f"https://www.youtube.com/results?search_query={self.word[stop:]}", new=2)
        else:
            webbrowser.open("https://www.youtube.com/", new=2)
        return False

    def start(self):
        if(Alert.prompt()):
            self.histo.add(self.word)  # add the word to the history
            # Search for commands in the word matching in the data file
            for cmdKey in self.cmds.keys():
                if(cmdKey == self.word.lower()):
                    return self.showWhat(self.word.lower())
                elif self.word.find(f"{cmdKey} ") != -1:
                    if(self.word.startswith("yt")):
                        return self.getYt()
                    elif not self.word.find(f" -") != -1:
                        return self.add(cmdKey)
                    else:
                        for sKey in self.cmds[cmdKey].keys():
                            if(self.cmds[cmdKey][sKey] and (sKey == "options")):
                                for i in range(len(self.cmds[cmdKey][sKey])):
                                    if self.word.find("-"+self.cmds[cmdKey][sKey][i]) != -1:
                                        return self.rm(self.cmds[cmdKey][sKey][i])

            if not self.getWhat("path") or not self.getWhat("sc"):
                return False

            if self.word.find("https://".lower()) != -1:
                webbrowser.open('{}'.format(self.word), new=2)
                return False

            for domain in self.domains:
                if domain in self.word.lower():
                    webbrowser.open(f"https://{self.word}", new=2)
                    return False

            webbrowser.open(
                f"https://www.google.com/search?q={self.word}&ie=UTF-8", new=2)
            return False
        else:
            return True

    def help(self):
        os.system("cls")
        Help().getHelp()
        input("Press 'ENTER' to Continue...")
        os.system("cls")
        return True
