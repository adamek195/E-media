import zlib
from tabulate import tabulate

class Decompresser:

    @staticmethod
    def decompress_data(data):
        compressed_byte_array = bytearray(data)
        compressed_byte_array.pop(0)
        compressed_byte_array.pop(0)
        return zlib.decompress(compressed_byte_array, -15)



class gAMAData:
    def __init__(self, gAMA_data):
        print("\ngAMA:\n")
        self.gAMA_data = []
        self.gAMA_data = gAMA_data
        self.gamma_value = self.gAMA_data[0]
        self.real_gamma_value = self.gamma_value / 100000

    def print_gamma(self):
        print("The value of gamma is {}".format(self.gamma_value))

    def print_real_gamma(self):
        print("The value of decoded gamma is {}".format(self.real_gamma_value))



class cHRMData:
    def __init__(self, cHRM_data):
        print("\ncHRM:\n")
        self.cHRM_data = []
        self.cHRM_data = cHRM_data
        self.white_point_x = self.cHRM_data[0] / 100000
        self.white_point_y = self.cHRM_data[1] / 100000
        self.red_x = self.cHRM_data[2] / 100000
        self.red_y = self.cHRM_data[3] / 100000
        self.green_x = self.cHRM_data[4] / 100000
        self.green_y = self.cHRM_data[5] / 100000
        self.blue_x = self.cHRM_data[6] / 100000
        self.blue_y = self.cHRM_data[7] / 100000

    def print_chromaticity_values(self):
        chromaticity_table = [['', 'Red', 'Green', 'Blue', 'White Point'],
        ['x', self.red_x, self.green_x, self.blue_x, self.white_point_x],
        ['y', self.red_y, self.green_y, self.blue_y, self.white_point_y]]

        print("Table of chromaticity values: ")
        print(tabulate(chromaticity_table))



class sRGBData:
    def __init__(self, sRBG_data):
        print("\nsRGB:\n")
        self.sRBG_data = []
        self.sRBG_data = sRBG_data
        self.rendering_intent = self.sRBG_data[0]

    def print_rendering_intent(self):
        if self.rendering_intent == 0:
            print("Values of rendering intent is {}: Perceptual".format(self.rendering_intent))
        elif self.rendering_intent == 1:
            print("Values of rendering intent is {}: Relative colorimetric".format(self.rendering_intent))
        elif self.rendering_intent == 2:
            print("Values of rendering intent is {}: Saturation".format(self.rendering_intent))
        elif self.rendering_intent == 3:
            print("Values of rendering intent is {}: Absolute colorimetric".format(self.rendering_intent))

class tEXtData:

    def __init__(self, data):
        print("\ntEXt:\n")
        self.data = data
        self.keyword_encoded = []
        self.data_encoded = []
        self.data_decoded = ""
        self.keyword = ""


    def decode_tEXt_data(self):
        iterator = 0
        for elements in self.data:
            for element in elements:
                if element == 0:
                    break
                self.keyword_encoded.append(element)
                iterator += 1

        self.keyword = bytearray(self.keyword_encoded).decode('utf-8')
        print("Keyword: {}".format(self.keyword))

        for elements in self.data:
            while iterator < len(elements):
                self.data_encoded.append(elements[iterator])
                iterator += 1
        self.data_decoded = bytearray(self.data_encoded).decode('latin1')
        print("Data: {} \n".format(self.data_decoded))



class iTXtData:

    def __init__(self, data):
        print("\niTXt:\n")
        self.data = data
        self.keyword_encoded = []
        self.data_encoded = []
        self.data_decoded = []
        self.keyword = ""


    def decode_iTXt_data(self):
        iterator = 0
        for elements in self.data:
            for element in elements:
                if element == 0:
                    iterator += 1
                    break
                self.keyword_encoded.append(element)
                iterator += 1

        self.keyword = bytearray(self.keyword_encoded).decode('latin1')
        print("Keyword: {}".format(self.keyword))

        for elements in self.data:
            is_compressed = elements[iterator]
            print("Compress method {}".format(is_compressed))

        iterator += 1
        iterator += 1
        separator_counter = 0
        while separator_counter < 2:
            for elements in self.data:
                while elements[iterator] != 0:
                    iterator += 1
                iterator += 1
            separator_counter += 1

        for elements in self.data:
            while iterator < len(elements):
                self.data_encoded.append(elements[iterator])
                iterator += 1

        if is_compressed:
            self.data_decoded = Decompresser.decompress_data(
                                            self.data_encoded).decode('utf-8'
                                            )
        else:
            self.data_decoded = bytearray(self.data_encoded).decode('utf-8')
        print("Data: {} \n".format(self.data_decoded))



class zTXtData:

    def __init__(self, data):
        print("\nzTXt:\n")
        self.data = data
        self.keyword_encoded = []
        self.data_encoded = []
        self.data_decoded = []
        self.keyword = ""


    def decode_zTXt_data(self):
        iterator = 0
        for elements in self.data:
            for element in elements:
                if element == 0:
                    break
                self.keyword_encoded.append(element)
                iterator += 1

        self.keyword = bytearray(self.keyword_encoded).decode('latin1')
        print("Keyword: {}".format(self.keyword))

        for elements in self.data:
            is_compressed = elements[iterator]
            print("Compress method {}".format(is_compressed))

        iterator += 1
        iterator += 1

        for elements in self.data:
            while iterator < len(elements):
                self.data_encoded.append(elements[iterator])
                iterator += 1

        self.data_decoded = Decompresser.decompress_data(
                                            self.data_encoded).decode('latin1'
                                            )
        print("Data: {} \n".format(self.data_decoded))



class tIMEData:

    def __init__(self, tIME_data):
        print("\ntIME:\n")
        self.tIME_data = []
        self.tIME_data = tIME_data
        self.year = self.tIME_data[0]
        self.month = self.tIME_data[1]
        self.day = self.tIME_data[2]
        self.hour = self.tIME_data[3]
        self.minute = self.tIME_data[4]
        self.second = self.tIME_data[5]

    def print_modification_date(self):
        if self.day < 10:
            self.day = "0" + str(self.day)
        if self.month < 10:
            self.month = "0" + str(self.month)
        if self.hour < 10:
            self.hour = "0" + str(self.hour)
        if self.minute < 10:
            self.minute = "0" + str(self.minute)
        if  self.second < 10:
            self.second = "0" + str(self.second)
        print("Last modification date: {}.{}.{} {}:{}:{}".format(
            self.day, self.month, self.year, self.hour, self.minute,
                                                                self.second))
