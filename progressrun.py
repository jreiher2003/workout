import winsound
import time

def progressrun(startInterval, stepInterval, totTime):
    j = 0
    while j < totTime:
        i = 0 
        while i < 4:
            winsound.Beep(440, 250)
            time.sleep(startInterval) 
            i += 1
            print i
        if startInterval == 1: 
            startInterval = 1
        else:
            startInterval -= stepInterval
        print 'new interval ' + str(startInterval)


        j += 1
        print 'Jloop ' + str(j)


# this to do here
# 1. turn totTime into minutes (maybe)
# 2. count down minutes
# 3. different beep on a level change
# 4. add an end beep
# 5. add a keyboardInterrupt Error try/exept block
# 6. defence aganist interval going below a certain level
# 7 change tot to levels




progressrun(5, 1, 10)



