# import timeit
# import time

# start = timeit.timeit()
# print "hello"
# time.sleep(3)
# end = timeit.timeit()
# print end - start
import sys

from timeit import default_timer as timer
import time
i = 0
while i < 10:
    start = timer()
    time.sleep(1)
    sys.stdout.write("Count down: %d \r" % (i))
    sys.stdout.flush()
    i += 1


    end = timer()
    print(end - start)  
    start += end
    print start 

# import time
# import sys

# for i in range(100):
#     time.sleep(1)
#     sys.stdout.write("\r%d%%" % i)
#     sys.stdout.flush()

# import time
# from tqdm import tqdm
# for i in tqdm(range(100)):
#   time.sleep(1)