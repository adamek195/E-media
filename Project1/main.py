from tkinter import Tk, Label, Button
from tkinter.filedialog import askopenfilename
from chunk_processor import PNGChunkProcessor


root = Tk()


def choose_photo():
    chunk_processor = PNGChunkProcessor()
    query = chunk_processor.return_chunks_names_query()
    img_path = askopenfilename()
    label_chunks = Label(root, text=query)
    label_chunks.grid(row=3, column=0)
    img_source = open(img_path, 'rb')
    chunk_processor.save_chunks(img_source)
    chunk_processor.print_chunks_types()


def main():

    root.title("PNG reader")
    root.geometry("400x400")

    fetch_btn = Button(root, text="Load photo", command=choose_photo)
    fetch_btn.grid(row=1, column=0, columnspan=1, pady=10, padx=10, ipadx=130)

    root.mainloop()


if __name__ == "__main__":
    main()
