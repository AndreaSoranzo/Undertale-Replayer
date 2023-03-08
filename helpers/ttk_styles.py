from tkinter.ttk import *


class TTKStyles:
    def init(self):
        s = Style()
        s.configure('.', background="#000")
        s.configure('test.TFrame', background="#4C5")
        s.configure('TLabel', foreground="#E0E0E0", font=("arial", 20, "bold"))
        s.configure('sub.TLabel', font=("arial", 15, "bold"))
        s.configure('fut.TLabel', font=("arial", 10, "bold"))
        s.configure('TButton', font=("arial", 20, "bold"))
        s.configure('sub.TButton', font=("arial", 10, "bold"))
        s.configure('TCheckbutton',
                    foreground="#E0E0E0", font=("arial", 10, "bold"))
