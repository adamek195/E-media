import numpy


class IHDRData:

    def __init__(self, IHDR_data_values):
        print("\nIHDR:\n")
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

        print("Width of image {} and height of image {}".format(self.width,
                                                                self.height))
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



class IDATFilter:

    def __init__(self,width,height, IDAT_data):
        print("\nIDAT:\n")
        self.recon_pixels = []
        self.bytes_per_pixel = 4
        self.height = height
        self.stride = width * self.bytes_per_pixel
        self.IDAT_data = []
        self.IDAT_data = IDAT_data

    @staticmethod
    def paeth_predictor(a, b, c):
        p = a + b - c
        pa = abs(p - a)
        pb = abs(p - b)
        pc = abs(p - c)
        if pa <= pb and pa <= pc:
            Pr = a
        elif pb <= pc:
            Pr = b
        else:
            Pr = c
        return Pr

    def recon_a(self, r, c):
        if c >= self.bytes_per_pixel:
            return self.recon_pixels[r * self.stride + c -
                                                        self.bytes_per_pixel]
        return 0

    def recon_b(self, r, c):
        if r > 0:
            return self.recon_pixels[(r-1) * self.stride + c]
        return 0

    def recon_c(self, r, c):
        if r > 0 and c >= self.bytes_per_pixel:
            return self.recon_pixels[(r-1) * self.stride + c -
                                                         self.bytes_per_pixel]
        return 0

    def pixels_filter(self):
        i = 0
        for r in range(self.height):
            filter_type = self.IDAT_data[i]
            i += 1
            for c in range(self.stride): # for each byte in scanline
                filt_x = self.IDAT_data[i]
                i += 1
                if filter_type == 0: # None
                    recon_x = filt_x
                elif filter_type == 1: # Sub
                    recon_x = filt_x + self.recon_a(r, c)
                elif filter_type == 2: # Up
                    recon_x = filt_x + self.recon_b(r, c)
                elif filter_type == 3: # Average
                    recon_x = filt_x + (self.recon_a(r, c)
                                                    + self.recon_b(r, c)) // 2
                elif filter_type == 4: # Paeth
                    recon_x = filt_x + self.paeth_predictor(self.recon_a(r, c),
                                        self.recon_b(r, c), self.recon_c(r, c))
                else:
                    raise Exception('unknown filter type: ' + str(filter_type))
                self.recon_pixels.append(recon_x & 0xff)
        return self.recon_pixels



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