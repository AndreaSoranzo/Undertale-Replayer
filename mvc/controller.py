from subprocess import Popen
from atexit import register
import sys
import time
import psutil
from threading import Thread
from tkinter import Tk

from mvc.model import Model
from mvc.view import View


class Controller:

    PROCESS_NAME = "UNDERTALE"
    FIND_REFRESHRATE = 1.5

    def __init__(self):
        self.tk = Tk()
        self.model = Model(self.ShowRestoreErrorMessage)
        self.view = View(self.tk, self.model.GetBossList(), self.Exec)
        # register for on-exit app action

    def run(self):
        self.CheckUndertaleProcess()
        self.tk.focus_set()
        self.tk.resizable(False, False)
        self.tk.title("Underatale Replayer")
        self.tk.configure(background="#000")
        self.tk.iconbitmap(self.model.GetIconPath())
        try:
            self.model.ReadAppPaths()
        except:
            settingsTuple = self.view.AskPaths(self.CloseApp)
            self.model.SetAppPaths(settingsTuple[0], settingsTuple[1])
        register(self.model.RestoreUserFiles)
        self.tk.mainloop()

    def Exec(self, boss_id, playerName, isHit):
        self.model.SaveUserFiles()
        self.model.SetFiles(playerName, boss_id, isHit)
        undertale = Popen(self.model.GetUndertaleGamePath())
        listenThread = Thread(target=self.ListenForClosing, args=(self.FIND_REFRESHRATE,))
        listenThread.start()
        self.CloseApp()

    def CheckUndertaleProcess(self):
        print("CheckUndertaleProcess")
        for process in psutil.process_iter():
            if self.PROCESS_NAME in process.name():
                self.CloseApp()
    
    def ListenForClosing(self, findRefreshRate):
        poll = None
        while (poll == None):          
            time.sleep(findRefreshRate) # wait undertale initialization
            for process in psutil.process_iter():
                if self.PROCESS_NAME in process.name():
                    poll = process.pid
        while (True): 
            if not psutil.pid_exists(poll): # if it exist the undertale process still exists
                break

    def ShowRestoreErrorMessage(self):
        self.view.RestoreErrorMessage(self.model.GetUndertaleDataPath())

    def CloseApp(self):
        self.tk.destroy()
        sys.exit()
