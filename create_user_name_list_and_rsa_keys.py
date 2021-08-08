import random
import subprocess
import sys

rsa_key_len=sys.argv[1]
print("rsa_key_len_createeeee: ",rsa_key_len)
print("str(rsa_key_len: ",str(rsa_key_len))

# x=1
# while x%2==1:
# 	x=random.randint(7,10)

# f = open("user_name_list", "w")

# for i in range(0,x):
# 	f.write(str(i))
# 	f.write("\n")

# f.close()	

f = open("Usernames.txt", "r")

for i in f:
	# y=random.randint(0,1)
	print("user: ",i)
	if str(rsa_key_len)=="1024":
		g = open(i[:-1]+"_1024_priv.txt", "w")
		subprocess.call("./generate_public_private_rsa_keys_1024.sh")
		f1=open("private-key.pem","r")
		f2=open("public-key.pem","r")
		# c=0
		# for j in f1:
		# 	c+=1
		#print("c: ",c)	

		f1.close()
		f1=open("private-key.pem","r")

		k=0
		l=0

		for j in f1:
			# #print("k: ",k)
			# #print(i)
			# if(k!=0 and k!=c-1):	
			# 	r=len(j)-1
			# 	#print("r: ",r)
			g.write(j)
				#l+=r
			#k+=1	

		g.close()

		subprocess.run(["cp",i[:-1]+"_1024_priv.txt","./CONF"])	
		subprocess.run(["cp",i[:-1]+"_1024_priv.txt","./AUIN"])	
		subprocess.run(["cp",i[:-1]+"_1024_priv.txt","./COAI"])	

		g = open(i[:-1]+"_1024_pub.txt", "w")
		# c=0
		# for j in f2:
		# 	c+=1
		#print("c: ",c)	

		f2.close()
		f2=open("public-key.pem","r")

		k=0
		l=0

		for j in f2:
			#print("k: ",k)
			# print("1024")
			# print(i)
			# if(k!=0 and k!=c-1):	
			# 	r=len(j)-1
			# 	#print("r: ",r)
			g.write(j)
				#l+=r
			#k+=1	

		g.close()

		subprocess.run(["cp",i[:-1]+"_1024_pub.txt","./CONF"])	
		subprocess.run(["cp",i[:-1]+"_1024_pub.txt","./AUIN"])	
		subprocess.run(["cp",i[:-1]+"_1024_pub.txt","./COAI"])

	#elif y==1:
	elif (rsa_key_len)=="2048":
		g = open(i[:-1]+"_2048_priv.txt", "w")
		subprocess.call("./generate_public_private_rsa_keys_2048.sh")
		f1=open("private-key.pem","r")
		f2=open("public-key.pem","r")
		# c=0
		# for j in f1:
		# 	c+=1
		#print("c: ",c)	

		f1.close()
		f1=open("private-key.pem","r")

		k=0
		l=0

		for j in f1:
			#print("k: ",k)
			#print(i)
			# if(k!=0 and k!=c-1):	
			# 	r=len(j)-1
			# 	#print("r: ",r)
			g.write(j)
				#l+=r
			#k+=1	

		g.close()	

		subprocess.run(["cp",i[:-1]+"_2048_priv.txt","./CONF"])	
		subprocess.run(["cp",i[:-1]+"_2048_priv.txt","./AUIN"])	
		subprocess.run(["cp",i[:-1]+"_2048_priv.txt","./COAI"])

		g = open(i[:-1]+"_2048_pub.txt", "w")
		# c=0
		# for j in f2:
		# 	c+=1
		#print("c: ",c)	

		f2.close()
		f2=open("public-key.pem","r")

		k=0
		l=0

		for j in f2:
			#print("k: ",k)
			#print("2048")
			#print(j)
			#if(k!=0 and k!=c-1):	
			#	r=len(j)-1
			#	#print("r: ",r)
			g.write(j)
			#	l+=r
			#k+=1	

		g.close()	

		subprocess.run(["cp",i[:-1]+"_2048_pub.txt","./CONF"])	
		subprocess.run(["cp",i[:-1]+"_2048_pub.txt","./AUIN"])	
		subprocess.run(["cp",i[:-1]+"_2048_pub.txt","./COAI"])	

# subprocess.run(["rm","_"+str(rsa_key_len)+"_priv.txt"])
# subprocess.run(["rm","_"+str(rsa_key_len)+"_pub.txt"])


# subprocess.run(["rm","./CONF/_"+str(rsa_key_len)+"_priv.txt"])
# subprocess.run(["rm","./CONF/_"+str(rsa_key_len)+"_pub.txt"])

# subprocess.run(["rm","./AUIN/_"+str(rsa_key_len)+"_priv.txt"])
# subprocess.run(["rm","./AUIN/_"+str(rsa_key_len)+"_pub.txt"])

# subprocess.run(["rm","./COAI/_"+str(rsa_key_len)+"_priv.txt"])
# subprocess.run(["rm","./COAI/_"+str(rsa_key_len)+"_pub.txt"])