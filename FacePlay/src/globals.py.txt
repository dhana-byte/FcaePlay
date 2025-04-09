# src/globals.py

# Screen and colors
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)

# Game state
jet_x = WIDTH // 2
jet_y = HEIGHT - 100
jet_speed = 5
bullets = []
stars = []
score = 0
difficulty_level = 2
current_mood = "Neutral"
game_running = True
