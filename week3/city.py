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

# # Define some colors
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
# BLUE = (0, 0, 255)
# GREY = (129, 129, 129)
# YELLOW=(255,255,150)
# FRONT_SCROLLER_COLOR = (0,0,30)
# MIDDLE_SCROLLER_COLOR = (30,30,100)
# BACK_SCROLLER_COLOR = (50,50,150)
# BACKGROUND_COLOR = (17, 9, 39)
# LBLUE = (100,150,200)
# LRED =(200,100,125)
# LGREEN=(170,255,200)
# DGREY=(30,30,30)
# colors = [WHITE,GREY]
# colorss=[LBLUE,LGREEN]

def random_color():
    return random.choice(colors)

# # initialize the pygame class
# pygame.init()

# # Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# # Set the title of the window
# pygame.display.set_caption("CityScroller")

# # Loop until the user clicks the close button.
# done = False

# # Used to manage how fast the screen updates
# clock = pygame.time.Clock()





class building():


    def __init__(self, x_point, y_point, width, height, color):
        self.x_point=x_point
        self.y_point=y_point
        self.width=width
        self.height=height
        self.color=color
    def draw(self):

        pygame.draw.rect(screen, self.color, (self.x_point, self.y_point, self.width, self.height))
        
       
    def move(self, speed):
        self.x_point+= speed


class scroller(object):


    def __init__(self, width, height, base, color, speed):
        self.width=width
        self.height=height
        self.base=base
        self.color=color
        self.speed=speed
        self.list1=[]
        self.currentwidth = 0
        self.list2=[]
    
    def addbuildings(self):
           #width of scroller: self.width
           #width of all buildings (list1) 
           #until width of buildings equal to the width of the scroller
           #call addbuilding
        while self.currentwidth < self.width:
            self.addbuilding(self.currentwidth)


    def addbuilding(self, x_location):
        #create buildings, and add them to a list. use 'sppend' to call the draw function
        width1=random.randint(30,80)
        self.currentwidth+=width1
        height1 = random.randint(-250,-80)
        building1= building(x_location,self.base,width1,height1,self.color)
        self.list1.append(building1)


    # def creatrode(self,x_location):
    #     width9=100
    #     self.currentwidth+=width9
    #     rode1=building(x_location,self.base,width9,10,self.color)
    #     self.list2.append(rode1)

    def drawbuildings(self):
        for building2 in self.list1:
            building2.draw()
        for rode2 in self.list2:
            rode2.draw()

    def movebuildings(self):
        for building2 in self.list1:
            building2.move(self.speed)
        for rode2 in self.list2:
            rode2.move(self.speed)

        firstbuilding=self.list1[0]
        lastbuilding= self.list1[-1]
        
        # firstrode=self.list2[0]
        # lastrode=self.list2[-1]
        
        if firstbuilding.x_point>=0:
            width1=random.randint(30,80)
            height1 = random.randint(-220,-80)
            building3=building(firstbuilding.x_point-width1,self.base,width1,height1,self.color)
            self.list1.insert(0,building3)
        if lastbuilding.x_point>=800:
            self.list1.remove(lastbuilding)


        # if firstrode.x_point>=0:
        #     width9=100
        #     rode3=building(firstrode.x_point-width9,self.base,width9,10,self.color)
        #     self.list2.insert(0,rode3)
        # if lastrode.x_point>=800:
        #     self.list2.remove(lastrode)

# class rode7(scroller):
#     def __init__()



# front_scroller = scroller(SCREEN_WIDTH, 500, 530, LBLUE, 5)
# middle_scroller = scroller(SCREEN_WIDTH, 200, 470, LRED, 2)
# back_scroller = scroller(SCREEN_WIDTH, 20, 410, LGREEN, 1)
# rodeh= scroller(SCREEN_WIDTH,600,600,DGREY,5)


# back_scroller.addbuildings()
# middle_scroller.addbuildings()
# front_scroller.addbuildings()
# # rodeh.addbuildings()


# # -------- Main Program Loop -----------
# while not done:
#     # --- Main event loop
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True

#     # --- Game logic should go here

#     # --- Screen-clearing code goes here

#     # Here, we clear the screen to white. Don't put other drawing commands
#     # above this, or they will be erased with this command.

#     # If you want a background image, replace this clear with blit'ing the
#     # background image.
    
#     screen.fill(BACKGROUND_COLOR)
    
#     # for iuasido in range(20):
#     # pygame.draw.circle(screen,colors[random.randint(0,1)], (random.randint(110,800),random.randint(10,80),5)

#     # --- Drawing code should go here
#     for i in range(15):
#         pygame.draw.circle(screen,colors[random.randint(0,1)], (random.randint(0,800),random.randint(10,200)),2)
#     pygame.draw.circle(screen, YELLOW, (100,50), 30)
    
#     # back scroller
#     back_scroller.drawbuildings()
#     back_scroller.movebuildings()
    
#     # middle scroller
#     middle_scroller.drawbuildings()
#     middle_scroller.movebuildings()

#     # front scroller
#     front_scroller.drawbuildings()
#     front_scroller.movebuildings()

#     # # rode
#     # rode.drawbuildings()
#     # rode.movebuildings()

#     # --- Go ahead and update the screen with what we've drawn.
#     pygame.display.flip()

#     # --- Limit to 60 frames per second
#     clock.tick(60)

# # Close the window and quit.
# pygame.quit()
# exit() # Needed when using IDLE
