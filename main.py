import pygame, sys
#screen
class Displaysurf():
    def __init__(self, width=1200, height=800):
        self.width = width
        self.height = height
        self.resolution = (self.width, self.height)
        self.displaysurf = pygame.display.set_mode(self.resolution)
    def show(self):
        pygame.display.set_mode(self.resolution)
spawnpoint_1_x = Displaysurf().width/25
spawnpoint_1_y = Displaysurf().height/25
player_y = 0
player_x = 0
class Player1():
    def __init__(self):
        self.move_x = 0
        self.move_y = 0
        self.x = spawnpoint_1_x + self.move_x
        self.y = spawnpoint_1_y + self.move_y
        self.name = "Bob"
        self.color = (0,0,255)
        self.radius = 25
        self.speed = 25
    def show(self):
        pygame.draw.circle(Displaysurf().displaysurf, self.color, (self.x, self.y), self.radius)
    def controls(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_game()
        keys = pygame.key.get_pressed()
        if keys == pygame.K_w:
            self.move_y -= self.speed
        if keys == pygame.K_s:
            self.move_y += self.speed
        if keys == pygame.K_a:
            self.move_x -= self.speed
        if keys == pygame.K_d:
            self.move_x += self.speed
def quit_game():
    pygame.quit()
    sys.exit()

def main():
    pygame.init()
    Displaysurf().show()
    spawnpoint_1_x = Displaysurf().width/25
    spawnpoint_1_y = Displaysurf().height/25
    spawnpoint_2_x = Displaysurf().width/12
    spawnpoint_2_y = Displaysurf().height/12
    FPS = 60
    clock = pygame.time.Clock()
    game_state = "tag"
    while game_state == "tag":
        Player1().x += 5
        Player1().controls()
        Player1().show()
        pygame.display.update()
        pygame.display.flip()
        clock.tick(FPS)

main()
quit_game()