import pygame
import random
from city import scroller


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
YELLOW=(255,255,150)
FRONT_SCROLLER_COLOR = (0,0,30)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = (17, 9, 39)
LBLUE = (100,150,200)
LRED =(200,100,125)
LGREEN=(170,255,200)
DGREY=(120,120,120)
colors = [WHITE,GREY]

def random_color():
    return random.choice(colors)

# initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Set the title of the window
pygame.display.set_caption("RunnerGame")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



score=0
goodxpos=random.randint(0,800)
goodypos=random.randint(500,600)

class runnersprite(pygame.sprite.Sprite):
    def __init__(self,color,size,width,height,pos):
        pygame.sprite.Sprite.__init__(self)
        self.color=color
        self.size=size
        self.width=width
        self.height=height
        self.pos=pos
        self.image=pygame.Surface((self.width,self.height))
        self.image.fill(self.color)
        # mousepos=pygame.mouse.get_pos()
        self.rect = self.image.get_rect(center = self.pos)

    # def update(self):





front_scroller = scroller(SCREEN_WIDTH, 500, 530, FRONT_SCROLLER_COLOR, 5)
middle_scroller = scroller(SCREEN_WIDTH, 200, 470, MIDDLE_SCROLLER_COLOR, 2)
back_scroller = scroller(SCREEN_WIDTH, 20, 410, BACK_SCROLLER_COLOR, 1)
rodeh= scroller(SCREEN_WIDTH,600,600,DGREY,5)

back_scroller.addbuildings()
middle_scroller.addbuildings()
front_scroller.addbuildings()
    
# goodxpos=random.randint(0,800)
# goodypos=random.randint(500,600)
goodsprite=runnersprite(LGREEN,10,20,20,(goodxpos,goodypos))
good_sprites=pygame.sprite.Group()
good_sprites.add(goodsprite)




# user=runnersprite(BLUE,100)


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    runnerpos=pygame.mouse.get_pos()
    player1=runnersprite(LBLUE,10,40,55,runnerpos)

    all_sprites_list=pygame.sprite.Group()
    all_sprites_list.add(player1)

    if runnerpos==goodxpos:
        score+=1

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    
    screen.fill(BACKGROUND_COLOR)
    
    # for iuasido in range(20):
    # pygame.draw.circle(screen,colors[random.randint(0,1)], (random.randint(110,800),random.randint(10,80),5)

    # --- Drawing code should go here
    for i in range(15):
        pygame.draw.circle(screen,colors[random.randint(0,1)], (random.randint(20,800),random.randint(30,200)),2)
    pygame.draw.circle(screen, YELLOW, (100,50), 30)
    
    # back scroller
    back_scroller.drawbuildings()
    back_scroller.movebuildings()
    
    # middle scroller
    middle_scroller.drawbuildings()
    middle_scroller.movebuildings()

    # front scroller
    front_scroller.drawbuildings()
    front_scroller.movebuildings()

    all_sprites_list.draw(screen)

    good_sprites.draw(screen)

    # user.draw(70,100,20,80)

    # # rode
    # rode.drawbuildings()
    # rode.movebuildings()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)



# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE




# if x position of  runner = goodsprite, score +1