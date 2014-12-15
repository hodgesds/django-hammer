import random
from hashlib import sha256
from base64 import b64encode

def generate_key():
    return b64encode(sha256( str(random.getrandbits(256)) ).digest(), random.choice(['rA','aZ','gQ','hH','hG','aR','DD'])).rstrip('==')