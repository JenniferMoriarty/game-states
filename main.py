import pygame

pygame.init()
screen = pygame.display.set_mode((1200,800)) #screen is a rectangle, not square!
pygame.display.set_caption("game states with mouse menu")

#mouse input
xpos = 0
ypos = 0
mousePos = (xpos, ypos)
mouseDown = False

#game state variable
state = 1 #1 is menu, 2 is playing, 3 is credits
button1 = False
#add more buttons here!
quitGame = False

while 1: #game loop###########################################################
    
    #input section=========================================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #keeps track of mouse position
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos
        #keeps track of mouse button
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouseDown = False
        
        #keyboard input (more needed for actual game)
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_q:
                quitGame = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                quitGame = False
                
                
    #physics/update section=========================================
    #print(mousePos)#uncomment for testing
    
    #state 1: menu state!------------------------------
    if state == 1 and mousePos[0]>100 and mousePos[0]<300 and mousePos[1]>400 and mousePos[1]<550:
        button1 = True
    else:
        button1 = False
            
    if state == 1 and button1 == True and mouseDown == True:
        state = 2
    #state 2: playing state!---------------------------
    if state == 2 and quitGame == True: #pressing quit takes you back to menu
        state = 1
    #regular game physics would go here
    
    
    #render section=========================================
    
    #menu state-------------------------------
    if state == 1:
        screen.fill((230,100,100))# Clear the screen pink
        if button1 == False:
            pygame.draw.rect(screen, (100, 230, 100), (100, 400, 200, 150))
        else:
            pygame.draw.rect(screen, (200, 250, 200), (100, 400, 200, 150))
        pygame.draw.rect(screen, (100, 230, 100), (400, 400, 200, 150))
        pygame.draw.rect(screen, (100, 230, 100), (700, 400, 200, 150))
    
    #game state-------------------------------
    if state == 2:
        screen.fill((80,150,100))# Clear the screen green
        #more game stuff would be drawn here
       
    pygame.display.flip()# Update the display

#end of game loop###################################################################
pygame.quit()


