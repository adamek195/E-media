class IHDRData:

    def __init__(self, IHDR_data_values):
        self.IHDR_data = []
        self.IHDR_data = IHDR_data_values
        self.width = self.IHDR_data[0]
        self.height = self.IHDR_data[1]
        self.bit_depth = self.IHDR_data[2]
        self.color_type = self.IHDR_data[3]
        self.compression_method = self.IHDR_data[4]
        self.filter_method = self.IHDR_data[5]
        self.interlace_method = self.IHDR_data[6]

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_color_type(self):
        return self.color_type

    def get_bit_depth(self):
        return self.bit_depth

    def print_IHDR_data(self):
        print("Width of image {} and height of image {}".format(self.width, self.height))
        print("Bit depth of image: {}".format(self.bit_depth))
        if self.color_type == 0:
            print("PNG Image Type: Grayscale")
        elif self.color_type == 2:
            print("PNG Image Type: Truecolor")
        elif self.color_type == 3:
            print("PNG Image Type: Indexed-color")
        elif self.color_type == 4:
            print("PNG Image Type: Grayscale with alpha	")
        elif self.color_type == 6:
            print("PNG Image Type: Truecolor with alpha")
        print("Compression method: {}".format(self.compression_method))
        print("Filter method: {}".format(self.filter_method))
        print("Interlace method: {}".format(self.interlace_method))
