# -*- coding: utf-8 -*-
#!/usr/bin/env python3

# Author: Tahmid Rayat
# Github: https://github.com/htr-tech

"""
MIT License

Copyright (c) 2023 Tahmid Rayat

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
"""

import string
import itertools
import argparse

RE = "\033[0;31m"
GR = "\033[0;32m"
EN = "\033[0m"

banner = """ _    _ _                        
| |  | (_) 
| |  | |_  ____  ____ ____   ____  ____ ____ 
 \ \/ /| |/ _  |/ _  )  _ \ / _  )/ ___) _  )
  \  / | ( ( | ( (/ /| | | ( (/ /| |  ( (/ / 
   \/  |_|\_|| |\____)_| |_|\____)_|   \____)
         (_____|                @htr-tech    
"""

def _exit():
    raise SystemExit('\nExiting...\n')

class Decoder:
    def __init__(self, cipher, key):
        """
        Initializes a Decoder instance for decryption.

        Args:
            cipher (str): Encrypted vigenere ciphertext.
            key (str): The decryption key.
        """
        self.cipher = cipher
        self.key = key

    def decode_char(self, char, key_char):
        alpha_start = 65 if char.isupper() else 97
        decrypted_ord = (ord(char) - ord(key_char)) % 26 + alpha_start
        return chr(decrypted_ord)

    def decode_cipher(self):
        key_cycle = itertools.cycle(self.key)
        decrypted_text = ""

        for char in self.cipher:
            if char.isalpha():
                key_char = (next(key_cycle).upper() if char.isupper()
                            else next(key_cycle).lower())
                decrypted_text += self.decode_char(char, key_char)
            else:
                decrypted_text += char

        return decrypted_text


class BruteForcer:
    def __init__(self, cipher, known_text):
        """
        Initializes a BruteForcer instance for decrypting the encoded 
        cipher using a known part of the plaintext / flag.

        Args:
            cipher (str): Encrypted vigenere ciphertext.
            known_text (str): A known part of the plaintext/flag.
        """
        self.cipher = cipher
        self.known_text = known_text
        # Edit to increase the bruteforce digit length
        self.brute_digit = 1

    def brute_force_decode(self):
        """
        Attempts to decrypt the cipher by bruteforcing and comparing
        with the known part / flag format.

        Returns:
            str: The decryption key if successful, else an empty string.
        """
        found_key = ""
        known_text2 = "".join(filter(lambda x: x.isalpha(), self.known_text))

        for index, digit in enumerate(known_text2):
            for potential_key in string.ascii_lowercase:
                test_key = found_key + potential_key
                decoded_text = Decoder(
                    "".join(filter(lambda x: x.isalpha(), self.cipher)), test_key
                ).decode_cipher()

                if decoded_text[: index + 1] == known_text2[: index + 1]:
                    found_key += potential_key
                    decodeee = Decoder(self.cipher, found_key).decode_cipher()

                    if decodeee[: len(self.known_text)] == self.known_text:
                        return found_key

                    break
            else:
                print(f"[!] No key found for digit: {RE}{digit}{EN}")
                break

        return found_key

    def bruteforce(self, key):
        """
        Attempts to find the decryption key through bruteforce.

        This method generates possible decryption keys and deciphers the
        cipher using each key until a match is found. It allows appending
        additional letters to the key.

        Args:
            key (str): The initial decryption key.
        """
        while True:
            print("")
            for x in itertools.product(string.ascii_lowercase, repeat=self.brute_digit):
                new_key = key + "".join(x)
                new_text = Decoder(self.cipher, new_key).decode_cipher()

                if new_text.startswith(self.known_text):
                    print(f"{EN}Key: {RE}{new_key}{EN} | Flag: {new_text}")
            try:
                try_again = input(f"\n[{RE}E{EN}/{GR}B{EN}] Again Bruteforce ? : ")
                if try_again == "0" or try_again.lower().startswith("e"):
                    _exit()
                
                additional_letters = input(f"\n[+] Append letter: {GR}{key}{RE}")
                key += additional_letters
            except KeyboardInterrupt:
                _exit()


def main(cipher, known_text):
    bruteForcer = BruteForcer(cipher, known_text)
    results = bruteForcer.brute_force_decode()
    print(f"Possible Key: {GR}{results}{EN}")
    decoder = Decoder(cipher, results)
    print(f"Possible Flag: {GR}{decoder.decode_cipher()}{EN}\n")
    
    try:
        inp_brute = input(f"[{RE}E{EN}/{GR}B{EN}] Exit/Bruteforce : ")
        if inp_brute == "0" or inp_brute.lower().startswith("e"):
            _exit()
        else:
            bruteForcer.bruteforce(results)
    except KeyboardInterrupt:
        _exit()


if __name__ == "__main__":
    print(banner)
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--cipher", help="cipher text")
    parser.add_argument("-t", "--text", help="known text / flag format")
    args = parser.parse_args()
    if args.cipher and args.text:
        main(args.cipher, args.text)
    else:
        try:
            cipher = input("Input Cipher Text: ")
            known_text = input(f"Known/Flag Format: {GR}")
            print(f"{EN}")
            main(cipher, known_text)
        except KeyboardInterrupt:
            _exit()

# <catz> 2023-08-12 16:50:28