#! /bin/env python3

try:
    from matplotlib import pylab as plt
except Exception as e:
    print(e)
    exit()


class Caeser():

    def __init__(self, key=3):
        self.key = key
        self.alpha = "abcdefghijklmnopqrstuvwxyz "

    def echo(self, msg):
        print(f"[+] {msg}", end="\n")

    def enc(self, plain_text):
        cypher_text = ''
        plain_text = plain_text.lower()
        self.echo("Encrypting message...")
        for char in plain_text:
            index = self.alpha.find(char)
            index = (index + self.key) % len(self.alpha)
            cypher_text = cypher_text + self.alpha[index]
        self.echo("Done!")    
        return cypher_text

    def dec(self, cypher_text):
        plain_text = ''
        cypher_text = cypher_text.lower()
        self.echo("Decrypting message...")
        for char in cypher_text:
            index = self.alpha.find(char)
            index = (index - self.key) % len(self.alpha)
            plain_text = plain_text + self.alpha[index]
        self.echo("Done!")    
        return plain_text

    def brute_caeser(self, cypher_text):
        self.key = 0
        while self.key <= 26:
            dec = self.dec(cypher_text)
            self.echo(f"Using key {self.key} message is {dec}")
            self.key = self.key + 1
        return "[+] Done decrypting!"

    def letter_freq(self, plain_text):
        plain_text = plain_text.lower()
        letter_freq = {}
        self.echo("Calculating letter frequencies...")
        for letter in self.alpha:
            letter_freq[letter] = 0

        for letter in plain_text:
            if letter in letter_freq:
                letter_freq[letter] += 1
        return letter_freq

    def plot_letters(self, letter_freq={}):
        self.echo("Ploting graph...")
        plt.bar(letter_freq.keys(), letter_freq.values())
        plt.xlabel("Letters")
        plt.ylabel("Frequencies")
        plt.xlim([0, len(self.alpha)])
        plt.show()

