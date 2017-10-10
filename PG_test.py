#!/usr/bin/python2

"""
Program to create 2D Tower Defense war zone




 By Thermoflux
 https://github.com/Thermoflux



"""
def DrawGameWin():    
    
    import pygame,enemy
    
     # Define Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    #RED = (255, 0, 0)
    
    
    # Height and Width of the arena
    HEIGHT = 20
    WIDTH = 20
    
    # Rows and Coloums in arena
    ROW = 30
    COL = 30
    
    # MARGIN BETWEEN CELLS
    MARGIN = 5
    
    # Window size
    WINSIZE = [HEIGHT*ROW+MARGIN*(ROW+1), WIDTH*COL+MARGIN*(COL+1) ]
    
    # Make 2D array as an analogy to our arena
    Grid2D = []
    for row in range(ROW):
        Grid2D.append([])
        for coloum in range(COL):
            Grid2D[row].append(0)
            if (coloum+row)%2 == 0 :
                Grid2D[row].append(2)
    
    # print Grid2D
    
    pygame.init()
    screen = pygame.display.set_mode(WINSIZE)
    
    ''' Need to change '''
    
    # Set title of screen
    pygame.display.set_caption("Array Backed Grid")
     
    # Loop until the user clicks the close button.
    done = False
     
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
     
    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q: # Quit on pressing Q/q
                    done = True                
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                # Set that location to one
                if Grid2D[row][column] == 1:
                    Grid2D[row][column] = 0
                else:  
                    Grid2D[row][column] = 1
                print("Click ", pos, "Grid coordinates: ", row, column)
                
        # Set the screen background
        screen.fill(BLACK)
     
        # Draw the grid
        for row in range(ROW):
            for column in range(COL):
                color = WHITE
                if Grid2D[row][column] == 1:
                    color = GREEN
                if Grid2D[row][column] == 2:
                    color = BLACK
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
                if Grid2D[row][column] != 2:
                    enemy.draw_stick_figure(screen,(MARGIN + WIDTH) * column + MARGIN,
                                    (MARGIN + HEIGHT) * row + MARGIN,)
        # Limit to 60 frames per second
        clock.tick(60)
     
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
    
    
 
    return 

 

 
if __name__ == "__main__":
    DrawGameWin()
