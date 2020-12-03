#! /bin/env python3

from Crypto.Cipher import AES
from Crypto import Random
class My_AES():
    def __init__(self,blocksize=128):
        self.blocksize=blocksize
        self.key = Random.get_random_bytes(16)
    def append_space_padding(self, str):
        pad_len = self.blocksize - (len(str) % self.blocksize)
        padding = ' '*pad_len
        return str + padding

    def remove_space_padding(self,str):
        pad_len = 0
        for char in str[::-1]:
            if char == ' ':
                pad_len+= 1
            else:
                break
        str =  str[:-pad_len]
        return str

    def enc(self, plain_text):
        plain_text = self.append_space_padding(plain_text)
        des =  AES.new(self.key,AES.MODE_ECB)
        return des.encrypt(plain_text.encode('utf-8'))

    def dec(self, cipher_text):
        des = AES.new(self.key,AES.MODE_ECB)
        return self.remove_space_padding(des.decrypt(cipher_text).decode('utf-8'))


