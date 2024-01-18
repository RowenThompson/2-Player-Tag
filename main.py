import pygame, sys

resolution = dis_width, dis_height = (500, 500)
displaysurf = pygame.display.set_mode(resolution)
game_name = "2 Player Tag"
display_name = pygame.display.set_caption(game_name)
red = (255, 0, 0)
blue = (0, 0, 255)

def quit_game():
    pygame.quit()
    sys.exit()

def change_player_color(player_color, playerr_color):
    if player_color == blue:
        return player_color==red, playerr_color==blue
    if playerr_color == blue:
        return player_color==blue, playerr_color==red

def game_loop():
    pygame.init()
    game_state = "tag"
    player_x = 0
    player_y = 0
    playerr_x = 255
    playerr_y = 255
    speed = 0.025
    player_color = blue
    playerr_color = red
    player_rect = pygame.draw.rect(displaysurf, player_color, pygame.Rect(player_x, player_y, 50, 50))
    playerr_rect = pygame.draw.rect(displaysurf, playerr_color, pygame.Rect(playerr_x, playerr_y, 50, 50))

    while game_state == "tag":
        displaysurf.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                pass
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player_x -= speed

        if keys[pygame.K_d]:
            player_x += speed

        if keys[pygame.K_w]:
            player_y -= speed

        if keys[pygame.K_s]:
            player_y += speed

        if keys[pygame.K_LEFT]:
            playerr_x -= speed

        if keys[pygame.K_RIGHT]:
            playerr_x += speed

        if keys[pygame.K_UP]:
            playerr_y -= speed

        if keys[pygame.K_DOWN]:
            playerr_y += speed

        if player_rect.colliderect(playerr_rect):
            change_player_color(player_color, playerr_color)
        player_rect = pygame.draw.rect(displaysurf, player_color, pygame.Rect(player_x, player_y, 50, 50))
        playerr_rect = pygame.draw.rect(displaysurf, playerr_color, pygame.Rect(playerr_x, playerr_y, 50, 50))
        pygame.display.update()
game_loop()
quit_game()