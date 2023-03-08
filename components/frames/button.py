from tkinter.ttk import *


class ButtonFrame(Frame):
    def __init__(self, parent, ExexCallback) -> None:
        super().__init__(parent)
        self.StartCommand = ExexCallback
        self.CreateWidgets()

    def CreateWidgets(self):
        self.startButton = Button(self, text="Start Game", width=20, padding="0 10 0 10", command=self.StartCommand,
                            takefocus=False).pack(expand=True)
