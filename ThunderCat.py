
import pygame as pyg
import numpy as numpy
import time
import random
import keras

done = False
x = 100
y = 100
player_1_pos_x = 780
player_2_pos_x = 20

pos_y = 100


class player_stick():


  player = 0 
  width = 0
  height = 0
  pos_x = 0
  pos_y = 0

  def __init__(self, screen, pos_x, width, height):
    self.width = width
    self.height = height 

    player = pyg.draw.rect( screen, (255,255,255), [pos_x, pos_y, self.width , self.height])
  
  def move(self, screen,pos_x, pos_y):
    
    player = pyg.draw.rect(screen,(255,255,255), [pos_x,pos_y, self.width, self.height])
    
    return player 

  



class ball ():

  t = 0
  q = 0
  dir = 0 
  screen = 0
  dir = random.randint(0,1)
  sign = random.randint(-2,2)
  angle = random.randint(0,300)
  axes_control = random.randint(-4,4)  ##Find somethingwhich will either take 3.5 or -3.5 nothing in between
  boob = 0
  player_stick = 0
  pos_x = 0
  pos_y = 0
  def __init__(self, screen, m, n, ball_width, ball_height):
     #self.player_stick = player_stick
     self.t = m
     '''self.q = n'''
     
     
     self.screen = screen
     self.ball_height = ball_height
     self.ball_width = ball_width
     print "heloo" 
 

  def move(self):
     #self.player_stick = player_stick 
     
     self.angle = self.angle + self.sign
     
     #self.t = self.t + self.axes_control(+3.5 or -3.5 depends on sign)
     self.t = self.t + self.axes_control
     '''self.q = self.q - 3.5'''
     #for  checking the collision with boundaries, we might have to use only one variable on x - axis like angle
     '''print self.q'''
     print self.t     
     print self.angle
     boob = pyg.draw.rect(self.screen,(255,255,255), [self.t,self.angle,ball_width,ball_height])
     return boob
     
     #print self.player_stick.gg


  def collision_with_side(self):
    #Check and change direction if collision with side has happened i.e if collision happened at an angle x, it should get
    #reflected by angle 180 - 2x
    #This will change the angle 
    ###If collision with wall

    if ((self.angle >= 590 or self.angle <=10 )):
       #self.axes_control = -self.axes_control 
       print "hit on top - bottom"
       self.sign = -self.sign
     
    '''
     if ((self.t >= 790 or self.t <= 10)):
       #self.dir = -self.dir 
       print "hit on let - right"
       self.axes_control = -self.axes_control
    '''
     
  
  def collision_with_pl_side():
    #Raise a point to opponent if ball collides with ends
     
     pass


  def collision_with_player(self,boob,player_rect_1,player_rect_2, pos_x, pos_y):
     if (boob.colliderect(player_rect_2)):
        print "ITCOLLIDED!!!!!!!!!"
        self.axes_control = -self.axes_control
        self.sign  = -self.sign
     if (boob.colliderect(player_rect_1)):
        print "ITCOLLIDED!!!!!!!!!"
        self.axes_control = -self.axes_control
        self.sign = -self.sign  
     
    #Check if collision has happened with players stik. if yes, same as collision_with_side
      
      #self.pos_x = pos_x
      #self.pos_y = pos_y
     ''' if (  ((pos_x <= self.t + self.ball_width  <= pos_x + (player_rect_1.width)/2) and ((player_rect_1.height/2) + pos_y >= self.angle ))):
          print "ITCOLLIDED!!!!!!!!!"
          
          self.axes_control = -self.axes_control
          #self.sign = -self.sign       '''
        


class create_game:
  #Create structure 
  #fill colour
  #Push player stick
  
  pyg.init()
  screen = pyg.display.set_mode((800,600))
  pyg.display.set_caption('ThunderCat')
     





 
clock = pyg.time.Clock()
if __name__ == "__main__":
  m = 400
  n = 300 
  #(centre coorinates)
  width = 10
  height = 100
  ball_width = 10
  ball_height = 10
  pos_x = 0
  a = create_game()
  player1 = player_stick(a.screen, player_1_pos_x, width, height)
  player2 = player_stick(a.screen, player_2_pos_x, width, height)
  ball = ball( a.screen, m, n, ball_width, ball_height)
  
  while not done:
        #pos_x = pos_x+50
        #pos_y = pos_y+50
        #b.m.move(1,0)
        #print pos_x
        #m.move(pos_x,pos_y)
        for event in pyg.event.get():
                if event.type == pyg.QUIT:

                        done = True
                if event.type == pyg.KEYDOWN:
                        if event.key == pyg.K_LEFT:
                               pos_x = pos_x - 10
                        if event.key == pyg.K_RIGHT:
                               pos_x = pos_x + 10
                        if event.key == pyg.K_UP:
                               pos_y = pos_y - 10
                        if event.key == pyg.K_DOWN:
                               pos_y  = pos_y +10
          
        a.screen.fill((0,0,0))
        player_rect_1 = player1.move(a.screen,player_1_pos_x, pos_y)
        player_rect_2 = player2.move(a.screen,player_2_pos_x, pos_y)
        boob = ball.move()
        ball.collision_with_side()
        ball.collision_with_player(boob,player_rect_1,player_rect_2, player_1_pos_x, pos_y)
       
        print m,n
        pyg.display.update() 
        clock.tick(30)

  print "Hello World"






















































