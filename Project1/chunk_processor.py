from chunk import Chunk

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
