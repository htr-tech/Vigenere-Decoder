<p align="center">
  <b>Vigenère Cipher Decoder</b>
  <br/>
  Decode / Bruteforce Vigenere cipher text using the Flag Format!!
  <br/><br/>
  <a href="#"><img width="750" alt="Demo" src="./example/example.svg"></a>
</p>

#

### ~$ `time`
<table>
  <tr>
    <th>Script & Source</th>
    <th>Time Taken</th>
  </tr>
  <tr>
    <td>Brutes Each Char (example Dir)</a></td>
    <td>60 Minutes</td>
  </tr>
  <tr>
    <td>Vigenère Cipher Decoder (This)</td>
    <td>0.484 Seconds</td>
  </tr>
</table>

> `vigenere.py -c "RymJHS{XQ_MOWF_TTXU_DBHQBIZR?}" -t "CatCTF"`

#

### ~$ `cat usage.txt`:

- Simply **clone the repository**. Only python should be installed in your system.
  ```bash
  $ git clone https://github.com/htr-tech/Vigenere
  $ cd Vigenere
  $ python vigenere.py
  ```
  > Ouput (Interactive Menu)
  ```
   _    _ _
  | |  | (_)
  | |  | |_  ____  ____ ____   ____  ____ ____
   \ \/ /| |/ _  |/ _  )  _ \ / _  )/ ___) _  )
    \  / | ( ( | ( (/ /| | | ( (/ /| |  ( (/ /
     \/  |_|\_|| |\____)_| |_|\____)_|   \____)
           (_____|                @htr-tech

  Input Cipher Text: RymJHS{XQ_MOWF_TTXU_DBHQBIZR?}
  Known/Flag Format: CatCTF

  Possible Key: python
  Possible Flag: CatCTF{IS_THIS_EVEN_POSSIBLE?}
  ```

- You can also use **command line argument** to run this script.
  ```bash
  usage: vigenere.py [-h] [-c CIPHER] [-t TEXT]

  options:
    -h, --help            show this help message and exit
    -c CIPHER, --cipher CIPHER
                          cipher text
    -t TEXT, --text TEXT  known text / flag format
  ```

#

### ~ $ `cat faq.txt`

- ### What is Vigenère Cipher:
  Vigenère cipher is a polyalphabetic encryption algorithm. It is a method of encrypting alphabetic text using a series of different Caesar ciphers based on the letters of a keyword.

  It is considered a stronger cipher than the Caesar cipher because it uses longer keys that allow the letters to be encrypted in multiple ways, making frequency analysis less effective.

- ### What does this script do?
  This script allows you to decrypt a Vigenere cipher by providing the known part of the plaintext or flag format. It uses a Decoder class to decode the ciphered text with a given key, and a BruteForcer class to attempt to find the decryption key by comparing the flag format with the decrypted text. More details are commented inside the script.

- ### More to be added...


#

### ~$ `./social`:
<p align="left"><br/>
  <a href="https://tahmidrayat.is-a.dev" target="_blank"><img width="120" src="https://img.shields.io/badge/Socials-grey?style=for-the-badge&logo=linktree"></a>
  <a href="https://github.com/htr-tech" target="_blank"><img width="116"src="https://img.shields.io/badge/Github-blue?style=for-the-badge&logo=github"></a>
</p>