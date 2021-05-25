import sys
from collections import deque

class RSA:

    def __init__(self, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key

    def power(self, x, m, n):
        a = 1
        while m > 0:
            if m % 2 == 1:
                a = (a * x) % n
            x = (x * x) % n
            m //= 2
        return a

    def encrypting(self, num):
        result = self.power(num, self.public_key['e'], self.public_key['n'])
        return result


    def decrypting(self, num):
        result = self.power(num, self.private_key['d'], self.private_key['n'])
        return result

    def ecb_encrypt_compress(self, IDAT_data_compress):
        key_size = self.public_key['n'].bit_length()
        block_size = key_size//8
        encrypted_data = bytearray()
        padding = bytearray()
        after_iend_data = bytearray()
        self.original_data_len = len(IDAT_data_compress)
        for i in range(0, len(IDAT_data_compress), block_size):
            bytes_block = bytearray(IDAT_data_compress[i:i+block_size])

            #padding
            if len(bytes_block)%block_size != 0:
                for empty in range(block_size - (len(bytes_block)%block_size)):
                    padding.append(0)
                bytes_block = padding + bytes_block

            int_block = int.from_bytes(bytes_block, 'big')
            encrypt_block_int = self.encrypting(int_block)
            encrypt_block_bytes = encrypt_block_int.to_bytes(block_size+1, 'big')
            after_iend_data.append(encrypt_block_bytes[-1])
            encrypt_block_bytes = encrypt_block_bytes[:-1]
            encrypted_data += encrypt_block_bytes

        return encrypted_data, after_iend_data

