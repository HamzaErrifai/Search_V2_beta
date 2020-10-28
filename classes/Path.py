from .Shortcut import Shortcut

class Path(Shortcut):
    def __init__(self):
        super().__init__("path","save/path.json")