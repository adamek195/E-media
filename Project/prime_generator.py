from random import randrange, getrandbits

class PrimeGenerator:

    @staticmethod
    def rabin_miller_test(num, k=10):

        s = num - 1
        t = 0

        while s % 2 == 0:
            s = s // 2
            t += 1
        for trials in range(k):
            a = randrange(2, num - 1)
            v = pow(a, s, num)
            if v != 1:
                i = 0
                while v != (num - 1):
                    if i == t - 1:
                        return False
                    else:
                        i = i + 1
                        v = (v ** 2) % num
            return True

    @staticmethod
    def is_prime(num, k):
        if num == 2 or num == 3:
            return True
        if num <= 1 or num % 2 == 0:
            return False

        return PrimeGenerator.rabin_miller_test(num, k)

    @staticmethod
    def generate_prime_candidate(length):
        prime_candidate = getrandbits(length)
        prime_candidate |= (1 << length - 1) | 1
        return prime_candidate

    @staticmethod
    def generate_prime_number(length=1024):
        prime = 4

        while not PrimeGenerator.is_prime(prime, k=10):
            prime = PrimeGenerator.generate_prime_candidate(length)
        return prime