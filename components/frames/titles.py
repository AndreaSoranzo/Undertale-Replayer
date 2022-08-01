from tkinter.ttk import *


class TitlesFrame(Frame):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.CreateWidgets()

    def CreateWidgets(self):
        Label(self, text="Undertale Replayer", justify="center").pack()
        Label(self, text="An undertale boss replayer software",
              style="sub.TLabel", justify="center").pack()
