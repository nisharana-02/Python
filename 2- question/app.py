# -*- coding: utf-8 -*-
"""
Question#2 
"""

class Bug :
      
      def __init__(self, initialPosition=0 ):
          
          self.pos = initialPosition
          self.dir = "right"

          
      def turn (self):
          
          if self.dir == "right":
              self.dir = "left"
          
          elif self.dir == "left":
              self.dir = "right"
         
          
          
          
      def move (self):
          
          if self.dir == "right":
              self.pos = int(self.getPosition()) + 1
          elif  self.dir == "left":
              self.pos = int(self.getPosition()) - 1
              
          print(self.getPosition())
          
          
      def getPosition (self):
          return self.pos
      
bugsy = Bug (10)
bugsy.move () # Now the position is 11
bugsy.turn ()
bugsy.move () # Now the position is 10   
bugsy.move ()

          


