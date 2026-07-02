#modules in pyhton
#Types of modules 
#1.Built-in Modules
"""math, random,sys,datetime"""

#math
import math
print(math.sqrt(16))            #4

#Random
#OTP generator
import random
otp = ''
for i in range (6):
    digit = random.randint(0,9)
    otp = otp +str (digit)
print(f'Generated OTP is : {otp}')

#datetime
import datetime
now = datetime.datetime.now()
print(now)              #2026-04-29 22:17:35.240954

#sys
import sys
print(sys.version)          #3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)]

