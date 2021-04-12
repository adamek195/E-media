import zlib


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


    @staticmethod
    def decompress_data(data):
        compressed_byte_array = bytearray(data)
        compressed_byte_array.pop(0)
        compressed_byte_array.pop(0)
        return zlib.decompress(compressed_byte_array, -15)


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
            self.data_decoded = self.decompress_data(
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


    @staticmethod
    def decompress_data(data):
        compressed_byte_array = bytearray(data)
        compressed_byte_array.pop(0)
        compressed_byte_array.pop(0)
        return zlib.decompress(compressed_byte_array, -15)


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

        self.data_decoded = self.decompress_data(
                                            self.data_encoded).decode('latin1'
                                            )
        print("Data: {} \n".format(self.data_decoded))
