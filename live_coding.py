import json

# Leitura do arquivo db.json
with open("db.json", "r") as file:
    db = json.load(file)

def create_user(name, last_name, password):
    username = f"{name}_{last_name}"
    user = {
        "id": len(db["users"]) + 1,
        "username": username,
        "email": f"{username}@gmail.com",
        "password": password,
    }
    db["users"].append(user)
    return user
