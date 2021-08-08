import subprocess
import sys

x=sys.argv[1]
y=sys.argv[2]

subprocess.run(["openssl","rsautl","-verify","-pubin","-in","rsa_encrypted_hash_RECV","-out","hash_from_rsa","-inkey",x+"_"+y+"_pub.txt"])
# openssl rsautl -sign -in hash -out rsa_encrypted_hash -inkey 6_priv_2048.txt   
# else
# 	openssl rsautl -in session_key.txt -out rsa_encrypted_session_key -encrypt -pubin -inkey 6_pub_1024.txt  	 
# fi

# openssl rsautl -verify -inkey 6_pub_2048.txt -pubin -in rsa_encrypted_hash_RECV -out hash_from_rsa