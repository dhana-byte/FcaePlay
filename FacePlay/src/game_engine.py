# src/game_engine.py

import pygame
import random
from globals import *

def move_jet(keys):
    global jet_x
    if keys[pygame.K_LEFT] and jet_x > 0:
        jet_x -= jet_speed
    if keys[pygame.K_RIGHT] and jet_x < WIDTH - 60:
        jet_x += jet_speed

def spawn_star():
    if random.randint(1, 20) <= difficulty_level:
        stars.append([random.randint(0, WIDTH - 30), 0])

def move_and_draw_stars(screen):
    for star in stars[:]:
        star[1] += difficulty_level
        pygame.draw.rect(screen, RED, (star[0], star[1], 30, 30))
        if star[1] > HEIGHT:
            stars.remove(star)

def move_and_draw_bullets(screen):
    for bullet in bullets[:]:
        bullet[1] -= 5
        pygame.draw.rect(screen, WHITE, (bullet[0], bullet[1], 5, 10))
        if bullet[1] < 0:
            bullets.remove(bullet)

def handle_collisions():
    global score, game_running
    for star in stars[:]:
        for bullet in bullets[:]:
            if bullet[0] in range(star[0], star[0] + 30) and bullet[1] in range(star[1], star[1] + 30):
                stars.remove(star)
                bullets.remove(bullet)
                score += 10
                break

    for star in stars:
        if jet_y < star[1] + 30 and jet_x < star[0] + 30 and jet_x + 60 > star[0]:
            print("Game Over!")
            game_running = False
