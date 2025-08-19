# Simple password strength checker
Entry level project to warm up programming and algorithm knowledges. This is API written on python(FastAPI).

## Handlers 
/check - POST
Send password by object below:
```
{
  "password": "P@ssw0rd"
}
```
Sample response:
```
{
  "Result": "Password is unsafe",
  "Entropy score": 52,
  "Strength": "Reasonable"
}
```
