import sys 
import pygame
from bullet import Bullet
from time import sleep 
from alien import Alien


def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
                ship.moving_left = True
    
    elif event.key ==  pygame.K_SPACE:

        fire_bullet(ai_settings,screen,ship,bullets)

    #添加一个结束游戏的快捷键
    elif event.key == pygame.K_q:
        sys.exit()
            

def check_keyup_events(event,ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
                ship.moving_right = False
    elif event.key == pygame.K_LEFT:
                ship.moving_left = False
    
    


def check_events(ai_settings,screen,ship,bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(ai_setting,screen,ship,aliens,bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    #每次循环时都重新绘制
    screen.fill(ai_setting.bg_color)

    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    #让最新绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    #更新子弹的位置
    bullets.update()


    #删除已消失的子弹
    for bullet in bullets.copy() :
        if bullet.rect.bottom <=0:

            bullets.remove(bullet)

def fire_bullet(ai_settings,screen,ship,bullets):
    """如果还没有达到限制，就发射一颗子弹"""
    ##创建一颗子弹，并将其加入到标注bullets中
    if len(bullets) <  ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

def create_fleet(ai_settings,screen,aliens):
    """创建外星人群"""
    #创建一个外星人，并计算一行可容纳多少个外星人
    #外星人间距外星人宽度
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_space_x / (2*alien_width))

    #创建第一行外星人
    for alien_number in range(number_aliens_x):
        #创建一个外星人并将其加入前行
        alien = Alien(ai_settings,screen)
        alien.x = alien_width + 2 * alien_width *alien_number
        alien.rect.x = alien.x
        aliens.add(alien)