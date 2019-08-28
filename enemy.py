import sys 
import pygame

class Enemy():
    def __init__(self,screen):
        self.screen = screen
        
        #加载敌人的图像
        self.image = pygame.image.load('d:\\xinxin\\python_work\\python_pygame\\images\\diren.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #将敌人放在屏幕中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)