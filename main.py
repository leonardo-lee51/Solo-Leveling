import pygame
import sys
import os


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        # Load all sprites
        self.load_sprites()
        
        # Animation attributes
        self.current_sprite = 0
        self.animation_speed = 0.15  # Slower for idle animation
        self.image = self.sprites["idle"][self.current_sprite]
        self.rect = self.image.get_rect(topleft=(pos_x, pos_y))
        self.facing = "right"  # Track which direction player is facing
        
        # Animation state
        self.current_animation = "idle"
        self.is_animating = False
        self.animation_cooldown = 0
        
    def load_sprites(self):
        """Load all sprite images into dictionaries"""
        self.sprites = {
            "idle": [
                pygame.image.load("idle_right.png").convert_alpha(),
                pygame.image.load("idle_left.png").convert_alpha(),
                pygame.image.load("idle_up.png").convert_alpha(),
                pygame.image.load("idle_down.png").convert_alpha()
            ],
            # You could add more animation states here like "walk", "attack", etc.
        }
        #Mano ta duro fazer essa cena, mas tudo com dedication and patiente, everthing is possible
        #Carpe Diem, Sieze the day, and make it count!, make it count, carpe diem, carpe diem
        #Carpe Diem, malke it count, make it count, carpe diem, carpe diem carpe diem car pe diem d
        # Carpe dioem , malke i t count, Carpe Diem make itr count, Carp eDiem , makle it count, Carpe diem, make i tcoun t, Cartpe 
        #Carpe Diem, Make it count
        
        # Scale all sprites to consistent size if needed
        for animation in self.sprites:
            for i, sprite in enumerate(self.sprites[animation]):
                self.sprites[animation][i] = pygame.transform.scale(sprite, (200, 400))
    
    def update(self):
        """Update sprite animation"""
        if self.is_animating:
            self.current_sprite += self.animation_speed
            
            # Reset animation if completed
            if self.current_sprite >= len(self.sprites[self.current_animation]):
                self.current_sprite = 0
                self.is_animating = False
                
            self.image = self.sprites[self.current_animation][int(self.current_sprite)]
            
        # Handle animation cooldown
        if self.animation_cooldown > 0:
            self.animation_cooldown -= 1
    
    def animate(self, animation_type="idle"):
        """Start a specific animation"""
        if self.animation_cooldown <= 0:
            self.current_animation = animation_type
            self.current_sprite = 0
            self.is_animating = True
            self.animation_cooldown = 10  # Small cooldown to prevent spamming
    
    def change_facing(self, direction):
        """Change which way the character is facing"""
        self.facing = direction
        # You could implement different sprites based on facing direction


# Main game class
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Improved Animation Demo")
        self.clock = pygame.time.Clock()
        self.bg_color = (30, 30, 40)
        
        # Create sprite group and player
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(100, 100)
        self.all_sprites.add(self.player)
        
    def run(self):
        """Main game loop"""
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
    
    def handle_events(self):
        """Handle user input"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Keyboard controls for animation
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.player.animate("idle")
                    self.player.change_facing("right")
                elif event.key == pygame.K_LEFT:
                    self.player.animate("idle")
                    self.player.change_facing("left")
                elif event.key == pygame.K_UP:
                    self.player.animate("idle")
                    self.player.change_facing("up")
                elif event.key == pygame.K_DOWN:
                    self.player.animate("idle")
                    self.player.change_facing("down")
    
    def update(self):
        """Update game state"""
        self.all_sprites.update()
    
    def draw(self):
        """Draw everything"""
        self.screen.fill(self.bg_color)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()


# Run the game
if __name__ == "__main__":
    game = Game()
    game.run()