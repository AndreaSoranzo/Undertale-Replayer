from mvc.controller import Controller
from ctypes import windll

def main():
    # disable DPI resizeing
    windll.shcore.SetProcessDpiAwareness(1)
    C = Controller()
    C.run()


if __name__ == "__main__":
    main()
