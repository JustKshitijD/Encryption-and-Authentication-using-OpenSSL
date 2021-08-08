#!/bin/bash
# FILE=./6_pub_2048.txt
# if test -f "$FILE"; then
openssl rsautl -in session_key.txt -out rsa_encrypted_session_key -encrypt -pubin -inkey 6_pub_2048.txt  
# else
# 	openssl rsautl -in session_key.txt -out rsa_encrypted_session_key -encrypt -pubin -inkey 6_pub_1024.txt  	 
# fi

