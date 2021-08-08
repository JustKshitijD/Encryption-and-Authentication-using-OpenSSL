#!/bin/bash
# FILE=./6_pub_2048.txt
# if test -f "$FILE"; then
# openssl rsautl -in hash -out rsa_encrypted_hash -encrypt -pubin -inkey 6_pub_2048.txt 
#$ echo "$TEXT" | openssl rsautl -sign -inkey private.key -in - -out - | base64 > encrypted.txt

openssl rsautl -sign -in hash -out rsa_encrypted_hash -inkey 6_priv_2048.txt   
# else
# 	openssl rsautl -in session_key.txt -out rsa_encrypted_session_key -encrypt -pubin -inkey 6_pub_1024.txt  	 
# fi

