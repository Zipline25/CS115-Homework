"""
Tristan Newey
3/10/2025
Homework 8 - Moving Objects
This program will be the second assignment of creating frogger, where we have the cars and frog move.
"""

# initializing pygame
import pygame
from pygame.constants import KEYDOWN
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

# positioning
cur_pos = [275.5,325]
red_pos = [134,60]
blue_pos = [276,150]
white_pos = [345,240]

"""game loop"""
running = True
while running:
  """ Handle events """
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == KEYDOWN:
        if event.key == pygame.K_ESCAPE: # escape key
            running = False
        if event.key == pygame.K_w: # up direction
            cur_pos[1] -= 24

        if event.key == pygame.K_s: # down direction
            cur_pos[1] += 24
            
        if event.key == pygame.K_a: # left direction
            cur_pos[0] -= 24
            
        if event.key == pygame.K_d: # right direction
            cur_pos[0] += 24

  
  # boundaries for frog
  if cur_pos[0] < 0:
    cur_pos[0] = 0
    
  if cur_pos[0] > width-20:
    cur_pos[0] = width-20
    

  if cur_pos[1] < 0:
    cur_pos[1] = 0
    
  if cur_pos[1] > height-55:
    cur_pos[1] = height-55

  # car movement
  red_pos[0] -= 15
  if red_pos[0] < -155:
    red_pos[0] = width
    
  blue_pos[0] -= 12
  if blue_pos[0] < -100:
    blue_pos[0] = width

  white_pos[0] -= 20
  if white_pos[0] < -125:
    white_pos[0] = width

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
   pygame.Rect((cur_pos[0],cur_pos[1]),(55,55))
  )
  # red car
  pygame.draw.rect(screen, 
   (255,0,0), 
   pygame.Rect((red_pos[0],red_pos[1]),(155,60))
  )
  # blue car
  pygame.draw.rect(screen, 
   (0,0,120), 
   pygame.Rect((blue_pos[0],blue_pos[1]),(100,65))
  )
  # white car
  pygame.draw.rect(screen, 
   "white", 
   pygame.Rect((white_pos[0],white_pos[1]),(125,40))
  )

  # update screen
  pygame.display.flip()

  #fps
  dt = clock.tick(speed) / 1000

# quit pygame
pygame.quit()