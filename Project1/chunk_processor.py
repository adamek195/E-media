import struct
import zlib


class PNGChunkProcessor:

    def __init__(self):
        self.chunks = []

    def validate_png(self, img):
        png_signature = b'\x89PNG\r\n\x1a\n'
        if img.read(len(png_signature)) != png_signature:
            raise Exception('Invalid PNG Signature')

    def read_chunk(self, img):
        chunk_length, chunk_type = struct.unpack('>I4s', img.read(8))
        chunk_data = img.read(chunk_length)
        chunk_crc, = struct.unpack('>I', img.read(4))
        chunk_actual_crc = zlib.crc32(chunk_data, zlib.crc32(struct.pack('>4s', chunk_type)))
        if chunk_crc != chunk_actual_crc:
            raise Exception('invalid chunk sum')
        return chunk_type, chunk_data

    def save_chunks(self, img):
        self.validate_png(img)
        while True:
            chunk_type, chunk_data = self.read_chunk(img)
            self.chunks.append((chunk_type, chunk_data))
            if chunk_type == b'IEND':
                break
    
    def print_chunks_types(self):
        print([chunk[0] for chunk in self.chunks])


