
import subprocess
   
# with open("hash",'w') as fp:
# 		fp.write("openssl enc -des-ede3-cbc -in plaintext -K " + str(data)+ " -iv " +str(data2)+ " -out session_key_encrypted_message\n")

f=open("out","w")
subprocess.run(["openssl" ,"dgst" ,"-sha512","plaintext"],stdout=f)

f=open("out","r")
for line in f:
	for word in line.split():
		if '=' not in word:
			print(word)
			f2=open("hash","w")
			f2.write(word)
