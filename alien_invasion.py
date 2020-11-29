import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_heigth))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    #Make a group to store bullets in
    bullets = Group()

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        #get rid of bullets that have disappeared
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))

        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
