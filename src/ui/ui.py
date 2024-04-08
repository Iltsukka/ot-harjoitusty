from tkinter import Tk, ttk, constants
from ui.main_view import MainView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
    
    def start(self):
        self._show_main_view()
    
    def _show_main_view(self):
        self._current_view = MainView(self._root)
        self._current_view.pack()
