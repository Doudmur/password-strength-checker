from fastapi import FastAPI
from schemas import Password
from checker import check_password

app = FastAPI()


@app.post("/check")
def read_root(password: Password):
    check, entropy, entropy_rank = check_password(password.password)
    if check: message = "Password is safe"
    else: message = "Password is unsafe"
    return {"Result": message, "Entropy score": entropy, "Strength": entropy_rank}