from itertools import permutations
from string import ascii_uppercase
from string import ascii_lowercase

def create_translation_tab(reference_tab, permutation_num, reverse=False):
  reference_tab_permutations = permutations(reference_tab)
  for i in range(permutation_num):
    if(i == permutation_num - 1):
      encoded_tab = ''.join(next(reference_tab_permutations))
    else:
      next(reference_tab_permutations)

  if reverse:
    return str.maketrans(encoded_tab, reference_tab)
  else:
    return str.maketrans(reference_tab, encoded_tab)

def encode(text, permutation_num, reverse=False):
  if reverse:
    uppercase_translation = create_translation_tab(ascii_uppercase, permutation_num, True)
    lowercase_translation = create_translation_tab(ascii_lowercase, permutation_num, True)
  else:
    uppercase_translation = create_translation_tab(ascii_uppercase, permutation_num)
    lowercase_translation = create_translation_tab(ascii_lowercase, permutation_num)

  return text.translate(uppercase_translation).translate(lowercase_translation)
