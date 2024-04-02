from tkinter import ttk, constants

class MainView:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._initialize()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text='Add a Book')
        title_label = ttk.Label(master=self._frame, text='Title:')
        author_label = ttk.Label(master=self._frame, text='Author:')
        button = ttk.Button(master=self._frame, text='Submit')
        title_entry = ttk.Entry(master=self._frame)
        author_entry = ttk.Entry(master=self._frame)
        label.grid(row=0, column=0,columnspan=2)
        title_label.grid(row=1, column=0, padx=5, pady=5)
        title_entry.grid(row=1, column=1, sticky=(constants.W, constants.E), padx=5, pady=5)
        author_label.grid(row=2, column=0, padx=5, pady=5)
        author_entry.grid(row=2, column=1, sticky=(constants.W, constants.E), padx=5, pady=5)
        button.grid(row=3, column=0, columnspan=2, sticky=(constants.W, constants.E), pady=5)
        self._frame.grid_columnconfigure(1, weight=1, minsize=300)

        
            
    
    def destroy(self):
        self._frame.destroy()
    
    def pack(self):
        self._frame.pack(fill=constants.X)