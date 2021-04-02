from chunk import Chunk
import struct

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
            width = IHDR_data_values[0]
            height = IHDR_data_values[1]
            bit_depth = IHDR_data_values[2]
            color_type = IHDR_data_values[3]
            compression_method = IHDR_data_values[4]
            filter_method = IHDR_data_values[5]
            interlace_method = IHDR_data_values[6]
            print("Width of image {} and height of image {}".format(width,
                                                                    height))
            print("Bit depth of image: {}".format(bit_depth))
            if color_type == 0:
                print("PNG Image Type: Grayscale")
            elif color_type == 2:
                print("PNG Image Type: Truecolor")
            elif color_type == 3:
                print("PNG Image Type: Indexed-color")
            elif color_type == 4:
                print("PNG Image Type: Grayscale with alpha	")
            elif color_type == 6:
                print("PNG Image Type: Truecolor with alpha")
            print("Compression method: {}".format(compression_method))
            print("Filter method: {}".format(filter_method))
            print("Interlace method: {}".format(interlace_method))
