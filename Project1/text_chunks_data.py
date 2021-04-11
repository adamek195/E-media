class tEXtData:

    def __init__(self, data):
        print("\ntEXt:\n")
        self.data = data
        self.keyword_encoded = []
        self.data_encoded = []


    def decode_tEXt_data(self):
        iterator = 0
        for elements in self.data:
            for element in elements:
                if element is 0:
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
        self.data = data

    def print_iTXt_data(self):
        print("\n\niTXt:")
        print([bytearray(row).decode('latin1') for row in self.data])


class zTXtData:

    def __init__(self, data):
        self.data = list(data)

    def print_zTXt_data(self):
        print("\n\nzTXt:")
        print([bytearray(row).decode('latin1') for row in self.data])
