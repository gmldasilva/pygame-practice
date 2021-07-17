import pygame, sys, random

pygame.init()

screen = pygame.display.set_mode((640, 360))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

wood_bg = pygame.image.load('./assets/Wood_BG.png')
land_bg = pygame.image.load('./assets/Land_BG.png')
water_bg = pygame.image.load('./assets/Water_BG.png')

cloud1 = pygame.image.load('./assets/Cloud1.png')
cloud2 = pygame.image.load('./assets/Cloud2.png')
crosshair = pygame.image.load('./assets/crosshair.png')
duck_surface = pygame.image.load('./assets/duck.png')

game_font = pygame.font.Font(None, 30)
text_surface = game_font.render('You won!', True, (255, 255, 255))
text_rect = text_surface.get_rect(center = (320, 180))

land_position_y = 260
land_speed = 0.5

water_position_y = 300
water_speed = 1

duck_list = []
for duck in range(10):
    duck_pos_x = random.randrange(50, 600)
    duck_pos_y = random.randrange(50, 320)
    duck_rect = duck_surface.get_rect(center = (duck_pos_x, duck_pos_y))
    duck_list.append(duck_rect)

while True:

    crosshair_rect = crosshair.get_rect(center = pygame.mouse.get_pos())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for index, duck_rect in enumerate(duck_list):
                if duck_rect.collidepoint(event.pos):
                    del duck_list[index]

    screen.blit(wood_bg, (0, 0))

    land_position_y += land_speed
    if land_position_y >= 280 or land_position_y <= 240:
        land_speed *= -1
    screen.blit(land_bg, (0, land_position_y))

    water_position_y += water_speed
    if water_position_y >= 320 or water_position_y <= 280:
        water_speed *= -1
    screen.blit(water_bg, (0, water_position_y))

    for duck_rect in duck_list:
        screen.blit(duck_surface, duck_rect)

    if len(duck_list) <= 0:
        screen.blit(text_surface, text_rect)


    screen.blit(crosshair, crosshair_rect)

    screen.blit(cloud1,(50, 25))
    screen.blit(cloud2,(85, 40))

    screen.blit(cloud1,(302, 5))
    screen.blit(cloud2,(500, 45))
    screen.blit(cloud1,(206, 27))

    pygame.display.update()
    clock.tick(60) # never faster than 120 fps