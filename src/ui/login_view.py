from tkinter import ttk, constants, messagebox
from services.user_service import user_service

class LoginView:
    """Luokka, joka vastaa kirjautumislomakkeen näyttämisestä.
    """
    def __init__(self, root, handle_login, handle_register):
        self._root = root
        self._frame = None
        self._handle_login = handle_login
        self._handle_register = handle_register
        self._username_entry = None
        self._password_entry = None
        self._initialize()
    
    def _initialize(self):
        """Alustaa käyttäjälle näytettävät graafiset komponentit.
        """
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(master=self._frame, text='Login')
        heading_label.grid(row=0,columnspan=2)
        username_label = ttk.Label(master=self._frame, text='Username:')
        password_label = ttk.Label(master=self._frame, text='Password:')
        self._username_entry = ttk.Entry(master=self._frame)
        self._password_entry = ttk.Entry(master=self._frame)
        username_label.grid(row=1, column=0, sticky=(constants.E, constants.W), padx=5, pady=3)
        self._username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=3)
        password_label.grid(row=2, column=0, sticky=(constants.E, constants.W), padx=5, pady=3)
        self._password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=3)


        log_in_button = ttk.Button(master=self._frame, text='login', command=self._validate_login)
        log_in_button.grid(row=3, columnspan=2, sticky=(constants.W, constants.E), pady=5, padx=5)
        register_button = ttk.Button(master=self._frame, text='click here to register', command=self._handle_register)
        register_button.grid(row=4, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        self._frame.grid_columnconfigure(1, weight=1, minsize=300)

    def _validate_login(self):
        """Tarkistaa, onko käyttäjällä oikeus kirjautua sisään.
        """
        username = self._username_entry.get()
        password = self._password_entry.get()
        if user_service.check_login_credentials(username, password):
            self._handle_login(username)
            return
        messagebox.showerror(title='Invalid user credentials', message='Login Failed')
    
    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()
