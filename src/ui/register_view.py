from tkinter import ttk, constants

class RegisterView:
    def __init__(self, root, show_login_view):
        self._root = root
        self._frame = None
        self._show_login_view = show_login_view
        self._initialize()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(master=self._frame, text='Register')
        heading_label.grid(row=0,columnspan=2)
        username_label = ttk.Label(master=self._frame, text='Username:')
        password_label = ttk.Label(master=self._frame, text='Password:')
        password_confirmation_label = ttk.Label(master=self._frame, text='Password Confirmation:')

        username_entry = ttk.Entry(master=self._frame)
        password_entry = ttk.Entry(master=self._frame)
        password_confirmation_entry = ttk.Entry(master=self._frame)
        username_label.grid(row=1, column=0, sticky=(constants.E, constants.W), padx=5, pady=3)
        username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=3)
        password_label.grid(row=2, column=0, sticky=(constants.E, constants.W), padx=5, pady=3)
        password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=3)
        password_confirmation_label.grid(row=3, column=0, sticky=(constants.E, constants.W), padx=5, pady=3)
        password_confirmation_entry.grid(row=3,column=1, sticky=(constants.E, constants.W), padx=5, pady=3 )


        register_button = ttk.Button(master=self._frame, text='Register', command=self._register)
        register_button.grid(row=4, columnspan=2, sticky=(constants.W, constants.E), pady=5, padx=5)
        login_button = ttk.Button(master=self._frame, text='click here instead to login if you have an account', command=self._show_login_view)
        login_button.grid(row=5, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        self._frame.grid_columnconfigure(1, weight=1, minsize=300)
    
    def _register(self):
        return
    
    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()