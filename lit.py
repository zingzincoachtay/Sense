
#perl -e 'print "[1,";for($k=2;$k<=64;$k++){print ",$k";}print "]";' 
#https://github.com/astro-pi/python-sense-hat
### Perceived brightness of RGB color
#https://stackoverflow.com/questions/596216/formula-to-determine-perceived-brightness-of-rgb-color
# ITU -- International Telecommunication Union
# ITU BT.709 
#Y = 0.2126 R + 0.7152 G + 0.0722 B
# ITU BT.601 
#Y = 0.299 R + 0.587 G + 0.114 B
#Y = 0.33 R + 0.5 G + 0.16 B
#Y = 0.375 R + 0.5 G + 0.125 B
#Y = (R+R+B+G+G+G)/6
#Y = (R+R+R+B+G+G+G+G)>>3

import sys,json,random
#from time import sleep
from sense_hat import SenseHat
sense = SenseHat()

def moduloFloor(num,base):
  return round(num - num % base)
def Brightness(d):
  #if d>0 and d<=5:
  #  return moduloFloor(14 * d,1)
  #if d>5 and d<=10:
  #  return moduloFloor( 7 * d,1)
  #if d>10 and d<=64:
  if d>0 and d<=64:
    return d if d % 1 == 0 else moduloFloor(d,1)
  if d>64 and d<=100:
    return moduloFloor(d*64/100,1) 
  return 64 if d > 100 else d 
def toggle(s,instruction):
  w = (255,255,255) # White
  b = (  0,  0,  0) # Black
  s.set_pixels([w if instruction[k] else b for k in range(len(instruction))] )
def off(s):
  #sleep(6)
  s.clear()

def getRandFile(F,listrandom):
  with open(F,"r") as f:
    try:
      listrandom = json.load(f)
    except:
      print("JSON malformated")
    f.close()
  return listrandom
def setRandFile(F,listrandom):
  with open(F,"w") as f:
    try:
      f.write( json.dumps(listrandom) )
    except:
      print("New JSON not written")
    f.close()
def setPixels(Illumination,lastrandom,given,argc,OnOff):
  random.seed(lastrandom[0])
  random.shuffle(lastrandom)
  Illumination = Brightness(Illumination)
  for j in lastrandom[:Illumination:]:
    OnOff[j-1] = 1
  return OnOff

# later: if randomness is static, change seed by timestamp
#random.seed()
argc = len(sys.argv)
lastrandom = getRandFile(sys.argv[1],[]) if argc>1 else range(1,64)
Darkness = int(sys.argv[2]) if argc>2 else 2
# later: make sure List has the size of at least 64
sz = 64
# later: can change increase rate by Dynamism
# later: allow scale of 5, 10, 12, 16, 100, and 64 (by default)
#Dynamism = 8

#if sys.argv[2]=="monitor" :
#  while(true):
if Darkness==0:
    sense.clear()
    exit#break
if Darkness<0:
    exit
Zeros = [0] * sz # [0 for it in range(sz)]
OnOff = setPixels(Darkness,lastrandom,sys.argv,argc,Zeros)
toggle(sense,OnOff)
#
#Ask for input: Darkness
#
#else:
#    break

setRandFile(sys.argv[1],lastrandom)

