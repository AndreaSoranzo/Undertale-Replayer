from tkinter import filedialog, messagebox
from tkinter.ttk import *
from helpers.ttk_styles import TTKStyles

from components.frames.footer import FooterFrame
from components.frames.boss_grid import BossGridFrame
from components.frames.button import ButtonFrame
from components.frames.settings import SettingsFrame
from components.frames.titles import TitlesFrame

_WINDOW_HEIGHT = 1000
_WINDOW_WIDTH = 1000 

class View:
    def __init__(self, Tk, BossList, ExexCallback):
        TTKStyles().init()
        self.Exec_callback = ExexCallback
        self.MONITOR_HEIGHT = Tk.winfo_screenheight()
        self.MONITOR_WIDTH = Tk.winfo_screenwidth()
        self.positionY = int(self.MONITOR_HEIGHT/2-_WINDOW_HEIGHT/2)
        self.positionX = int(self.MONITOR_WIDTH/2-_WINDOW_WIDTH/2)
        self.Tk = Tk
        self.Tk.geometry(
            f"{_WINDOW_WIDTH}x{_WINDOW_HEIGHT}+{self.positionX}+{self.positionY}")
        self.Tk.update()
        self.Tk.columnconfigure(0, weight=1)
        self.Tk.rowconfigure(1, weight=1)


        self.titles = TitlesFrame(Tk)
        self.bossGrid = BossGridFrame(Tk, BossList, 5)
        self.playerSettings = SettingsFrame(Tk)
        self.buttons = ButtonFrame(Tk, self.StartButtonAction)
        self.footer = FooterFrame(Tk)

        self.titles.grid(column=0, row=0, sticky="n", pady=10)
        self.bossGrid.grid(column=0, row=1, padx=10, pady=20)
        self.playerSettings.grid(column=0, row=2, pady=30)
        self.buttons.grid(column=0, row=3, pady=30)
        self.footer.grid(column=0, row=4, sticky="s")

    def StartButtonAction(self):
        boss_id = self.bossGrid.GetbossID()
        name = self.playerSettings.GetPlayerName()
        isHit = self.playerSettings.GetHitMode()
        try:
            self.Exec_callback(boss_id, name, isHit)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def RestoreErrorMessage(self, errPath):
        messagebox.showerror(
            "Error", f"Error while restoring files\nGo to {errPath} to fix things")

    def AskPaths(self, exitCallback):
        game_path = filedialog.askopenfilename(title="Select Undertale game")
        if not game_path:
            exitCallback()
        data_path = filedialog.askdirectory(
            title="Select Undertale data folder")
        if not data_path:
            exitCallback()
        return (game_path, data_path)
