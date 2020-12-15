import os
from .Alert import Alert
from .Path import Path


class File():
    def __init__(self):
        self.savePath = "E:\\Projects\\Python\\Search_V2_beta\\externalscripts\\"
        if not os.path.exists(self.savePath):
            os.mkdir(self.savePath)

    def add(self, newFile):
        name = newFile
        newFile += ".py"
        if not os.path.exists(self.savePath+newFile):
            # create the file
            f = open(self.savePath+newFile, 'w+')
            f.write("# Your code Here")
            f.close()
            Path().addWithName(self.savePath+newFile, name)
            os.system("start notepad "+self.savePath+newFile)
        else:
            self.edit(newFile)

    def edit(self, fileName):
        os.system("start notepad "+self.savePath+fileName)

    def delete(self, fileName):
        name = fileName
        fileName += ".py"
        if os.path.exists(self.savePath + fileName):
            os.remove(self.savePath + fileName)
            Path().delete(name)
        else:
            Alert("error", "This file does NOT exists!")
