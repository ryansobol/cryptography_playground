from cryptography.fernet import Fernet
import json


def decrypt_entries(entries_encrypted, key):
  entries_encrypted_bytes = entries_encrypted.encode()

  fernet = Fernet(key)

  entries_bytes = fernet.decrypt(entries_encrypted_bytes)

  entries_json = entries_bytes.decode()

  return json.loads(entries_json)
