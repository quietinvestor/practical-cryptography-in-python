from hashlib import md5
from random import choice
from statistics import mean
from string import ascii_lowercase
from time import time

alphabet = list(ascii_lowercase)
alphabet_bytes = []

for letter in alphabet:
    alphabet_bytes.append(bytes(letter, 'ascii'))

duration_list = []

for i in range(10):
    preimage_seed = choice(alphabet_bytes)
    test_hash = md5(preimage_seed).hexdigest()
    start_time = time()
    
    for letter in alphabet_bytes:
        if md5(letter).hexdigest() == test_hash:
            duration = time() - start_time
            duration_list.append(duration)
            print(f'{letter} is the preimage_seed! - {duration:.10f} seconds')
            break

print(f'\nAverage: {mean(duration_list):.10f} seconds')
