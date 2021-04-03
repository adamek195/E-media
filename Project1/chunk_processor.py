import zlib
import struct
import matplotlib.pyplot as plt
import numpy as np

from chunk import Chunk
from IDAT_filter import IDATFilter
from IHDR_data import IHDRData

class PNGChunkProcessor:

    def __init__(self):
        self.chunks = []

    @classmethod
    def validate_png(cls, img):
        png_signature = b'\x89PNG\r\n\x1a\n'
        if img.read(len(png_signature)) != png_signature:
            raise Exception('Invalid PNG Signature')

    def save_chunks(self, img):
        self.validate_png(img)
        while True:
            new_chunk = Chunk(img)
            self.chunks.append(new_chunk)
            if new_chunk.chunk_type == b'IEND':
                break

    def print_chunks_types(self):
        print([chunk.chunk_type for chunk in self.chunks])

    def IHDR_chunk_processor(self):
        if self.chunks[0] == None:
            print("You do not read image!")
        else:
            IHDR_data = self.chunks[0].chunk_data
            IHDR_data_values = struct.unpack('>IIBBBBB', IHDR_data)
            IHDR_data = IHDRData(IHDR_data_values)
            self.width = IHDR_data.get_width()
            self.height = IHDR_data.get_height()
            self.color_type = IHDR_data.get_color_type()
            IHDR_data.print_IHDR_data()

    def IDAT_chunk_processor(self):
        IDAT_data = b''.join(chunk.chunk_data for chunk in self.chunks if chunk.chunk_type == b'IDAT')
        IDAT_data = zlib.decompress(IDAT_data)
        IDAT_filter = IDATFilter(self.width, self.height, IDAT_data)
        recon_pixels = []
        recon_pixels = IDAT_filter.pixels_filter()
        plt.imshow(np.array(recon_pixels).reshape((self.height, self.width, 4)))
        plt.show()
