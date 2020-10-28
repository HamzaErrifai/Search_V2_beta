from .GetJson import GetJson


class Help():
    def __init__(self):
        self.saveFile = "data/data.json"

    def getHelp(self):
        data = GetJson.parse(self.saveFile)  # get the data from the json file
        for pKey in data.keys():
            print(pKey, end=":\n")
            for sKey in data[pKey].keys():
                if(data[pKey][sKey]):
                    print(f"\t{sKey}: ", end="")
                    if(sKey == "options"):  # important to format the options with a '-'
                        for i in range(len(data[pKey][sKey])):
                            print(f"-{data[pKey][sKey][i]}", end="\t")
                    else:
                        print(data[pKey][sKey])
                print()
