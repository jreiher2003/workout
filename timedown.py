# import time

# import sys


# def countdown(t): # in seconds
#     for i in range(t,0,-1):
#         print 'tasks done, now sleeping for %d seconds\r' % i,
#         sys.stdout.flush()
#         time.sleep(1)

# # countdown(20)


# def workoutClock():
#   start_time = time.time()
#   end_time = 10
#   for i in range(int(start_time), int(end_time), 1):
#       print i
#       sys.stdout.flush()
#       time.sleep(1)

# # workoutClock()

# #!/usr/bin/env python
# import sys
# import time

# for i in range(1, 1001):
#     time.sleep(1 - time.time() % 1) # sleep until a whole second boundary
#     sys.stderr.write('\r%4d' % i)

#!/usr/bin/python
# import time

# def stopwatch(seconds):
#     start = time.time()
#     time.clock()    
#     elapsed = 0
#     while elapsed < seconds:
#         elapsed = time.time() - start
#         print "loop cycle time: %f, seconds count: %02d" % (time.clock() , elapsed) 
#         time.sleep(1)  

# stopwatch(20)

from sys import stdout
from time import sleep
for i in range(1,20):
    stdout.write("\r%d" % i)
    stdout.flush()
    sleep(1)
# stdout.write("\n") # move the cursor to the next line