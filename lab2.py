import sys
import subprocess
import os


n=len(sys.argv)

# subprocess.run(['gcc','create_plaintext.c'])
# subprocess.run(['./a.out'])
subprocess.run(['cp','Mail-sample.txt','plaintext'])
subprocess.run(['cp','plaintext','./CONF/'])
subprocess.run(['cp','plaintext','./AUIN/'])
subprocess.run(['cp','plaintext','./COAI/'])

if(int(n)==4 and str(sys.argv[1])=="CreateKeys"):
	rsa_key_len=sys.argv[3]
	print("rsa_key_len: ",rsa_key_len)
	subprocess.run(['python','create_user_name_list_and_rsa_keys.py',str(rsa_key_len)])	


if(str(sys.argv[1])=="CreateMail"):
	#print(sys.argv[2])
	#print(sys.argv[7])
	if(str(sys.argv[2])=="CONF"):  # has 9 arguements (no sha)
		if(str(sys.argv[7])=="aes-256-cbc"):
			os.chdir("CONF")
			subprocess.run(["./bash_encrypt_2_aes.sh",str(sys.argv[3]),str(sys.argv[4]),str(sys.argv[8])]) #(sender,receiver,rsa_key_len)
			subprocess.run(["cp","Mail-out.txt","../"])
			#print(os.getcwd())
			os.chdir("../")
			#print(os.getcwd())
		elif(str(sys.argv[7])=="des-ede3-cbc"):
			os.chdir("CONF")
			subprocess.run(["./bash_encrypt_2_des.sh",str(sys.argv[3]),str(sys.argv[4]),str(sys.argv[8])]) #(sender,receiver,rsa_key_len)
			subprocess.run(["cp","Mail-out.txt","../"])
			os.chdir("../")

	elif(str(sys.argv[2])=="AUIN"):  # has 9 arguements (no sha)
		#print("in auin")
		if(str(sys.argv[7])=="sha512"):
			os.chdir("AUIN")
			subprocess.run(["./bash_encrypt_sha.sh",str(sys.argv[3]),str(sys.argv[4]),str(sys.argv[8])]) #(sender,receiver,rsa_key_len)
			subprocess.run(["cp","Mail-out.txt","../"])
			os.chdir("../")
		elif(str(sys.argv[7])=="sha3-512"):
			os.chdir("AUIN")
			subprocess.run(["./bash_encrypt_sha3.sh",str(sys.argv[3]),str(sys.argv[4]),str(sys.argv[8])]) #(sender,receiver,rsa_key_len)
			subprocess.run(["cp","Mail-out.txt","../"])
			os.chdir("../")


	elif(str(sys.argv[2])=="COAI"):  # has 9 arguements (no sha)
		#print("in auin")
		if(str(sys.argv[7])=="sha512" and str(sys.argv[8])=="des-ede3-cbc"):
			os.chdir("COAI")
			subprocess.run(["./bash_encrypt_2_des_sha.sh",str(sys.argv[3]),str(sys.argv[4]),str(sys.argv[9])]) #(sender,receiver,sha512,aes-256,2048)
			subprocess.run(["cp","Mail-out.txt","../"])
			os.chdir("../")

		elif(str(sys.argv[7])=="sha512" and str(sys.argv[8])=="aes-256-cbc"):
			#print("Heyyy")
			os.chdir("COAI")
			subprocess.run(["./bash_encrypt_2_aes_sha.sh",str(sys.argv[3]),str(sys.argv[4]),str(sys.argv[9])]) #(sender,receiver,sha512,aes-256,2048)
			subprocess.run(["cp","Mail-out.txt","../"])
			os.chdir("../")

		elif(str(sys.argv[7])=="sha3-512" and str(sys.argv[8])=="des-ede3-cbc"):
			os.chdir("COAI")
			subprocess.run(["./bash_encrypt_2_des_sha3.sh",str(sys.argv[3]),str(sys.argv[4]),str(sys.argv[9])]) #(sender,receiver,sha512,aes-256,2048)
			subprocess.run(["cp","Mail-out.txt","../"])
			os.chdir("../")

		elif(str(sys.argv[7])=="sha3-512" and str(sys.argv[8])=="aes-256-cbc"):
			os.chdir("COAI")
			subprocess.run(["./bash_encrypt_2_aes_sha3.sh",str(sys.argv[3]),str(sys.argv[4]),str(sys.argv[9])]) #(sender,receiver,sha512,aes-256,2048)
			subprocess.run(["cp","Mail-out.txt","../"])
			os.chdir("../")
		
		
				
					

elif(str(sys.argv[1])=="ReadMail"):
	if(str(sys.argv[2])=="CONF"):
		subprocess.run(["cp","CONF/decrypted_plaintext","CONF/Mail-decrypt.txt"])
		subprocess.run(["cp","CONF/Mail-decrypt.txt","."])
	if(str(sys.argv[2])=="AUIN"):
		subprocess.run(["cp","AUIN/plaintext_RECV","AUIN/Mail-decrypt.txt"])
		subprocess.run(["cp","AUIN/Mail-decrypt.txt","."])
	if(str(sys.argv[2])=="COAI"):
		subprocess.run(["cp","COAI/plaintext_RECV","COAI/Mail-decrypt.txt"])
		subprocess.run(["cp","COAI/Mail-decrypt.txt","."])
			
			