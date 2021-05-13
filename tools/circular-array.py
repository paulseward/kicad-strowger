#!/usr/bin/env python
import math

# Draw an arc of equally spaced circles
arcRad=185
pinRad=7
pinCount=10

fill='0' # not filled
# fill='f' # filled with bg colour
#fill='F' # filled with pen colour

# origin pin
print("C 0 0 {} 1 0 N".format(pinRad))

# arc of pins
for pin in range(1,pinCount):
  angle = 180/float(pin)
  X     = int(round(math.sin(angle)*arcRad))
  Y     = int(round(math.cos(angle)*arcRad))

  # Circles:
  # C X Y radius part dmg pen fill
  print("C {} {} {} 1 0 N".format(X,Y,pinRad))

