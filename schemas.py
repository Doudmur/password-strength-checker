from pydantic import BaseModel

class Password(BaseModel):
    password: str

class PasswordPolicy(BaseModel):
    length: int
    uppercase: bool
    lowercase: bool
    special: bool
