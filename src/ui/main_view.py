from tkinter import ttk, constants, Listbox, END, StringVar
from services.book_service import book_service

class MainView:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._frame_second = None
        self._title_entry = None
        self._author_entry = None
        self._book_listbox = None
        self._books = book_service.all_books()
        self._initialize()
    
    def _initialize(self):
        self._initialize_add_book()
        self._initialize_book_list_view()
        

    def _create_book(self):
        title = self._title_entry.get()
        author = self._author_entry.get()
        created_book = book_service.create_book(title, author)
        book_information = f'{created_book.title} - {created_book.author}'
        self._book_listbox.insert(END, book_information)
        for book in self._books:
            print(book.title)
    
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
        title = ttk.Label(master=self._frame_second, text='Books')
        title.grid(row=0, column=0, columnspan=2)
        delete_button = ttk.Button(master=self._frame_second, text='delete', command=self._delete)
        delete_button.grid(row=1, column=2,columnspan=2, sticky=(constants.W, constants.E), padx=5)
        filter_header = StringVar(self._frame_second)
        filter_header.set('Sort by')
        filter_options = ['Sort by','Default sorting','Title', 'Author']
        filter_menu = ttk.OptionMenu(self._frame_second, filter_header, *filter_options, command=self._sort_by)
        filter_menu.grid(row=2, column=2, columnspan=2, sticky=(constants.W, constants.E), padx=5)
        for book in self._books:
            book_information = f'{book.title} - {book.author}'
            self._book_listbox.insert(END, book_information)
        self._frame_second.grid_columnconfigure(1, weight=1)
        self._frame_second.grid_columnconfigure(0, weight=1)
        self._frame_second.grid_columnconfigure(2, weight=0, minsize=100)
        self._frame_second.grid_columnconfigure(3, weight=0, minsize=100)


    def _sort_by(self, option):
        sorted_books = book_service.sort_by(option)
        self._update_book_list(sorted_books)

    
    def _update_book_list(self, sorted_books):
        self._book_listbox.delete(0, END)
        for book in sorted_books:
            book_information = f'{book.title} - {book.author}'
            self._book_listbox.insert(END, book_information)
    
    #need to update deleting on repository and service level as well
    def _delete(self):
        selection = self._book_listbox.curselection()
        print(self._book_listbox.get(selection))
        self._book_listbox.delete(selection)
    
    def destroy(self):
        self._frame.destroy()
    
    def pack(self):
        self._frame.pack(fill=constants.X)
        self._frame_second.pack(fill=constants.X)