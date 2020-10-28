from .Alert import Alert
from .GetJson import GetJson
import os


class Shortcut():
    def __init__(self, scName, saveFile):
        self.saveFile = saveFile
        self.scName = scName
        if not os.path.isfile(self.saveFile):
            f = open(self.saveFile, 'w+')
            f.write('')
            f.close()

    def save(self, var):  # write to the json file
        GetJson.write(self.saveFile, var)

    def add(self, newPath):  # Shortcut
        pathsDict = GetJson.parse(self.saveFile)  # get the dictionnary
        newPath = str(newPath)

        name = str(input("Enter the name: "))
        while(not name):  # To prevent searching null values
            name = str(input("Enter the name: "))
        name = name.lower()

        if newPath in pathsDict.values():
            Alert("Alert", "{} already exists".format(newPath))
            return

        if name in pathsDict:  # if the key already exists
            Alert("Alert", "{} already exists".format(name))
            return

        pathsDict[name] = newPath
        self.save(pathsDict)
        Alert("Success", "'{}' added successfully".format(newPath))

    def delete(self, pathName):  # needs to be recreated
        pathsDict = GetJson.parse(self.saveFile)  # get the dictionnary
        try:
            pathsDict.pop(pathName)
            self.save(pathsDict)
            Alert("Success", "'{}' deleted successfully".format(pathName))
        except:
            Alert("Error", "'{}' not found!".format(pathName))

    def get(self):
        return GetJson.parse(self.saveFile)  # dict

    def show(self):
        ps = self.get()  # Dictionnary
        os.system("cls")
        print(self.scName+"s: ")
        for keys, values in sorted(ps.items()):  # print dict sorted by keys
            print("\t"+keys+": "+values+"\n")
        input("Press 'ENTER' to Continue...")
        os.system("cls")
