from configparser import ConfigParser

import shutil as cmd
import os
import sys


class Model:
    UNDERTALE_DATA_PATH = ""
    UNDERTALE_GAME_PATH = ""

    USERSAVE_NAME = "previoussaveiles"

    try:

        ICON_PATH = sys._MEIPASS+"/img/icon.ico"

        # 0->Name/1->Image_Path/2->Save_Path
        BOSS_LIST = {
            0: ["Toriel", sys._MEIPASS+"/img/toriel.png", sys._MEIPASS+"/saves/toriel"],
            1: ["Papyrus", sys._MEIPASS+"/img/papyrus.png", sys._MEIPASS+"/saves/papyrus"],
            2: ["Undyne", sys._MEIPASS+"/img/undyne.png", sys._MEIPASS+"/saves/undyne"],
            3: ["Mettaton Ex", sys._MEIPASS+"/img/mettaton.png", sys._MEIPASS+"/saves/mettaton"],
            4: ["Muffet", sys._MEIPASS+"/img/muffet.png", sys._MEIPASS+"/saves/muffet"],
            5: ["Asgore", sys._MEIPASS+"/img/asgore.png", sys._MEIPASS+"/saves/asgore"],
            6: ["Omega Flowey", sys._MEIPASS+"/img/flowey.png", sys._MEIPASS+"/saves/flowey"],
            7: ["Asriel Dreemurr", sys._MEIPASS+"/img/asriel.png", sys._MEIPASS+"/saves/asriel"],
            8: ["Undyne the Undying", sys._MEIPASS+"/img/undyneu.png", sys._MEIPASS+"/saves/undyneu"],
            9: ["Sans", sys._MEIPASS+"/img/sans.png", sys._MEIPASS+"/saves/sans"],
            10: ["True Lab", sys._MEIPASS+"/img/truelab.png", sys._MEIPASS+"/saves/truelab"]
        }
    except:
        ICON_PATH = "img/icon.ico"

        # 0->Name/1->Image_Path/2->Save_Path
        BOSS_LIST = {
            0: ["Toriel", "img/toriel.png", "saves/toriel"],
            1: ["Papyrus", "img/papyrus.png", "saves/papyrus"],
            2: ["Undyne", "img/undyne.png", "saves/undyne"],
            3: ["Mettaton Ex", "img/mettaton.png", "saves/mettaton"],
            4: ["Muffet", "img/muffet.png", "saves/muffet"],
            5: ["Asgore", "img/asgore.png", "saves/asgore"],
            6: ["Omega Flowey", "img/omega.png", "saves/flowey"],
            7: ["Asriel Dreemurr", "img/asriel.png", "saves/asriel"],
            8: ["Undyne the Undying", "img/undyneu.png", "saves/undyneu"],
            9: ["Sans", "img/sans.png", "saves/sans"],
            10: ["True Lab", "img/truelab.png", "saves/truelab"]
        }

    def __init__(self, callback):
        self.Err_callback = callback

    def SetFiles(self, newPlayerName: str, boss_id: str, NoHitMode: bool):
        print("SetFiles")
        cmd.copy(self.BOSS_LIST[boss_id][2]+"/file0", self.UNDERTALE_DATA_PATH)
        cmd.copy(self.BOSS_LIST[boss_id][2] +
                 "/undertale.ini", self.UNDERTALE_DATA_PATH)
        self.ChangeName(newPlayerName)
        if NoHitMode:
            self.ActivateNoHit()

    def SaveUserFiles(self):
        print("SaveUserFiles")
        print(self.folder_path)
        if os.path.exists(self.folder_path):
            return
        os.mkdir(self.folder_path)
        try:
            cmd.move(self.UNDERTALE_DATA_PATH+"/file0", self.folder_path)
        except:
            self.CreateFile(self.folder_path,"file0")
        cmd.move(self.UNDERTALE_DATA_PATH+"/undertale.ini", self.folder_path)

    def RestoreUserFiles(self):
        print("RestoreUserFiles")
        try:
            if not os.path.exists(self.folder_path):
                return
            cmd.move(self.folder_path+"/file0",
                     self.UNDERTALE_DATA_PATH+"/file0")
            cmd.move(self.folder_path+"/undertale.ini",
                     self.UNDERTALE_DATA_PATH+"/undertale.ini")
            os.rmdir(self.folder_path)
        except:
            self.Err_callback()

    def SetAppPaths(self, game_path, data_path):
        self.CreateFile("settings","config.ini")
        inifile = ConfigParser()
        inifile.optionxform = str   # reset Case Sentitive
        inifile.read("settings/config.ini")
        inifile["GAME"] = {"Path": f"\"{game_path}\""}
        inifile["DATA"] = {"Path": f"\"{data_path}\""}
        with open("settings/config.ini", "w") as config:
            inifile.write(config)
        self.ReadAppPaths()

    def ReadAppPaths(self):
        try:
            inifile = ConfigParser()
            inifile.optionxform = str   # reset Case Sentitive
            inifile.read("settings/config.ini")
            self.UNDERTALE_GAME_PATH = inifile["GAME"]["Path"][1:-1]
            self.UNDERTALE_DATA_PATH = inifile["DATA"]["Path"][1:-1]
            self.folder_path = os.path.join(
                self.UNDERTALE_DATA_PATH, self.USERSAVE_NAME)
        except:
            raise IOError

    def ChangeName(self, newPlayerName: str):
        print("ChangeName")
        with open(self.UNDERTALE_DATA_PATH+"/file0", "r+") as file0:
            data = file0.readlines()
            file0.seek(0)
            data[0] = newPlayerName+"\n"
            file0.truncate()
            file0.writelines(data)

        inifile = ConfigParser()
        inifile.optionxform = str   # reset Case Sentitive
        inifile.read(self.UNDERTALE_DATA_PATH+"/undertale.ini")
        inifile["General"]["Name"] = f"\"{newPlayerName}\""
        with open(self.UNDERTALE_DATA_PATH+"/undertale.ini", "w") as undertalefile:
            inifile.write(undertalefile)

    def ActivateNoHit(self):
        print("ActivateNoHit")
        with open(self.UNDERTALE_DATA_PATH+"/file0", "r+") as file0:
            data = file0.readlines()
            file0.seek(0)
            data[2] = "1\n"
            file0.truncate()
            file0.writelines(data)

    def CreateFile(self,path,fileName):
        with open(path+"/"+fileName, 'w') as f:
            pass
        
    def GetIconPath(self):
        return self.ICON_PATH

    def GetBossList(self):
        return self.BOSS_LIST

    def GetUndertaleGamePath(self):
        return self.UNDERTALE_GAME_PATH

    def GetUndertaleDataPath(self):
        return self.UNDERTALE_DATA_PATH
