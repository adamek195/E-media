class gAMAData:
    def __init__(self, gAMA_data):
        self.gAMA_data = []
        self.gAMA_data = gAMA_data
        self.gamma_value = self.gAMA_data[0]
        self.real_gamma_value = self.gamma_value / 100000

    def print_gamma(self):
        print("The value of gamma is {}".format(self.gamma_value))

    def print_real_gamma(self):
        print("The value of decoded gamma is {}".format(self.real_gamma_value))
