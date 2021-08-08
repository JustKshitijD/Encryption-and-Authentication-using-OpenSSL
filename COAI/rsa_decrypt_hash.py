#!/bin/bash
# FILE=./6_priv_2048.txt
# if test -f "$FILE"; then
# openssl rsautl -decrypt -inkey 6_priv_2048.txt -in rsa_encrypted_session_key_RECV -out session_key_RECV.txt
import subprocess
import sys

x=sys.argv[1]
y=sys.argv[2]

subprocess.run(["openssl","rsautl","-verify","-inkey",x+"_"+y+"_pub.txt","-pubin","-in","rsa_encrypted_hash_RECV","-out","hash_from_rsa"])

#openssl rsautl -sign -in hash -out rsa_encrypted_hash -inkey 2_priv_2048.txt   
# else
# 	openssl rsautl -in session_key.txt -out rsa_encrypted_session_key -encrypt -pubin -inkey 6_pub_1024.txt  	 
# fi




#$ cat encrypted.txt | base64 -d | openssl rsautl -verify -pubin -inkey public.key -in -
#openssl rsautl -verify -inkey 2_pub_2048.txt -pubin -in rsa_encrypted_hash_RECV -out hash_from_rsa
# else
# 	openssl rsautl -decrypt -inkey 6_priv_1024.txt -in rsa_encrypted_session_key_RECV -out session_key_RECV.txt
# fi		