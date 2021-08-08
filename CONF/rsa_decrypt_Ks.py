import subprocess
import sys
x=sys.argv[1] # receiver
y=sys.argv[2] # rsa_key_len

subprocess.run(['openssl', 'rsautl' ,'-decrypt' ,'-in', 'rsa_encrypted_session_key_RECV' ,'-out' ,'session_key_RECV.txt','-inkey', str(x)+"_"+str(y)+'_priv.txt'])



#openssl rsautl -decrypt -inkey 6_priv_2048.txt -in rsa_encrypted_session_key_RECV -out session_key_RECV.txt
# else
# 	openssl rsautl -decrypt -inkey 6_priv_1024.txt -in rsa_encrypted_session_key_RECV -out session_key_RECV.txt
# fi	