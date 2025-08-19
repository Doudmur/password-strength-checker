from pathlib import Path
import json
from schemas import PasswordPolicy
import re
import math
import string
import pickle

def load_config(path: str = "config.json") -> PasswordPolicy:
    config_path = Path(path)
    if not config_path.exists():
        raise FileNotFoundError(f"Config file {path} not found")

    with open(config_path, "r") as f:
        raw_config = json.load(f)

    return PasswordPolicy(**raw_config)

def load_rockyou(path: str = "rockyou.pkl") -> any:
    rockyou_path = Path(path)
    if not rockyou_path.exists():
        raise FileNotFoundError(f"Rockyou file {path} not found")

    with open(rockyou_path, "rb") as f:
        bloom = pickle.load(f)

    return bloom


def password_entropy(password: str) -> float:
    pool = 0
    if any(c.islower() for c in password):
        pool += 26
    if any(c.isupper() for c in password):
        pool += 26
    if any(c.isdigit() for c in password):
        pool += 10
    if any(c in string.punctuation for c in password):
        pool += len(string.punctuation)

    # bits of entropy
    return round(len(password) * math.log2(pool), 2)

settings = load_config()
specials = r"!#$%&'()*+,-./:;<=>?@[\]^_`{|}\"~"
rockyou = load_rockyou()

def check_password(password: str) -> (bool, float, string):
    entropy = math.floor(password_entropy(password))
    if entropy < 28: entropy_rank = "Very weak"
    elif 28 <= entropy <= 35: entropy_rank = "Weak"
    elif 36 <= entropy <= 59: entropy_rank = "Reasonable"
    elif 60 <= entropy <= 127: entropy_rank = "Strong"
    else: entropy_rank = "Very strong"
    policy = settings
    if password in rockyou:
        print(f"Password to common")
        return False, entropy, entropy_rank
    if len(password) < policy.length:
        print(f"Password too short")
        return False, entropy, entropy_rank
    if password.upper() == password:
        print(f"Password does not contains lowercase letters")
        return False, entropy, entropy_rank
    if password.lower() == password:
        print(f"Password does not contains uppercase letters")
        return False, entropy, entropy_rank
    if not re.search(f"[{specials}]", password):
        print("Password must contain at least one special character")
        return False, entropy, entropy_rank
    return True, entropy, entropy_rank
