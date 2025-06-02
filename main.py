import pygame 

pygame.init()
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solo Leveling Battle Screen")


# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HP_RED = (200, 0, 0)
HP_GREEN = (0, 255, 0)

FONT = pygame.font.Font(None, 36)
NAME_FONT = pygame.font.Font(None, 40)

# Botão estilizado com bordas e efeitos


class FancyButton:
    def __init__(self, text, x, y, width, height, base_color, hover_color):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.base_color = base_color
        self.hover_color = hover_color
        self.color = base_color
        self.hovered = False
        self.border_color = (255, 215, 0)

    def draw(self, win):
        mouse_pos = pygame.mouse.get_pos()
        self.hovered = self.rect.collidepoint(mouse_pos)
        self.color = self.hover_color if self.hovered else self.base_color

        pygame.draw.rect(win, self.border_color, self.rect.inflate(10, 10), border_radius=12)
        pygame.draw.rect(win, self.color, self.rect, border_radius=10)
        
        text_surface = FONT.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        win.blit(text_surface, text_rect)

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(event.pos)
    
    
def battle_screen():
    clock = pygame.time.Clock()
    running = True

    attack_btn = FancyButton("Attack", 550, 400, 200, 50, (120, 0, 0), (180, 30, 30))
    skill_btn = FancyButton("Skill", 550, 470, 200, 50, (0, 0, 120), (30, 30, 180))

    hp = 100
    max_hp = 100
    player_name = "Jinwoo"