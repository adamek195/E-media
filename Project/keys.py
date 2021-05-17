from random import getrandbits
from prime_generator import PrimeGenerator

class Keys:

    def __init__(self, key_size=1024):
        self.key_size = key_size
        self.p = PrimeGenerator.generate_prime_number(key_size)
        self.q = PrimeGenerator.generate_prime_number(key_size)
        self.euler_function = (self.p - 1)*(self.q - 1)
        self.n = self.p * self.q


    def gcd_euklides(self, a, b):
        while(b):
            a, b = b, a % b

        return a

    def generate_public_key(self):
        while True:
            e = getrandbits(self.key_size)
            if self.gcd_euklides(e, (self.p - 1) * (self.q - 1)) == 1:
                break

        if 1 > e or e > self.n:
            self.generate_public_key()
        if e % 2 == 0:
            self.generate_public_key()

        public_key = {"e": e, "n": self.n}

        return public_key

keys = Keys()
public_key = keys.generate_public_key()
print(public_key)


