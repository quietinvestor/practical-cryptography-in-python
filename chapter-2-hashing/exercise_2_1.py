from hashlib import md5

def get_md5(byte_str):
  return md5(byte_str).hexdigest()

str_list = [
            b'alice',
            b'bob',
            b'balice',
            b'cob',
            b'a',
            b'aa',
            b'aaaaaaaaaa',
            b'a' * 100000
           ]

for item in str_list:
  print(f'{get_md5(item)}')
