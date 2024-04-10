from tkinter import Tk
from ui.ui import UI

def main():

    window = Tk()
    window.title('Book management app')
    ui = UI(window)
    ui.start()
    window.mainloop()

if __name__ == '__main__':
    main()
    