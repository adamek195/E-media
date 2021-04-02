from tkinter import Tk, Label
from chunk_processor import PNGChunkProcessor

def main():
    img_source = open('images/bird.png', 'rb')
    chunk_processor = PNGChunkProcessor()
    chunk_processor.save_chunks(img_source)
    chunk_processor.print_chunks_types()

    root = Tk()
    label = Label(root, text="Hello world")
    label.pack()
    root.mainloop()


if __name__ == "__main__":
    main()
