from random import shuffle
from string import ascii_uppercase
from string import ascii_lowercase

def create_translation_tab(reference_tab):
  encoded_tab = list(reference_tab)
  shuffle(encoded_tab)
  encoded_tab = ''.join(encoded_tab)

  return str.maketrans(reference_tab, encoded_tab), str.maketrans(encoded_tab, reference_tab)

def encode(text, translation_tab, reverse=False):
  if reverse:
    return text.translate(translation_tab[1])
  else:
    return text.translate(translation_tab[0])
