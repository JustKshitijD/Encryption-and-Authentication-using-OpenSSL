import os

f=open("rsa_encrypted_session_key","rb")
x=f.read()

f2=open("Mail-out.txt","w")

res = ''.join(str(bin(i)) for i in x)
#print("res: ",res)
# y=str(res)
# print("y: ",y)

f2.write(res)
f2.write("\n\n")

f.close()

f=open("session_key_encrypted_message","rb")
x=f.read()

res = ''.join(str(bin(i)) for i in x)
f2.write(res)

f.close()
f2.close()




