import time
import sys
def slow_print(s):
  for c in s:
    sys.stdout.write( '%s' % c )
    sys.stdout.flush()
    time.sleep(0.02) #Typing speed can be adjusted here.

#Example

slow_print("This script was created by Casey Neale")
