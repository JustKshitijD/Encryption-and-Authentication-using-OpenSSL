#!/bin/bash

gcc create_session_key_3_des.c
./a.out

python CONF_encrypt2.py 
./run_encrypt_line.sh

#./rsa_encrypt_Ks.sh
python rsa_encrypt_Ks.py $2 $3

python final_encryption.py

python break_final_enc_for_decryption.py $3
#./rsa_decrypt_Ks.sh 
python rsa_decrypt_Ks.py $2 $3

python CONF_decrypt2.py
./run_decrypt_line.sh

python create_output_file.py