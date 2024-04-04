from tkinter import ttk, constants
from services.book_service import book_service

class MainView:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._frame_second = None
        self._initialize()
    
    def _initialize(self):
        self._initialize_add_book()
        self._initialize_book_list_view()
        

        #book servicen tulee palauttaa kirja-objekti, jossa löytyy kirjan id, muutenkin tämä pitää muuttaa
    def _create_book(self):
        title = self._title_entry.get()
        author = self._author_entry.get()
        if book_service.create_book(title, author):
            label_title = ttk.Label(master=self._frame_second, text=title)
            label_author = ttk.Label(master=self._frame_second, text=author)
            label_title.grid()
            label_author.grid()
    
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

    #kirjojen näyttäminen tulee muuttaa listboxiksi
    def _initialize_book_list_view(self):
        self._frame_second = ttk.Frame(master=self._root)
        books = book_service.all_books()
        title = ttk.Label(master=self._frame_second, text='Books')
        book_title = ttk.Label(master=self._frame_second, text='Title:')
        author = ttk.Label(master=self._frame_second, text='Author:')
        title.grid(row=0, column=0, columnspan=3)
        book_title.grid(row=1, column=0)
        author.grid(row=1, column=1)
        row_num = 2
        for book in books:
            title = ttk.Label(master=self._frame_second, text=book.title)
            title.grid(row=row_num,column=0)
            author = ttk.Label(master=self._frame_second, text=book.author)
            author.grid(row=row_num, column=1)

            delete_button = ttk.Button(master=self._frame_second, text='delete book')
            delete_button.grid(row=row_num,column=2, sticky=(constants.E), padx=60)
            row_num += 1
        self._frame_second.grid_columnconfigure(1, weight=1)
        self._frame_second.grid_columnconfigure(0, weight=1)
        self._frame_second.grid_columnconfigure(2, weight=1)
    


    
    def destroy(self):
        self._frame.destroy()
    
    def pack(self):
        self._frame.pack(fill=constants.X)
        self._frame_second.pack(fill=constants.X)