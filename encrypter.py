from cryptography.fernet import Fernet
import json


def encrypt_entries(entries, key):
  entries_json = json.dumps(entries)

  entries_bytes = entries_json.encode()

  fernet = Fernet(key)

  entries_encrypted_bytes = fernet.encrypt(entries_bytes)

  return entries_encrypted_bytes.decode()
