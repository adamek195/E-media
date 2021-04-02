from tkinter import Tk, Label, Button
from chunk_processor import PNGChunkProcessor


root = Tk()
chunk_processor = PNGChunkProcessor()


def fetch_chunks():
    query = chunk_processor.return_chunks_names_query()
    label = Label(root, text=query)
    label.grid(row=3, column=0)


def main():
    img_source = open('images/bird.png', 'rb')
    chunk_processor.save_chunks(img_source)
    chunk_processor.print_chunks_types()

    root.title("PNG reader")
    root.geometry("400x400")

    fetch_btn = Button(root, text="Fetch chunks", command=fetch_chunks)
    fetch_btn.grid(row=1, column=0, columnspan=1, pady=10, padx=10, ipadx=130)

    root.mainloop()


if __name__ == "__main__":
    main()
