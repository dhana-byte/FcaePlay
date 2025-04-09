# src/main.py

import pygame
import threading
from emotion_detector import detect_emotion
from game_engine import *
from globals import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FacePlay - Jet Shooting Game")
clock = pygame.time.Clock()

jet_img = pygame.image.load("assets/jet.png")
jet_img = pygame.transform.scale(jet_img, (60, 80))

def main():
    global game_running

    # Start emotion detection in a background thread
    emotion_thread = threading.Thread(target=detect_emotion)
    emotion_thread.start()

    while game_running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

        keys = pygame.key.get_pressed()
        move_jet(keys)

        bullets.append([jet_x + 25, jet_y])
        spawn_star()
        move_and_draw_stars(screen)
        move_and_draw_bullets(screen)
        handle_collisions()

        # Draw jet
        screen.blit(jet_img, (jet_x, jet_y))

        # Score, mood, level
        font = pygame.font.SysFont(None, 30)
        screen.blit(font.render(f"Score: {score}", True, WHITE), (10, 10))
        screen.blit(font.render(f"Mood: {current_mood}", True, WHITE), (10, 40))
        screen.blit(font.render(f"Level: {difficulty_level}", True, WHITE), (10, 70))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    emotion_thread.join()

if __name__ == "__main__":
    main()
