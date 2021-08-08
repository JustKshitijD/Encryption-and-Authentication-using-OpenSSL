
import subprocess
import sys

x=sys.argv[1]
y=sys.argv[2]


subprocess.run(["openssl","rsautl","-decrypt","-inkey",x+"_"+y+"_priv.txt","-in","rsa_encrypted_session_key_RECV","-out","session_key_RECV.txt"])

#openssl rsautl -sign -in hash -out rsa_encrypted_hash -inkey 2_priv_2048.txt   
# else
# 	openssl rsautl -in session_key.txt -out rsa_encrypted_session_key -encrypt -pubin -inkey 6_pub_1024.txt  	 
# fi



#openssl rsautl -in session_key.txt -out rsa_encrypted_session_key -encrypt -pubin -inkey 6_pub_2048.txt  




#openssl rsautl -decrypt -inkey 6_priv_2048.txt -in rsa_encrypted_session_key_RECV -out session_key_RECV.txt
# else
# 	openssl rsautl -decrypt -inkey 6_priv_1024.txt -in rsa_encrypted_session_key_RECV -out session_key_RECV.txt
# fi		