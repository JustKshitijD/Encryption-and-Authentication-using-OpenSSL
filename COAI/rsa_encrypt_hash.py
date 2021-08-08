import subprocess
import sys

x=sys.argv[1]
y=sys.argv[2]


subprocess.run(["openssl","rsautl","-sign","-in","hash","-out","rsa_encrypted_hash","-inkey",x+"_"+y+"_priv.txt"])

#openssl rsautl -sign -in hash -out rsa_encrypted_hash -inkey 2_priv_2048.txt   
# else
# 	openssl rsautl -in session_key.txt -out rsa_encrypted_session_key -encrypt -pubin -inkey 6_pub_1024.txt  	 
# fi

