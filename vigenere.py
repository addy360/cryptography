#! /bin/env python3

import time
class Vigenere():
    def __init__(self,secret_key=''):
        self.secret_key = secret_key.lower()
        self.alpha = "abcdefghijklmnopqrstuvwxyz "

    def echo(self, msg):
        print(f"[+] {msg}", end="\n")
    
    def enc(self, plain_text):
        plain_text = plain_text.lower()
        cipher_text = ''
        key_index = 0
        self.echo("Encrypting message...")
        time.sleep(2)
        for char in plain_text:
            index = (self.alpha.find(char) + (self.alpha.find(self.secret_key[key_index]))) % len(self.alpha)
            cipher_text = cipher_text + self.alpha[index]
            key_index+=1
            if key_index == len(self.secret_key):
                key_index = 0
        self.echo("Done!")
        return cipher_text

    def dec(self, cipher_text):
        cipher_text = cipher_text.lower()
        plain_text = ''
        key_index = 0
        self.echo("Decrypting message...")
        time.sleep(2)
        for char in cipher_text:
            index = (self.alpha.find(char) - (self.alpha.find(self.secret_key[key_index]))) % len(self.alpha)
            plain_text = plain_text + self.alpha[index]
            key_index+=1
            if key_index == len(self.secret_key):
                key_index = 0
        self.echo("Done!")
        return plain_text

    


