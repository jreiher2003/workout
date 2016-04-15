# import winsound
import os
import time
import timeit
import datetime
import sys
from playsound import playsound
import pygame as pg 
import subprocess

__author__ = 'Jeff Reiher'

# import pygame
# pygame.init()
# pygame.display.list_modes()
# from pygame import mixer

def workout():
	# mixer.init()
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
			# Freq = 2000
			# Dur = 1000
			# winsound.Beep(Freq, Dur)
			# mixer.music.load("Yeah.mp3")
			# mixer.music.play()
			# playsound("Yeah.mp3", block=False)
			# os.popen2("cvlc Yeah.mp3 --play-and-exit")
			subprocess.call(['xdg-open','Yeah.mp3'])
			time.sleep(go)
			i+=1
			j+=1
			sys.stdout.write('set # %d   \r' % j) 
			sys.stdout.flush() 
		else:
			# Freq = 3000
			# Dur = 1300
			# winsound.Beep(Freq, Dur)
			# mixer.music.load("Okay.mp3")
			# mixer.music.play()
			# playsound("Okay.mp3", block=False)
			# os.popen2("cvlc Okay.mp3 --play-and-exit")
			subprocess.call(['xdg-open','Okay.mp3'])
			time.sleep(rest)
			i+=1
	Freq = 4000
	Dur = 2500
	# winsound.Beep(Freq,Dur)
	# mixer.music.load("Huh.mp3")
	# mixer.music.play()
	# playsound("Huh.mp3", block=False)
	# os.popen2("cvlc Huh.mp3 --play-and-exit")
	subprocess.call(['xdg-open','Huh.mp3'])
	end_time = (time.time() - start_time)
	m,s = divmod(end_time, 60)
	h, m = divmod(m, 60)
	print '\n'
	print "%d:%02d:%02d" % (h,m,s)
	print str(datetime.timedelta(seconds=end_time))



if __name__ == '__main__':
	workout()