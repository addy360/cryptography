#! /bin/env python3
import time
from random import randint
from matplotlib import pyplot as plt

class OTP():
    def __init__(self):
        self.msg = ''
        self.alpha = "abcdefghijklmnopqrstuvwxyz "

    def echo(self, msg):
        print(f"[+] {msg}", end="\n")

    def generate_random_key(self):
        random_sequence = []
        self.echo("Generating random key from message...")
        time.sleep(1)
        for rand in range(len(self.msg)):
            random_sequence.append(randint(0,len(self.alpha)))
        self.key = random_sequence


    def enc(self):
        self.msg = self.msg.lower()
        cipher_text = ''
        self.generate_random_key()
        self.echo("Encrypting message...")
        time.sleep(1)
        for index , char in enumerate(self.msg):
            key_index = self.key[index]
            char_index = self.alpha.find(char)
            cipher_text = cipher_text + self.alpha[(char_index+key_index)%len(self.alpha)]
        self.echo("Done!")
        return cipher_text

    def dec(self, cipher_text,key=None):
        self.key = key if key is not None else self.key
        plain_text = ''
        self.echo("Decrypting message...")
        time.sleep(1)
        for index, char in enumerate(cipher_text):
            key_index = self.key[index]
            char_index = self.alpha.find(char)
            plain_text = plain_text + self.alpha[(char_index-key_index)%len(self.alpha)]
        self.echo("Done!")
        return plain_text
