from exercise_1_1 import encode,decode

def auto_decode(encoded_str):
  encoded_str = encoded_str.lower()
  max_words = [0, 0, ""]

  with open('1-1000.txt', 'r') as words:
    english_dictionary = words.read().split('\n')
    dictionary_length = len(english_dictionary)

    for i in range(26):
      decoded_str = decode(encoded_str, i)
      word_counter = 0

      for j in range(dictionary_length):
        if english_dictionary[j] in decoded_str:
          word_counter += 1
    
      if word_counter > max_words[1]:
        max_words = [i, word_counter, decoded_str]

  return max_words
