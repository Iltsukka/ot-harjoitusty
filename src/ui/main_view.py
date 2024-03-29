from tkinter import ttk, constants

class MainView:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._initialize()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text='testing')
        button = ttk.Button(master=self._frame, text='quit')
        label.grid()
        button.grid()
    
    def destroy(self):
        self._frame.destroy()
    
    def pack(self):
        self._frame.pack(fill=constants.X)