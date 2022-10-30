from tkinter import *
from tkinter.ttk import *


class BossCard(Frame):
    def __init__(self, parent, imagePath, title, checkVariable, boss_id) -> None:
        super().__init__(parent)
        self.imagePath = imagePath
        self.title = title
        self.checkVariable = checkVariable
        self.boss_id = boss_id
        self.resizer_multiplyer = 1.5
        self.CreateWidgets()

    def CreateWidgets(self):
        self.boss_image = PhotoImage(file=self.imagePath)
        Label(self, image=self.boss_image).pack(side="top", pady=20)
        Label(self, text=self.title, style="sub.TLabel", wraplength=200,
              justify="center").pack()
        Checkbutton(self, variable=self.checkVariable, onvalue=self.boss_id,
                    offvalue=-1, takefocus=False).pack(side="bottom", pady=15)
