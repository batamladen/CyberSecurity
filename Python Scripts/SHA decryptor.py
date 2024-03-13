import hashlib
import base64
import os

def cryptBytes(hash_type, salt, value):
    if not hash_type:
        hash_type = "SHA"
    if not salt:
        salt = base64.urlsafe_b64encode(os.urandom(16)).decode('utf-8')

    hash_obj = hashlib.new(hash_type)
    hash_obj.update(salt.encode('utf-8'))
    hash_obj.update(value)
    hashed_bytes = hash_obj.digest()
    result = f"${hash_type}${salt}${base64.urlsafe_b64encode(hashed_bytes).decode('utf-8').replace('+', '.')}"

    return result

def getCryptedBytes(hash_type, salt, value):
    try:
        hash_obj = hashlib.new(hash_type)
        hash_obj.update(salt.encode('utf-8'))
        hash_obj.update(value)
        hashed_bytes = hash_obj.digest()
        return base64.urlsafe_b64encode(hashed_bytes).decode('utf-8').replace('+', '.')
    except Exception as e:
        raise Exception(f"Error while computing hash of type {hash_type}: {e}")

hash_type = "SHA1"
salt = "d"
search = "b8fd41a541a435857a8f3e751cc3a91c174362"
wordlist = 'C:/Users/HP/Downloads/rockyou.txt'

with open(wordlist,'r',encoding='latin-1') as password_list:
    for password in password_list:
        value = password.strip().encode('utf-8')
        hashed_password = cryptBytes(hash_type, salt, value)
        if hashed_password == search:
            print(f'Found Password: {password.strip()}, hash:{hashed_password}')
            break
