import winsound
import time
import timeit
import datetime
import sys

__author__ = 'Jeff Reiher'

def workout():
	start_time = time.time()
	i = 0
	j = 0	
	go = input('How long to work(seconds): ')
	rest = input('How long to rest(seconds): ')
	sets = input('How many sets(rounds): ')
	sets = sets * 2
	time.sleep(3)
	while i < sets:
		if i %  2 == 0:
			Freq = 2000
			Dur = 1000
			winsound.Beep(Freq, Dur)
			time.sleep(go)
			i+=1
			j+=1
			sys.stdout.write('set # %d   \r' % j) 
			sys.stdout.flush() 
		else:
			Freq = 3000
			Dur = 1300
			winsound.Beep(Freq, Dur)
			time.sleep(rest)
			i+=1
	Freq = 4000
	Dur = 2500
	winsound.Beep(Freq,Dur)
	end_time = (time.time() - start_time)
	m,s = divmod(end_time, 60)
	h, m = divmod(m, 60)
	print '\n'
	print "%d:%02d:%02d" % (h,m,s)
	print str(datetime.timedelta(seconds=end_time))



if __name__ == '__main__':
	workout()