class tIMEData:

    def __init__(self, tIME_data):
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
