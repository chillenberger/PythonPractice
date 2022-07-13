from tkinter import *
from tkinter import filedialog
from pathlib import Path

#  All important variables here to simplify reading my code
directory = None
path = None
save = None
room = None


def main():

    path = "StackOverflow/assets/logdata.txt"

    save = open(path, 'r+')
    lines = save.readlines()
    save.close()

    print(lines)
    lines[0] = f"room={str(room)}"
    print(lines)

    save = open(path, 'w+')
    save.writelines(lines)
    save.close()

if __name__ == '__main__':
    main()