#!/bin/bash
# FILE=./6_priv_2048.txt
# if test -f "$FILE"; then
openssl rsautl -decrypt -inkey 6_priv_2048.txt -in rsa_encrypted_session_key_RECV -out session_key_RECV.txt
# else
# 	openssl rsautl -decrypt -inkey 6_priv_1024.txt -in rsa_encrypted_session_key_RECV -out session_key_RECV.txt
# fi		