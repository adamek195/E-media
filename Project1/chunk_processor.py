import zlib
import struct
import os
from chunk import Chunk
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

from IHDR_data import IHDRData
from IDAT_filter import IDATFilter
from PLTE_data import PLTEData

class PNGChunkProcessor:

    PNG_SIGNATURE = b'\x89PNG\r\n\x1a\n'
    CRITICAL_CHUNKS = [b'IHDR', b'PLTE', b'IDAT', b'IEND']

    def __init__(self):
        self.chunks = []

    @staticmethod
    def validate_png(img):
        if (img.read(len(PNGChunkProcessor.PNG_SIGNATURE))
                                        != PNGChunkProcessor.PNG_SIGNATURE):
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

    def return_chunks_names_query(self):
        return "  ".join([str(chunk.chunk_type) for chunk in self.chunks])

    def IHDR_chunk_processor(self):
        IHDR_data = self.chunks[0].chunk_data
        IHDR_data_values = struct.unpack('>IIBBBBB', IHDR_data)
        IHDR_data = IHDRData(IHDR_data_values)
        self.width = IHDR_data.get_width()
        self.height = IHDR_data.get_height()
        self.color_type = IHDR_data.get_color_type()
        self.bit_depth = IHDR_data.get_bit_depth()
        IHDR_data.print_IHDR_data()


    def IDAT_chunk_processor(self):
        IDAT_data = b''.join(chunk.chunk_data for chunk in self.chunks
                                            if chunk.chunk_type == b'IDAT')
        IDAT_data = zlib.decompress(IDAT_data)
        IDAT_filter = IDATFilter(self.width, self.height, IDAT_data)
        recon_pixels = []
        recon_pixels = IDAT_filter.pixels_filter()
        plt.imshow(np.array(recon_pixels).reshape((self.height,
                                                            self.width, 4)))
        plt.show()


    def PLTE_chunk_processor(self):
        PLTE_chunk = []
        i = 0
        for chunk in self.chunks:
            if chunk.chunk_type == b'PLTE':
                PLTE_chunk.append(chunk)
                PLTE_index = i
            i+=1
        if PLTE_chunk is None:
            raise Exception("Image not have PLTE chunk")
        if self.color_type == 2 or self.color_type == 6:
            print("PLTE chunk is optional")
        elif self.color_type == 3:
            print("PLTE chunk must appear")
        if len(PLTE_chunk) != 1:
            raise Exception("Incorrect number of PLTE chunk")
        PLTE_length= self.chunks[PLTE_index].get_chunk_length()
        if PLTE_length % 3 != 0:
            raise Exception("Incorrect PLTE length - not divisible by 3")
        PLTE_data = PLTEData(PLTE_chunk[0].chunk_data)
        PLTE_data.parse_plte_data()
        PLTE_data.print_palette()
        if (PLTE_data.get_amount_of_entries_in_palette()
                                                    > 2**self.bit_depth):
            raise Exception("Incorrect number of entries in palette!")


    def IEND_chunk_processor(self):
        number_of_chunks = len(self.chunks)
        if self.chunks[number_of_chunks-1].chunk_type != b"IEND":
            print("IEND must be the last chunk")
        IEND_data = struct.unpack('>',
                                self.chunks[number_of_chunks - 1].chunk_data)
        if  len(IEND_data) == 0:
            print("IEND is empty")


    def create_new_image(self):
        filename = "tmp.png"
        img_path = "./images/{}".format(filename)
        if Path(img_path).is_file():
            os.remove(img_path)
        temporary_file = open(img_path, 'wb')
        temporary_file.write(PNGChunkProcessor.PNG_SIGNATURE)
        for chunk in self.chunks:
            if chunk.chunk_type in PNGChunkProcessor.CRITICAL_CHUNKS:
                temporary_file.write(struct.pack('>I', chunk.chunk_length))
                temporary_file.write(chunk.chunk_type)
                temporary_file.write(chunk.chunk_data)
                temporary_file.write(struct.pack('>I', chunk.chunk_crc))
        temporary_file.close()
        return filename