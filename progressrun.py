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
		startInterval -= stepInterval
		print startInterval
		j += 1


# this to do here
# 1. turn totTime into minutes
# 2. count down minutes
# 3. different beep on a level change
# 4. add a end beep
# 5. add a keyboardInterrupt Error try/exept block
# 6. defence aganist interval going below a certain level




progressrun(4, 1, 60)



