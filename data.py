import pygame
pygame.init()

clock = pygame.time.Clock()

# Screen settings
WIDTH, HEIGHT = 500, 500
SQUARESPACE = WIDTH // 3
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

BG_COLOR =(0, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0 ,0)

# Lines
h_lines = 2
v_lines = 2
line_width = 7

# Spaces where player puts X or O
spacex = SQUARESPACE
spacey = SQUARESPACE

# This is where we'll save the center position for each space
centerX = []
centerY = []
cols, rows = 3, 3

# Images
cross = pygame.image.load("images/cross.jpg")
cross.set_colorkey(( 255, 255, 255))
cross = pygame.transform.scale(cross, (180, 180))

circle = pygame.image.load("images/circle.png")
circle.set_colorkey((0, 0, 0))
circle = pygame.transform.scale(circle, (130, 130))

# Player score
x_score, o_score = 0, 0

# Creating font
score_font = pygame.font.SysFont('Ariel', 20)
winner_font = pygame.font.SysFont('Ariel', 30)
replay_font = pygame.font.SysFont('Times New Roman', 20)
title_font = pygame.font.SysFont('Times New Roman', 90, bold=True)
modes_font = pygame.font.SysFont('Times New Roman', 22, bold=True)


