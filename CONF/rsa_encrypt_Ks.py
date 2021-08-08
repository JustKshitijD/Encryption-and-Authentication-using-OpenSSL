import subprocess
import sys
x=sys.argv[1] # receiver
y=sys.argv[2] # rsa_key_len

subprocess.run(['openssl', 'rsautl' ,'-in', 'session_key.txt' ,'-out' ,'rsa_encrypted_session_key', '-encrypt', '-pubin', '-inkey', str(x)+"_"+str(y)+'_pub.txt'])


# else
# 	openssl rsautl -in session_key.txt -out rsa_encrypted_session_key -encrypt -pubin -inkey 6_pub_1024.txt  	 
# fi

