import pygame, sys


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load("idle_right.png"))
        self.sprites.append(pygame.image.load("idle_left.png"))
        self.sprites.append(pygame.image.load("idle_up.png"))
        self.sprites.append(pygame.image.load("idle_down.png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect(topleft=(pos_x, pos_y))

    def update(self):
        if self.is_animating == True:
            self.current_sprite += 0.2  # Change this value to control the speed of sprite change
        
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
            self.is_animating = False  # Stop animating after the last sprite
        
        self.image = self.sprites[int(self.current_sprite)]

    def animate(self):
        self.is_animating = True
        self.update()


pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Simple Pygame Window")

#set player height
player_height = 250  # Set the height of the player sprite
# Set player width
player_width = 250  # Set the width of the player sprite
moving_sprites = pygame.sprite.Group()
player = Player(100, 100)
moving_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if event.type == pygame.KEYDOWN:
        player.animate()

    screen.fill((0, 0, 0))  # Clear the screen with black
    moving_sprites.draw(screen)  # Draw all sprites in the group
    moving_sprites.update()  # Update all sprites in the group

    pygame.display.flip()  # Update the display
    clock.tick(60)  # Limit to 60 frames per second