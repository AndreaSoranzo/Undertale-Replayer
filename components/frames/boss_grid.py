from tkinter import *
from tkinter.ttk import *
from components.customWidgets.boss_card import BossCard


class BossGridFrame(Frame):

    def __init__(self, parent, listPath, items_per_row) -> None:
        super().__init__(parent)
        self.selectedValue = IntVar()
        self.scrollSpeed = 60

        self.bossScrollableCanvas = Canvas(self,width=parent.winfo_width(),background="#000",borderwidth=0, highlightthickness=0)
        self.scrollbar = Scrollbar(self,orient="vertical", command=self.bossScrollableCanvas.yview)
        self.bossScrollableCanvas.configure(yscrollcommand=self.scrollbar.set)

        self.bossesGrid = Frame(self.bossScrollableCanvas)
        self.bossScrollableCanvas.create_window((5,0), window=self.bossesGrid,anchor="nw")
        self.bossesGrid.bind(
            "<Configure>",
            lambda e: self.bossScrollableCanvas.configure(
                scrollregion=self.bossScrollableCanvas.bbox("all"),
                height=e.height
            )
        )
        self.bossScrollableCanvas.bind_all(
            "<MouseWheel>",
            lambda e : self.bossScrollableCanvas.yview_scroll(int(-1*(e.delta/self.scrollSpeed)), 'units')
        )
        self.scrollbar.pack(side="right", fill="y")
        self.bossScrollableCanvas.pack(side="left", fill="both", expand=True)
        self.listPath = listPath
        self.items_per_row = items_per_row
        self.columnconfigure(0, weight=1)
        self.CreateWidgets()

    def CreateWidgets(self):

        for i in range(len(self.listPath)):
            self.reminder = i % self.items_per_row
            self.rowCount = int(i / self.items_per_row)
            BossCard(self.bossesGrid, self.listPath[i][1], self.listPath[i][0], self.selectedValue, i).grid(column=self.reminder, row=self.rowCount, padx=30, sticky="s")
    def GetbossID(self):
        return self.selectedValue.get()