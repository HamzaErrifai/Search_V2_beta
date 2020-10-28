import os


class Alert:
    def __init__(self, flag, message):
        os.system("cls")
        print("[{}]: {}".format(flag.upper(), message))
        input("\nPress 'ENTER' to Continue...")
        os.system("cls")
