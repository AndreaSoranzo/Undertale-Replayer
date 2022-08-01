from tkinter import *
from tkinter.ttk import *
from components.customWidgets.boss_card import BossCard


class BossGridFrame(Frame):
    rowCount = 0
    reminder = 0

    def __init__(self, parent, listPath, items_per_row) -> None:
        super().__init__(parent)
        self.selectedValue = IntVar()
        self.listPath = listPath
        self.items_per_row = items_per_row
        self.columnconfigure(0, weight=1)
        self.CreateWidgets()

    def CreateWidgets(self):

        for i in range(len(self.listPath)):
            reminder = i % self.items_per_row
            if (reminder == 0):
                self.rowCount += 1
            BossCard(
                self, self.listPath[i][1], self.listPath[i][0], self.selectedValue, i).grid(column=reminder, row=self.rowCount, padx=30, sticky="s")

    def GetbossID(self):
        return self.selectedValue.get()
