# pygameライブラリをインポート
import pygame

# HP表示のクラス


class Hp:
    def __init__(self, screen, hp):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 25)
        self.text = self.font.render(
            'Your HP:'+str(hp), True, (255, 255,  255))

    def draw(self):
        self.screen.blit(self.text, (10, 36))
