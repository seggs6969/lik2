import os
key = "link"
value = os.getenv(key)
while True:
    os.system(f"python3 l.py {value}")
