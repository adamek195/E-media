class tEXtData:

    def __init__(self, data):
        self.data = data

    def print_tEXt_data(self):
        print([bytearray(row).decode('utf-8') for row in self.data])
