# =============

ciphertext = "RymJHS{XQ_MOWF_TTXU_DBHQBIZR?}"
flag_heading = "CatCTF"
partial_key = "py"
# Maximum key length to be bruteforced.
max_brute_length = 5

# =============

import itertools
def bruteforce(ciphertext, max_length, partial_key=''):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for length in range(1, max_length + 1):
        for key in itertools.product(alphabet, repeat=length):
            full_key = partial_key + ''.join(key)
            plaintext = ''
            key_index = 0
            for char in ciphertext:
                if char.isalpha():
                    shift = alphabet.index(full_key[key_index])
                    if char.isupper():
                        plaintext += alphabet[(alphabet.index(char.lower()) - shift) % 26].upper()
                    else:
                        plaintext += alphabet[(alphabet.index(char) - shift) % 26]
                    key_index = (key_index + 1) % len(full_key)
                else:
                    plaintext += char
            if flag_heading in plaintext:
                print(f"Key: {full_key}", end=' | ')
                print(f"Flag: {plaintext}")
                return

bruteforce(ciphertext, max_brute_length, partial_key)
