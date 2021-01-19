# pygameライブラリをインポート
import pygame

# スコアのクラス


class Score:
    def __init__(self, screen, score):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 25)
        self.text = self.font.render(
            'Your Score:'+str(score), True, (255, 255,  255))

    def draw(self):
        self.screen.blit(self.text, (10, 10))
