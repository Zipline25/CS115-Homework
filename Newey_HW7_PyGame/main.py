"""
Tristan Newey
3/3/2025
Homework 7 - PyGame
This program will be the beginning of programing frogger, I made the general setting of it.
"""

# initializing pygame
import pygame

pygame.init()

# window dimensions
width = 600
height = 400
screen = pygame.display.set_mode((width, height))

# set window title
pygame.display.set_caption("snake")

# fps
clock = pygame.time.Clock()
dt = 0
speed = 10

"""game loop"""
running = True
while running:
  """ Handle events """
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  """ draw to our screen """
  # clear screen
  screen.fill("black")

  """ draw frog, starting/ending point, and cars """
  # starting point
  pygame.draw.rect(screen, 
   (0,200,0), 
   pygame.Rect((-20,315),(100000,800))
  )
  # ending point
  pygame.draw.rect(screen, 
   (0,200,0), 
   pygame.Rect((-20,0),(100000,40))
  )
  # frog
  pygame.draw.rect(screen, 
   (50,255,255), 
   pygame.Rect((272.5,335),(55,55))
  )
  # red car
  pygame.draw.rect(screen, 
   (255,0,0), 
   pygame.Rect((134,60),(155,60))
  )
  # blue car
  pygame.draw.rect(screen, 
   (0,0,120), 
   pygame.Rect((276,150),(100,65))
  )
  # white car
  pygame.draw.rect(screen, 
   "white", 
   pygame.Rect((345,240),(125,40))
  )
  
  # update screen
  pygame.display.flip()

  #fps
  dt = clock.tick(speed) / 1000

# quit pygame
pygame.quit()