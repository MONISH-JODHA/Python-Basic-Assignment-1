import random
import string
# cl="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# sl="abcdefghijklmnopqrstuvwxyz"
# spl="!@#$%&*"
# d="0123456789"

# cl=list(cl)
# sl=list(sl)
# spl=list(spl)
# #d=list(int(i) for i in d)
# d=list(d)
# o=[1,1,2,1]
# print (cl,sl,spl,d)

sl=random.choice(string.ascii_lowercase)
cl=random.choice(string.ascii_uppercase)
n=random.choices(string.digits, k=2) 
spl=random.choice('!@#$%&*')
basicpassword=[sl+cl]+n+[spl]
bachahuapasswd=random.choices(string.ascii_letters+string.digits+'!@#$%&*', k=11)
purapassword=bachahuapasswd+basicpassword
random.shuffle(purapassword)
password="".join(purapassword)
print(password)

    