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