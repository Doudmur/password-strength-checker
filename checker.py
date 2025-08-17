from pathlib import Path
import json
from schemas import PasswordPolicy
import re

def load_config(path: str = "config.json") -> PasswordPolicy:
    config_path = Path(path)
    if not config_path.exists():
        raise FileNotFoundError(f"Config file {path} not found")

    with open(config_path, "r") as f:
        raw_config = json.load(f)

    return PasswordPolicy(**raw_config)

settings = load_config()
specials = r"!#$%&'()*+,-./:;<=>?@[\]^_`{|}\"~"

def check_password(password: str) -> bool:
    policy = settings
    if len(password) < policy.length:
        print(f"Password too short")
        return False
    if password.upper == password:
        print(f"Password does not contains lowercase letters")
        return False
    if password.lower == password:
        print(f"Password does not contains uppercase letters")
        return False
    if not re.search(f"[{specials}]", password):
        print("Password must contain at least one special character")
        return False
    return True
