#slicing on string
# msg = 'education'
# print(msg[::])      #output : education

# msg = 'education'
# print(msg[::1])     #output : education

# msg = 'education'
# print(msg[::2])     #output : euain

# msg = 'education'
# print(msg[::4])         #output : ean

# a = 'education'
# print(a[1:6:1])         #output : ducat

# a = 'education'
# print(a[2:6:2])         #output : ua

# a = 'education'
# print(a[2:6:2])         #output : ua

# string = 'welcome to python class'
# print(string[0:7])                  #welcome
# print(string[8:10])                 #to
# print(string[11:17])                #python
# print(string[18:23])                #class
# print(string[0:11])                 #welcome to
# print(string[11:23])                #python class
# print(string[3:9])                  #come t
# print(string[5:15])                 #me to pyth
# print(string[:7])                   #welcome
# print(string[8:])                   #to python class

#negative slicing
string = 'welcome to python class'
print(string[-5::])             #class
print(string[-12:-6:])          #python
print(string[-23:-16])          #welcome
print(string[-15:-13])          #to
print(string[-11:-7])           #ytho
print(string[-23:-1])           #welcome to python cals
print(string[:-6])              #welcome to python
print(string[-6:])              #class
print(string[-10:-5])           #thon

#reversing
string = 'welcome to python class'
print(string[::-1])             #ssalc nohtyp ot emoclew
print(string[22::-1])           #ssalc nohtyp ot emoclew
print(string[16:10:-1])         #nohtyp
print(string[-1:-6:-1])         #ssalc
print(string[9::-1])            #ot emoclew
