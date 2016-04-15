# import pygame
# pygame.init()

# pygame.mixer.music.load("Yeah.mp3")
# pygame.mixer.music.play()
# pygame.event.wait()

# import pyxine 
# xine = pyxine.Xine()
# stream = xine.stream_new()
# stream.open("Yeah.mp3")
# stream.play()

import pygame
pygame.init()
# pygame.display.set_mode((200,100))
pygame.mixer.music.load("Yeah.mp3")
pygame.mixer.music.play()

# clock = pygame.time.Clock()
# clock.tick(10)
# while pygame.mixer.music.get_busy():
#     pygame.event.poll()
#     clock.tick(10)