# This proof-of-concept shows how to enable data integrity, authenticity, and
# confidentiality of Fernet-based journal entries, ensuring the complete privacy
# of a personal thoughts and musings.
#
# See https://github.com/fernet/spec/blob/master/Spec.md#fernet-spec
#
# cipher_text = AES(text, key)
#
# intialization_vector = os.random(16)
#
# hmac = HMAC(version + timestamp, intialization_vector + cipher_text, key)
#
# fernet_token = base64encode(version + timestamp + intialization_vector + cipher_text + hmac)


import decrypter
import getter
import encrypter
import pprint

# Setup

SHARED_KEY = "rxI9N-vcla3cnCPfZZmHmzINnfz8IV-v3tiQlqR0k1I="


# Encrypt journal entries

decrypted_entries = getter.get_decrypted_entries()

encrypted_data = encrypter.encrypt_entries(decrypted_entries, SHARED_KEY)

print(encrypted_data)


# Decrypt journal entries

encrypted_entries = getter.get_encrypted_entries()

decrypted_data = decrypter.decrypt_entries(encrypted_entries, SHARED_KEY)

pprint.pp(decrypted_data)
