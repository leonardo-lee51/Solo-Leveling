import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
EARTH_IMAGE = 'Earth.png'  # Make sure to have an earth image in the same directory

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spinning Earth")

# Load the Earth image
earth = pygame.image.load(EARTH_IMAGE)
earth = pygame.transform.scale(earth, (200, 200))  # Resize the image


# Main loop
def main():
    clock = pygame.time.Clock()
    angle = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill((0, 0, 0))

        # Rotate the Earth
        rotated_earth = pygame.transform.rotate(earth, angle)
        angle += 1  # Increase the angle for spinning

        # Get the rectangle of the rotated image
        rect = rotated_earth.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        # Draw the rotated Earth
        screen.blit(rotated_earth, rect.topleft)

        # Update the display
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()