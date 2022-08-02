from subprocess import Popen
from atexit import register
from threading import Thread
from psutil import process_iter
from tkinter import Tk

from mvc.model import Model
from mvc.view import View


class Controller:

    def __init__(self):
        self.tk = Tk()
        self.model = Model(self.ShowRestoreErrorMessage)
        self.view = View(self.tk, self.model.GetBossList(), self.Exec)
        # register for on-exit app action

    def run(self):
        self.CheckUndertaleProcess()
        self.tk.focus_set()
        self.tk.resizable(False, False)
        self.tk.title("Underatale Raplayer")
        self.tk.configure(background="#000")
        self.tk.iconbitmap("img/icon.ico")
        try:
            self.model.TrySetAppPaths()
        except:
            settingsTuple = self.view.AskPaths()
            self.model.SetAppPaths(settingsTuple[0], settingsTuple[1])
        register(self.model.RestoreUserFiles)
        self.tk.mainloop()

    def Exec(self, boss_id, playerName, isHit):
        self.model.SaveUserFiles()
        self.model.SetFiles(playerName, boss_id, isHit)
        undertale = Popen(self.model.GetUndertaleGamePath())
        listenThread = Thread(target=self.ListenForClosing, args=(undertale,))
        listenThread.start()
        self.CloseApp()

    def CheckUndertaleProcess(self):
        print("CheckUndertaleProcess")
        for process in process_iter():
            if "UNDERTALE" in process.name():
                self.CloseApp()

    def ListenForClosing(self, app):
        result = app.poll()
        while (result is None):  # if is None -> app is running
            result = app.poll()

    def ShowRestoreErrorMessage(self):
        self.view.RestoreErrorMessage(self.model.GetUndertaleDataPath())

    def CloseApp(self):
        self.tk.destroy()
