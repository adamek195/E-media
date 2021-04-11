class IDATFilter:

    def __init__(self,width,height, IDAT_data):
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
