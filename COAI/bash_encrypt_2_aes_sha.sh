#!/bin/bash

#python sha512_generate.py
python sha512_generate.py

#python create_user_name_list_and_rsa_keys.py
#./rsa_encrypt_hash.sh 
python rsa_encrypt_hash.py $1 $3

python merge_enc_hash_and_message.py

gcc create_session_key.c
./a.out

python CONF_encrypt2.py
./encrypt_line

#./rsa_encrypt_Ks.sh
python rsa_encrypt_Ks.py $2 $3

python final_encryption.py

python break_final_enc_for_decryption.py
#./rsa_decrypt_Ks.sh
python rsa_decrypt_Ks.py $2 $3

python CONF_decrypt2.py
chmod a+x ./*
./decrypt_line

python break_enc_hash_and_message.py

python create_hash_from_received_plaintext_sha.py
#./rsa_decrypt_hash.sh
python rsa_decrypt_hash.py $1 $3

python create_final_output.py

python final_compare.py

