import os
import json
from .Alert import Alert


class GetJson:
    @staticmethod
    def parse(file):
        if os.path.isfile(file):
            if not os.stat(file).st_size == 0:
                f = open(file, "r")
                dictData = json.load(f)
                f.close()
                return dictData
            else:
                return {}

        else:
            Alert("ERROR", "file does not exist (json: data)")

    @staticmethod
    def write(file, value):
        if os.path.isfile(file):
            with open(file, 'w') as f:
                f.write(json.dumps(value))  # writes a string of json
        else:
            Alert("ERROR", file + " does not exist")
