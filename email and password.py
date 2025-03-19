import json
import random
import string

def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{username}@gmail.com"

def generate_random_password(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

count = 5                     

data = []
for _ in range(count):
    entry = {
        "email": generate_random_email(),
        "password": generate_random_password()
    }
    data.append(entry)

filename = "email_and_password.json" 
with open(filename, "w") as f:
    json.dump(data, f, indent=1)

print(f"JSON-файл '{filename}' done!")
