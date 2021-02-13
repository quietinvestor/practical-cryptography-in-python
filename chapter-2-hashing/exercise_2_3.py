from hashlib import md5

test_str_list = [
                 b'bob',
                 b'cob',
                 b'fob',
                 b'gob',
                 b'hob',
                 b'job',
                 b'lob',
                 b'mob',
                 b'nob',
                 b'rob',
                 b'yob',
                ]

def get_md5(byte_str):
  return md5(byte_str).hexdigest()

def hex_to_bin(hex_str):
  return bin(int(hex_str, 16))

def compare_bins(bin_a, bin_b):
  counter = 0
  bin_a = list(bin_a)
  bin_b = list(bin_b)
  bin_diff = abs(len(bin_a) - len(bin_b))
  bin_min_len = min(len(bin_a), len(bin_b))

  if not bin_diff:
    counter += bin_diff

  for i in range(bin_min_len):
    if bin_a[i] == bin_b[i]:
      counter += 1

  return counter / (bin_min_len + bin_diff)

def compare_byte_str_hash_bins(byte_str_a, byte_str_b):
  bin_a = hex_to_bin(get_md5(byte_str_a))
  bin_b = hex_to_bin(get_md5(byte_str_b))

  return compare_bins(bin_a, bin_b)

def compare_byte_str_list_hash_bins(str_list):
  for i in range(len(str_list)):
    str_list_others = str_list[i + 1:] + str_list[:i]
    for j in range(len(str_list_others)):
      print(f'{str_list[i]} vs. {str_list_others[j]}: \
      {compare_byte_str_hash_bins(str_list[i], str_list_others[j]) * 100:.2f} \
      % equal bits')
