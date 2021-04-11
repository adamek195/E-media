class tEXtData:

    def __init__(self, data):
        self.data = data

    def print_tEXt_data(self):
        print("\n\ntEXt:")
        print([bytearray(row).decode('utf-8') for row in self.data])


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
