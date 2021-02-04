from string import ascii_uppercase
from string import ascii_lowercase

def create_translation_tab(reference_tab, offset):
  return str.maketrans(reference_tab, reference_tab[offset:] + reference_tab[:offset])

def encode(plain_text, offset):
  uppercase_translation = create_translation_tab(ascii_uppercase, offset)
  lowercase_translation = create_translation_tab(ascii_lowercase, offset)

  return plain_text.translate(uppercase_translation).translate(lowercase_translation)

def decode(encoded_text, offset):
  return encode(encoded_text, -offset)
