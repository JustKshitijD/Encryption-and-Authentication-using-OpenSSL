with open("rsa_encrypted_hash","rb") as f:
	for line in f:
		print("len(rsa_encrypted_hash): ",len(line))

with open("merged_enc_hash_and_message","rb") as f:
	for line in f:
		print("len(merged_enc_hash_and_message): ",len(line))		

with open("session_key_encrypted_merged_enc_hash_and_message","rb") as f:
	for line in f:
		print("len(session_key_encrypted_merged_enc_hash_and_message): ",len(line))
		
