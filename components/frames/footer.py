from tkinter.ttk import *


class FooterFrame(Frame):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.CreateWidgets()

    def CreateWidgets(self):
        Label(self, text="Made by If_Jay",
              style="fut.TLabel", justify="center").pack()
