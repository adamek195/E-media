import zlib
import struct


class Chunk:

    def __init__(self, img):
        self.chunk_length, self.chunk_type = struct.unpack('>I4s', img.read(8))
        self.chunk_data = img.read(self.chunk_length)
        self.chunk_crc, = struct.unpack('>I', img.read(4))
        chunk_actual_crc = zlib.crc32(self.chunk_data,
                            zlib.crc32(struct.pack('>4s', self.chunk_type)))
        if self.chunk_crc != chunk_actual_crc:
            raise Exception('invalid chunk sum')

    def get_chunk_length(self):
        return self.chunk_length