from tabulate import tabulate

class cHRMData:
    def __init__(self, cHRM_data):
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