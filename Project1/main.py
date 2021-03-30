from tkinter import Tk, Label

def main():
    root = Tk()
    label = Label(root, text="Hello world")
    label.pack()
    root.mainloop()


if __name__ == "__main__":
    main()
