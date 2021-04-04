import numpy

class PLTEData:

    def __init__(self, PLTE_data):
        self.PLTE_data = []
        self.PLTE_data = PLTE_data
        self.palette = []

    def parse_plte_data(self):
        for i in range (0, len(self.PLTE_data),3):
            rawPixel = self.PLTE_data[i:i+3]
            pixel = (rawPixel[0], rawPixel[1], rawPixel[2])
            self.palette.append(pixel)

    def print_palette(self):
        palette = numpy.array(self.palette)
        palette = numpy.reshape(self.palette, (-1,3))
        print(palette)

    def get_amount_of_entries_in_palette(self):
        return len(self.palette)