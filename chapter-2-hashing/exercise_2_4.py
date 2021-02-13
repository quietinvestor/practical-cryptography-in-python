from hashlib import md5

def file_md5(file_name):
    with open(file_name, 'rb') as f:
        return md5(f.read()).hexdigest()

print(file_md5('file_hash_test'))
