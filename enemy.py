#!/usr/bin/python2

class Enemy:
    'Common base for enemys'
     # Define Colors
    
    def draw_stick_figure(screen, x, y):
        import  pygame

        BLACK = (0, 0, 0)
        #WHITE = (255, 255, 255)
        #GREEN = (0, 255, 0)
        RED = (255, 0, 0)
        # Head
        pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)
     
        # Legs
        pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
        pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)
     
        # Body
        pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)
     
        # Arms
        pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
        pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)
        
    def square(self, pos):
        # foobar
        return
        
    def circle(self, pos):
        # foobar
        return
        
    def triangle(self, pos):
        # foobar
        return
    
    def __init__(self, type, level, pos):
        
        if type == "square":
            Enemy.square(self, pos)
        elif type == "triangle":
            Enemy.triangle(self, pos)
        elif type == "circle":
            Enemy.circle(self, pos)
        
        self.speed = level
        self.health = level*5
        return self
    
    def takeDamage(self):
        # foobar
        return
