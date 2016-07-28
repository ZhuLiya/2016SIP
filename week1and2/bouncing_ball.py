"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
LIYA = (150,180,250)
SEE = (180,220,180)


pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Bouncing Ball Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# WRITE YOUR CODE HERE
XSPEED=3
YSPEED=3
SIZE=30
L=SIZE
XC=random.randint(31,669)
YC=random.randint(31,469)
color=[BLACK,WHITE,GREEN,RED,BLUE,GREY,LIYA]
index=6

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True



    # --- Game logic should go here
    XC+=XSPEED
    YC+=YSPEED
    
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(SEE)

    # --- Drawing code should go here
    pygame.draw.circle(screen,color[index],[XC,YC],SIZE)
    if XC>=700-L or XC<=0+L:
        XSPEED=-XSPEED
        index=random.randint(0,6)
        SIZE=random.randint(20,80)
    if YC>=500-L or YC<=0+L:
        YSPEED=-YSPEED 
        index=random.randint(0,6)
        SIZE=random.randint(20,80)
        
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
