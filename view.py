# view knows about controller but not about model

import tkinter as tk
from tkinter import ttk

class View(tk.Tk):

    PADDING = 10

    def __init__(self, controller):
        super().__init__()
        self.title('Window Title')
        self.controller = controller
        self.value_var = tk.StringVar()
        self._make_MainFrame()
        self._make_Entry()

    def defaultView(self):
        print("in defaultView")
        self.mainloop() #do not call anything after mainloop

    def _make_MainFrame(self):
        self.main_frm = tk.Frame(self)
        self.main_frm.pack(padx = self.PADDING, pady = self.PADDING)

    def _make_Entry(self):
        ent = ttk.Entry(self.main_frm, justify='right', textvar=self.value_var)
        ent.pack()


