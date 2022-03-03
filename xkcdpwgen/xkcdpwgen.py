#!/usr/bin/python3
import argparse
import random
from typing import List

SYMBOLS = [char for char in "~!@#$%^&*.:;"]

WORDS = "words.txt"

def get_n_randoms (n : int, lst : List) : 
    return list(map(lambda _ : lst[random.randint(0, len(lst) - 1)], [None] * n))

def get_random_words(n : int) -> List[str]:
    with open(WORDS, "r") as f:
        lines = f.readlines()
        return get_n_randoms(n, list(map(lambda l: l.rstrip(), lines)))

def modify_words(words: List[str], symbols: List[str], numbers : List[int], n_caps : int):
    return symbols + list(map(lambda w: w.capitalize(), words[:n_caps])) + words[n_caps:] + numbers

def generate_password(num_words : int, num_caps : int, num_numbers : int, num_symbols : int) -> str : 
    words = get_random_words(num_words)
    symbols =  get_n_randoms(num_symbols, SYMBOLS)
    numbers = get_n_randoms(num_numbers, [str(n) for n in range(0,10)])
    return "".join(modify_words(words, symbols, numbers, num_caps))

parser = argparse.ArgumentParser(description="Generate a secure, memorable password using the XKCD method")
parser.add_argument("-w", "--words",  type=int, default=4, help="include WORDS words in the password (default=4)")
parser.add_argument("-c", "--caps",  type=int, default=0, help="capitalize the first letter of CAPS random words (default=0)")
parser.add_argument("-n", "--numbers",  type=int, default=0, help="insert NUMBERS random numbers in the password (default=0)")
parser.add_argument("-s", "--symbols",  type=int, default=0, help="insert SYMBOLS random symbols in the password (default=0)")
args = parser.parse_args()
print(generate_password(int(args.words), int(args.caps), int(args.numbers), int(args.symbols)))
