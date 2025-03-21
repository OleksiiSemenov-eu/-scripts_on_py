import json
import random
import string

def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{username}@gmail.com"

def generate_random_password(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

count = 5
# You can change this number to generate a different number of objects in the array

data = []
for _ in range(count):
    entry = {
        "email": generate_random_email(),
        "password": generate_random_password()
    }
    data.append(entry)

filename = "email_and_password.json"
# Specify the path before 'email_and_password.json' to save the JSON file.
# If you are using Windows, use double backslashes (\\) in the path.
# If you are using Linux, use a forward slash (/).

with open(filename, "w") as f:
    json.dump(data, f, indent=1)

print(f"JSON-файл '{filename}' done!")
