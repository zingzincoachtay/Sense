#!/usr/bin/python3
from sense_hat import SenseHat

def approx(x):
  return round(x,2)

import a01,a02,a03,a04
import b01,b02
#import a03

sense = SenseHat()

#a01.marquee(sense)

#a02.letter(sense)

#a03.image(sense)
#a03.creeper(sense)
#a03.steve(sense)

#a04.transform(sense)
#a03.flippy(sense)

b01.environment(sense)

b02.orientation(sense)

