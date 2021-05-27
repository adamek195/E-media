from tkinter import Tk, Label, Button
from tkinter.filedialog import askopenfilename
from chunk_processor import PNGChunkProcessor
from PIL import Image, ImageTk
from fourier import Fourier
root = Tk()


def choose_photo():
    img_path = askopenfilename(filetypes=[("PNG Files", "*.png")])
    chunk_processor = PNGChunkProcessor()
    img_source = open(img_path, 'rb')
    chunk_processor.save_chunks(img_source)
    chunk_processor.print_chunks_types()
    chunk_processor.IHDR_chunk_processor()
    chunk_processor.IDAT_chunk_processor()
    chunk_processor.PLTE_chunk_processor()
    chunk_processor.gAMA_chunk_processor()
    chunk_processor.cHRM_chunk_processor()
    chunk_processor.sRGB_chunk_processor()
    chunk_processor.tEXt_chunk_processor()
    chunk_processor.iTXt_chunk_processor()
    chunk_processor.zTXt_chunk_processor()
    chunk_processor.tIME_chunk_prcessor()
    chunk_processor.IEND_chunk_processor()
    chunk_processor.create_ecb_image()
    Fourier.show_plots(img_path)
    display_photo(chunk_processor)


def display_photo(chunk_processor):
    filename = chunk_processor.create_new_image()
    path = "./images/{}".format(filename)
    img = Image.open(path)
    img = ImageTk.PhotoImage(Image.open(path).resize((round(300 / img.height *
                                                     img.width), round(300))))
    label = Label(root, image=img)
    label.image = img
    label.grid(row=2, column=0)


def main():
    root.title("PNG reader")
    root.geometry("400x400")

    fetch_btn = Button(root, text="Load photo", command=choose_photo)
    fetch_btn.grid(row=1, column=0, columnspan=1, pady=10, padx=10, ipadx=130)

    root.mainloop()


if __name__ == "__main__":
    main()