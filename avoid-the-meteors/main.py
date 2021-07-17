import pygame, sys, random
from spaceship import SpaceShip
from meteor import Meteor
from laser import Laser

def main_game():
    global laser_active
    laser_group.draw(screen)
    meteor_group.draw(screen)
    spaceship_group.draw(screen)

    laser_group.update()
    meteor_group.update()
    spaceship_group.update()

    if pygame.sprite.spritecollide(spaceship_group.sprite, meteor_group, True):
        spaceship.health -= 1
    
    for laser in laser_group:
        pygame.sprite.spritecollide(laser, meteor_group, True)

    if pygame.time.get_ticks() - laser_timer >= 2000:
        laser_active = True
        spaceship.charge()

    return 1

def end_game():
    text_surface = game_font.render("Game Over", True, (255, 255, 255))
    text_rect = text_surface.get_rect(center = (640, 340))
    screen.blit(text_surface, text_rect)

    score_surface = game_font.render(f"Score: {score}", True, (255, 255, 255))
    score_rect = score_surface.get_rect(center = (640, 380))
    screen.blit(score_surface, score_rect)

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
game_font = pygame.font.Font('./assets/LazenbyCompSmooth.ttf', 40)
score = 0
laser_timer = 0
laser_active = False

spaceship = SpaceShip('./assets/spaceship.png', 640, 500, screen)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

meteor_group = pygame.sprite.Group()
METEOR_EVENT = pygame.USEREVENT
pygame.time.set_timer(METEOR_EVENT, 250) #ms

laser_group = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == METEOR_EVENT:
            meteor_path = random.choice(('./assets/Meteor1.png', './assets/Meteor2.png', './assets/Meteor3.png'))
            random_x_pos = random.randrange(0, 1280)
            random_y_pos = random.randrange(-500, -50)
            random_x_speed = random.randrange(-2, 2)
            random_y_speed = random.randrange(5, 10)
            meteor = Meteor(meteor_path, random_x_pos, random_y_pos, random_x_speed, random_y_speed)
            meteor_group.add(meteor)

        if event.type == pygame.MOUSEBUTTONDOWN and laser_active:
            laser = Laser('./assets/Laser.png', event.pos, 15)
            laser_group.add(laser)
            laser_active = False
            laser_timer = pygame.time.get_ticks()
            spaceship.discharge()

        if event.type == pygame.MOUSEBUTTONDOWN and spaceship.health <= 0:
            spaceship.health = 3
            meteor_group.empty()
            score = 0

    screen.fill((42, 45, 51))

    if spaceship.health > 0:
        score += main_game()
    else:
        end_game()

    pygame.display.update()
    clock.tick(60)