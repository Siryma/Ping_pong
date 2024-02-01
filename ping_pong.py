import pygame
import sys
import random
import time

# Initialize the pygame
pygame.init()

# Set up the game window
width = 900
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ping Pong Game")

# Define the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game variables
ball = pygame.Rect(width / 2 - 15, height / 2 - 15, 30, 30)
player1 = pygame.Rect(width - 20, height / 2 - 70, 10, 140)
player2 = pygame.Rect(10, height / 2 - 70, 10, 140)
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player1_speed = 0
player2_speed = 0
