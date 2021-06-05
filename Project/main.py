from tkinter import Tk, Label, Button, Frame
from tkinter.filedialog import askopenfilename
from chunk_processor import PNGChunkProcessor
from PIL import Image, ImageTk
from fourier import Fourier
root = Tk()


def choose_photo_ecb():
    img_path = askopenfilename(filetypes=[("PNG Files", "*.png")])
    chunk_processor = PNGChunkProcessor()
    img_source = open(img_path, 'rb')
    chunk_processor.save_chunks(img_source)
    chunk_processor.print_chunks_types()
    chunk_processor.IHDR_chunk_processor()
    try:
        chunk_processor.IDAT_chunk_processor_ecb()
    except:
        chunk_processor.IDAT_chunk_processor_ecb()
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
    chunk_processor.create_ecb_library_image()
    Fourier.show_plots(img_path)
    display_photo(chunk_processor)

def choose_photo_cbc():
    img_path = askopenfilename(filetypes=[("PNG Files", "*.png")])
    chunk_processor = PNGChunkProcessor()
    img_source = open(img_path, 'rb')
    chunk_processor.save_chunks(img_source)
    chunk_processor.print_chunks_types()
    chunk_processor.IHDR_chunk_processor()
    try:
        chunk_processor.IDAT_chunk_processor_cbc()
    except:
        chunk_processor.IDAT_chunk_processor_cbc()
    chunk_processor.PLTE_chunk_processor()
    chunk_processor.gAMA_chunk_processor()
    chunk_processor.cHRM_chunk_processor()
    chunk_processor.sRGB_chunk_processor()
    chunk_processor.tEXt_chunk_processor()
    chunk_processor.iTXt_chunk_processor()
    chunk_processor.zTXt_chunk_processor()
    chunk_processor.tIME_chunk_prcessor()
    chunk_processor.IEND_chunk_processor()
    chunk_processor.create_cbc_image()
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
    frame = Frame(root)

    button_ecb = Button(frame, text="PNG with ECB", command=choose_photo_ecb)
    button_cbc = Button(frame, text="PNG with CBC", command=choose_photo_cbc)
    frame.grid(row=0, column=0, columnspan=1, pady=10, padx=10, ipadx=130)
    button_ecb.pack(side="top")
    button_cbc.pack(side="top")

    root.mainloop()


if __name__ == "__main__":
    main()