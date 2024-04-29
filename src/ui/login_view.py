from tkinter import ttk, constants

class LoginView:
    def __init__(self, root, handle_login, handle_register):
        self._root = root
        self._frame = None
        self._handle_login = handle_login
        self._handle_register = handle_register
        self._initialize()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(master=self._frame, text='Login')
        heading_label.grid(row=0,columnspan=2)
        username_label = ttk.Label(master=self._frame, text='Username:')
        password_label = ttk.Label(master=self._frame, text='Password:')
        username_entry = ttk.Entry(master=self._frame)
        password_entry = ttk.Entry(master=self._frame)
        username_label.grid(row=1, column=0, sticky=(constants.E, constants.W), padx=5, pady=3)
        username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=3)
        password_label.grid(row=2, column=0, sticky=(constants.E, constants.W), padx=5, pady=3)
        password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=3)


        log_in_button = ttk.Button(master=self._frame, text='login', command=self._validate_login)
        log_in_button.grid(row=3, columnspan=2, sticky=(constants.W, constants.E), pady=5, padx=5)
        register_button = ttk.Button(master=self._frame, text='click here to register', command=self._handle_register)
        register_button.grid(row=4, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        self._frame.grid_columnconfigure(1, weight=1, minsize=300)

    def _validate_login(self):
        self._handle_login()
    
    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()
