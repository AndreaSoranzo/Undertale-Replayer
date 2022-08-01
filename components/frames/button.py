from gc import callbacks
from subprocess import call
from tkinter.ttk import *


class ButtonFrame(Frame):
    def __init__(self, parent, command) -> None:
        super().__init__(parent)
        self.command = command
        self.CreateWidgets()

    def CreateWidgets(self):
        self.button = Button(self, text="Start Game", width=20, padding="0 10 0 10", command=self.command,
                             takefocus=False).pack(expand=True)
