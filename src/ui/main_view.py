from tkinter import ttk, constants, Listbox, END
from services.book_service import book_service

class MainView:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._frame_second = None
        self._title_entry = None
        self._author_entry = None
        self._book_listbox = None
        self._initialize()
    
    def _initialize(self):
        self._initialize_add_book()
        self._initialize_book_list_view()
        

        #book servicen tulee palauttaa kirja-objekti, jossa löytyy kirjan id, muutenkin tämä pitää muuttaa
    def _create_book(self):
        title = self._title_entry.get()
        author = self._author_entry.get()
        if book_service.create_book(title, author):
            book_information = f'{title} - {author}'
            self._book_listbox.insert(END, book_information)
    
    def _initialize_add_book(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text='Add a Book')
        title_label = ttk.Label(master=self._frame, text='Title:')
        author_label = ttk.Label(master=self._frame, text='Author:')
        button = ttk.Button(master=self._frame, text='Submit', command=self._create_book)
        self._title_entry = ttk.Entry(master=self._frame)
        self._author_entry = ttk.Entry(master=self._frame)
        label.grid(row=0, column=0,columnspan=2)
        title_label.grid(row=1, column=0, padx=5, pady=5)
        self._title_entry.grid(row=1, column=1, sticky=(constants.W, constants.E), padx=5, pady=5)
        author_label.grid(row=2, column=0, padx=5, pady=5)
        self._author_entry.grid(row=2, column=1, sticky=(constants.W, constants.E), padx=5, pady=5)
        button.grid(row=3, column=0, columnspan=2, sticky=(constants.W, constants.E), pady=5)
        self._frame.grid_columnconfigure(1, weight=1, minsize=300)

    def _initialize_book_list_view(self):
        self._frame_second = ttk.Frame(master=self._root)
        self._book_listbox = Listbox(master=self._frame_second, width=40)
        self._book_listbox.grid(row=1, column=0,rowspan=3, columnspan=2, sticky=(constants.W, constants.E))
        scrollbar = ttk.Scrollbar(master=self._frame_second, orient=constants.VERTICAL, command=self._book_listbox.yview)
        scrollbar.grid(row=1, column=1,rowspan=3, sticky=(constants.N, constants.S, constants.E))
        self._book_listbox.config(yscrollcommand=scrollbar.set)
        books = book_service.all_books()
        title = ttk.Label(master=self._frame_second, text='Books')
        title.grid(row=0, column=0, columnspan=2)
        delete_button = ttk.Button(master=self._frame_second, text='delete', command=self._delete)
        delete_button.grid(row=1, column=2,columnspan=2, sticky=(constants.W, constants.E), padx=5)
        for book in books:
            book_information = f'{book.title} - {book.author}'
            self._book_listbox.insert(END, book_information)
        self._frame_second.grid_columnconfigure(1, weight=1)
        self._frame_second.grid_columnconfigure(0, weight=1)
        self._frame_second.grid_columnconfigure(2, weight=0)
        self._frame_second.grid_columnconfigure(3, weight=0)
    

    def _delete(self):
        selection = self._book_listbox.curselection()
        print(self._book_listbox.get(selection))
        self._book_listbox.delete(selection)
    
    def destroy(self):
        self._frame.destroy()
    
    def pack(self):
        self._frame.pack(fill=constants.X)
        self._frame_second.pack(fill=constants.X)