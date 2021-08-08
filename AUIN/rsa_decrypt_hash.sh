#!/bin/bash
# FILE=./6_priv_2048.txt
# if test -f "$FILE"; then
# openssl rsautl -decrypt -inkey 6_priv_2048.txt -in rsa_encrypted_session_key_RECV -out session_key_RECV.txt

#$ cat encrypted.txt | base64 -d | openssl rsautl -verify -pubin -inkey public.key -in -
openssl rsautl -verify -inkey 6_pub_2048.txt -pubin -in rsa_encrypted_hash_RECV -out hash_from_rsa
# else
# 	openssl rsautl -decrypt -inkey 6_priv_1024.txt -in rsa_encrypted_session_key_RECV -out session_key_RECV.txt
# fi		