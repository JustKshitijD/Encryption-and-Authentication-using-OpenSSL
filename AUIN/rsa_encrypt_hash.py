import subprocess
import sys

x=sys.argv[1]
y=sys.argv[2]

print("x: ",x)
print("y: ",y)

subprocess.run(["openssl","rsautl","-sign","-in","hash","-out","rsa_encrypted_hash","-inkey",x+"_"+y+"_priv.txt"])
#subprocess.run(["openssl","rsautl","-sign","-in","out","-out","rsa_encrypted_hash","-inkey",x+"_"+y+"_priv.txt"])  
