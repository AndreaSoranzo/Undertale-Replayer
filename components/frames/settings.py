from tkinter import *
from tkinter.ttk import *


class SettingsFrame(Frame):

    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.isNoHitActivated = IntVar()
        self.isNoHitActivated.set(0)
        self.playerName = StringVar()
        self.CreateWidgets()

    def CreateWidgets(self):
        Label(self, text="Enter your name", style="sub.TLabel",
              justify="center").pack(side="left")
        Entry(self, width=30, font=("arial", 11, "bold"), textvariable=self.playerName,
              justify="center").pack(side="left", padx=40)
        Checkbutton(self, text="No Hit Mode", variable=self.isNoHitActivated,
                    onvalue=1, offvalue=0, takefocus=False).pack()

    def GetPlayerName(self):
        return self.playerName.get()[0:6]

    def GetHitMode(self):
        return self.isNoHitActivated.get()
