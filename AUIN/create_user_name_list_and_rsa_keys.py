import random
import subprocess

x=1
while x%2==1:
	x=random.randint(7,10)

f = open("user_name_list", "w")

for i in range(0,x):
	f.write(str(i))
	f.write("\n")

f.close()	

f = open("user_name_list", "r")

for i in f:
	y=random.randint(0,1)
	if y==0:
		g = open(i[:-1]+"_priv_1024.txt", "w")
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

		g = open(i[:-1]+"_pub_1024.txt", "w")
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

	elif y==1:
		g = open(i[:-1]+"_priv_2048.txt", "w")
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

		g = open(i[:-1]+"_pub_2048.txt", "w")
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

