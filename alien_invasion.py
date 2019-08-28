
import sys 
import pygame
from settings import Settings
from ship import *
from enemy import *
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

def run_game():    
        
    #初始化游戏并
    pygame.init()
    ai_settings =Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    

    pygame.display.set_caption("Alien Invaasion")
                 
      
    ship =Ship(screen,ai_settings)
   
    bullets = Group()
    aliens = Group()

    #创建外星人群
    gf.create_fleet(ai_settings,screen,aliens)
    
    #alien = Alien(ai_settings,screen)
    
    #开始游戏的主循环            
    while True:
        
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
 


        ship.update()  
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)
run_game()