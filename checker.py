from pathlib import Path
import json
from schemas import PasswordPolicy
import re
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

settings = load_config()
specials = r"!#$%&'()*+,-./:;<=>?@[\]^_`{|}\"~"
rockyou = load_rockyou()

def check_password(password: str) -> bool:
    policy = settings
    if password in rockyou:
        print(f"Password to common")
        return False
    if len(password) < policy.length:
        print(f"Password too short")
        return False
    if password.upper() == password:
        print(f"Password does not contains lowercase letters")
        return False
    if password.lower() == password:
        print(f"Password does not contains uppercase letters")
        return False
    if not re.search(f"[{specials}]", password):
        print("Password must contain at least one special character")
        return False
    return True
