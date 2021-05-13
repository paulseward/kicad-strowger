#!/usr/bin/env python
import math

# Draw an arc of equally spaced circles
arcRadius  = 400   # Radius of the arc to place the circles on
arcDegrees = 180   # Number of degrees to spread the circles over
arcOffset  = 0     # Angle to start from

pinRadius  = 7     # Radius of the circles
pinCount   = 25    # How many circles to place
pinFill    = '0'   # not filled
# pinFill  = 'f'   # filled with bg colour
# pinFill  = 'F'   # filled with pen colour

# Draw origin pin
print("C 0 0 {} 1 0 N".format(pinRadius))

# arc of pins
for pin in range(0,pinCount):
  angle = math.radians(arcOffset + (pin*arcDegrees/float(pinCount-1)))
  X     = int(round(math.sin(angle)*arcRadius))
  Y     = int(round(math.cos(angle)*arcRadius))

  # Draw the circle:
  # C X Y radius part dmg pen fill
  print("C {} {} {} 1 0 N".format(X,Y,pinRadius))

