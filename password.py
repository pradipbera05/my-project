import random 
import string
otp=string.digits
# total=string.ascii_letters+string.digits+string.punctuation
length=4
password="".join(random.sample(otp,length))

print(password)