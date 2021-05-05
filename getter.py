import json

with open("entries.decrypted.json", "r") as file:
  content = file.read()

decrypted_entries = json.loads(content)

with open("entries.encrypted.txt", "r") as file:
  encrypted_entries = file.read()

def get_decrypted_entries():
  return decrypted_entries

def get_encrypted_entries():
  return encrypted_entries
