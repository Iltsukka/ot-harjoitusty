from tkinter import ttk, constants, messagebox
from services.user_service import user_service

class RegisterView:
    """Vastaa käyttäjän rekisteröinnistä.
    """
    def __init__(self, root, show_login_view, handle_login):
        self._root = root
        self._frame = None
        self._show_login_view = show_login_view
        self._handle_login = handle_login
        self._username_entry = None
        self._password_entry = None
        self._password_confirmation_entry = None
        self._initialize()
    
    def _initialize(self):
        """Alustaa näytettävät graafiset komponentit.
        """
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(master=self._frame, text='Register')
        heading_label.grid(row=0,columnspan=2)
        username_label = ttk.Label(master=self._frame, text='Username:')
        password_label = ttk.Label(master=self._frame, text='Password:')
        password_confirmation_label = ttk.Label(master=self._frame, text='Password Confirmation:')

        self._username_entry = ttk.Entry(master=self._frame)
        self._password_entry = ttk.Entry(master=self._frame)
        self._password_confirmation_entry = ttk.Entry(master=self._frame)
        username_label.grid(row=1, column=0, sticky=(constants.E, constants.W), padx=5, pady=3)
        self._username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=3)
        password_label.grid(row=2, column=0, sticky=(constants.E, constants.W), padx=5, pady=3)
        self._password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=3)
        password_confirmation_label.grid(row=3, column=0, sticky=(constants.E, constants.W), padx=5, pady=3)
        self._password_confirmation_entry.grid(row=3,column=1, sticky=(constants.E, constants.W), padx=5, pady=3 )


        register_button = ttk.Button(master=self._frame, text='Register', command=self._register)
        register_button.grid(row=4, columnspan=2, sticky=(constants.W, constants.E), pady=5, padx=5)
        login_button = ttk.Button(master=self._frame, text='click here instead to login if you have an account', command=self._show_login_view)
        login_button.grid(row=5, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        self._frame.grid_columnconfigure(1, weight=1, minsize=300)
    
    def _register(self):
        """Vastaa käyttäjän luonnista.
        """
        username = self._username_entry.get()
        password = self._password_entry.get()
        password_conf = self._password_confirmation_entry.get()
        if password != password_conf:
            messagebox.showerror(title='Input Error!', message='Passwords do not match!')
            return
        if user_service.register_user(username, password):
            messagebox.showinfo(title='Success', message=f'User {username} was successfully created!')
            self._handle_login(username)
            return
        messagebox.showwarning(title='Could not create user', message='Username is already in use')
    
    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()