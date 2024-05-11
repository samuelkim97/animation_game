import pygame
import sys


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load("./animation-master/attack_1.png"))
        self.sprites.append(pygame.image.load("./animation-master/attack_2.png"))
        self.sprites.append(pygame.image.load("./animation-master/attack_3.png"))
        self.sprites.append(pygame.image.load("./animation-master/attack_4.png"))
        self.sprites.append(pygame.image.load("./animation-master/attack_5.png"))
        self.sprites.append(pygame.image.load("./animation-master/attack_6.png"))
        self.sprites.append(pygame.image.load("./animation-master/attack_7.png"))
        self.sprites.append(pygame.image.load("./animation-master/attack_8.png"))
        self.sprites.append(pygame.image.load("./animation-master/attack_9.png"))
        self.sprites.append(pygame.image.load("./animation-master/attack_10.png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        
    def update(self):
        self.current_sprite += 1
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]


# general setup
pygame.init()
clock = pygame.time.Clock()

# display
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Animation")

# sprite group
moving_sprites = pygame.sprite.Group()
player = Player(100, 100)
moving_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # drawing
    screen.fill((0, 0, 0))
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()
    clock.tick(60)
