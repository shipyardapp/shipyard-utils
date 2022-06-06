import hashlib


def hash_text(text_var, hash_type='sha256'):
    if hash_type == 'sha256':
        hashed_text = hashlib.sha256(text_var.encode('ascii')).hexdigest()
    return hashed_text
