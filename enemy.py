#!/usr/bin/python2

class Enemy:
    'Common base for enemys'
    
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
