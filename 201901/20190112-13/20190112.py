# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-01-13 16:21:55
@LastEditTime: 2019-01-13 21:31:58
@Description: python版打飞机游戏，12-13两天
'''

import pygame
from sys import exit
from pygame.locals import *
import random

# 设置游戏屏幕大小
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800

#子弹类
class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.midbottom = init_pos
        self.speed = 10

    def move(self):
        self.rect.top -= self.speed

# 玩家飞机类
class Player(pygame.sprite.Sprite):
    def __init__(self, plane_img, player_rect, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = []
        for i in range(len(player_rect)):
            self.image.append(plane_img.subsurface(player_rect[i]).convert_alpha())
        self.rect = player_rect[0]
        self.rect.topleft = init_pos
        self.speed = 8
        self.bullets = pygame.sprite.Group()
        self.img_index = 0
        self.is_hit = False

    def shoot(self, bullet_img):
        bullet = Bullet(bullet_img, self.rect.midtop)
        self.bullets.add(bullet)
    
    def moveUp(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed
    
    def moveDown(self):
        if self.rect.top >= SCREEN_HEIGHT - self.rect.height:
            self.rect.top = SCREEN_HEIGHT - self.rect.height
        else:
            self.rect.top += self.speed

    def moveLeft(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed

    def moveRight(self):
        if self.rect.left >= SCREEN_WIDTH - self.rect.width:
            self.rect.left = SCREEN_WIDTH - self.rect.width
        else:
            self.rect.left += self.speed

class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_img, enemy_down_imgs, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        self.down_imgs = enemy_down_imgs
        self.speed = 2
        self.down_index = 0

    def move(self):
        self.rect.top += self.speed


# 初始化
pygame.init()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('飞机大战')

background = pygame.image.load('./resources/image/background.png').convert()

game_over = pygame.image.load('./resources/image/gameover.png')

plane_img = pygame.image.load('./resources/image/shoot.png')

player_rect = []
player_rect.append(pygame.Rect(0, 99, 102, 126))
player_rect.append(pygame.Rect(165, 360, 102, 126))
player_rect.append(pygame.Rect(165, 234, 102, 126))
player_rect.append(pygame.Rect(330, 624, 102, 126))
player_rect.append(pygame.Rect(330, 498, 102, 126))
player_rect.append(pygame.Rect(432, 624, 102, 126))
player_pos = [200, 600]
player = Player(plane_img, player_rect, player_pos)


bullet_rect = pygame.Rect(1004, 987, 9, 21)
bullet_img = plane_img.subsurface(bullet_rect)


enemyl_rect = pygame.Rect(534, 612, 57, 43)
enemyl_img = plane_img.subsurface(enemyl_rect)
enemyl_down_imgs = []
enemyl_down_imgs.append(plane_img.subsurface(pygame.Rect(267, 347, 57, 43)))
enemyl_down_imgs.append(plane_img.subsurface(pygame.Rect(873, 697, 57, 43)))
enemyl_down_imgs.append(plane_img.subsurface(pygame.Rect(930, 296, 57, 43)))
enemyl_down_imgs.append(plane_img.subsurface(pygame.Rect(930, 687, 57, 43)))

enemiesl = pygame.sprite.Group()

enemies_down = pygame.sprite.Group()

shoot_frequency = 0
enemy_frequency = 0

player_down_index = 16

score = 0

clock = pygame.time.Clock()

running = True

while running:
    clock.tick(60)
    if not player.is_hit:
        if shoot_frequency % 15 == 0:
            player.shoot(bullet_img)
        shoot_frequency += 1
        if shoot_frequency >= 15:
            shoot_frequency = 0

    if enemy_frequency % 50 == 0:
        enemyl_pos = [random.randint(0, SCREEN_WIDTH - enemyl_rect.width), 0]
        enemyl = Enemy(enemyl_img, enemyl_down_imgs, enemyl_pos)
        enemiesl.add(enemyl)
    enemy_frequency += 1
    if enemy_frequency >= 100:
        enemy_frequency = 0

    for bullet in player.bullets:
        bullet.move()
        if bullet.rect.bottom < 0:
            player.bullets.remove(bullet)

    for enemy in enemiesl:
        enemy.move()
        if pygame.sprite.collide_circle(enemy, player):
            enemies_down.add(enemy)
            enemiesl.remove(enemy)
            player.is_hit = True
            break
        if enemy.rect.top < 0:
            enemiesl.remove(enemy)

    enemiesl_down = pygame.sprite.groupcollide(enemiesl, player.bullets, 1, 1)
    for enemy_down in enemies_down:
        enemies_down.add(enemy_down)

    screen.fill(0)
    screen.blit(background, (0, 0))

    if not player.is_hit:
        screen.blit(player.image[player.img_index], player.rect)
        player.img_index = shoot_frequency // 8
    else:
        player.img_index = player_down_index // 8
        screen.blit(player.image[player.img_index], player.rect)
        player_down_index += 1
        if player_down_index > 47:
            running = False

    for enemy_down in enemies_down:
        if enemy_down.down_index == 0:
            pass
        if enemy_down.down_index > 7:
            enemies_down.remove(enemy_down)
            score += 1000
            continue
        screen.blit(enemy_down.down_imgs[enemy_down.down_index // 2], enemy_down.rect)
        enemy_down.down_index += 1

    player.bullets.draw(screen)
    enemiesl.draw(screen)

    score_font = pygame.font.Font(None, 36)
    score_text = score_font.render(str(score), True, (128,128,128))
    text_rect = score_text.get_rect()
    text_rect.topleft = [10, 10]
    screen.blit(score_text, text_rect)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    key_pressed = pygame.key.get_pressed()

    if key_pressed[K_w] or key_pressed[K_UP]:
        player.moveUp()
    if key_pressed[K_s] or key_pressed[K_DOWN]:
        player.moveDown()
    if key_pressed[K_a] or key_pressed[K_LEFT]:
        player.moveLeft()
    if key_pressed[K_d] or key_pressed[K_RIGHT]:
        player.moveRight()


font = pygame.font.Font(None, 48)
text = font.render('Score:' + str(score), True, (255, 0, 0))
text_rect = text.get_rect()
text_rect.centerx = screen.get_rect().centerx
text_rect.centery = screen.get_rect().centery + 24
screen.blit(game_over, (0, 0))
screen.blit(text, text_rect)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()