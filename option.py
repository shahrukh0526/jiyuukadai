# pygameライブラリをインポート
import pygame

# 定数群
ATTACK_COLOR = (255, 0, 0)  # 攻撃力UPのボタンの色
HITPOINT_COLOR = (170, 202, 222)  # 体力UPのボタンの色
SPECIALATTACK_COLOR = (255, 255, 0)  # 特殊攻撃のボタンの色

# 攻撃力UPのクラス


class Attack:
    def __init__(self, screen):  # コンストラクタ
        self.screen = screen
        self.button = pygame.Rect(500, 350, 50, 50)
        self.font = pygame.font.SysFont('hgseikaishotaipro', 40)
        self.text = self.font.render("攻", True, (0, 0,  0))

    def draw(self):  # ボタン描画
        pygame.draw.rect(self.screen, ATTACK_COLOR, self.button)
        self.screen.blit(self.text, (505, 360))
# 体力UPのクラス


class HitPoint:
    def __init__(self, screen):  # コンストラクタ
        self.screen = screen
        self.button = pygame.Rect(552, 350, 50, 50)
        self.font = pygame.font.SysFont('hgseikaishotaipro', 40)
        self.text = self.font.render("体", True, (0, 0,  0))

    def draw(self):  # ボタン描画
        pygame.draw.rect(self.screen, HITPOINT_COLOR, self.button)
        self.screen.blit(self.text, (557, 360))

# 特殊攻撃のクラス


class SpecialAttack:
    def __init__(self, screen):  # コンストラクタ
        self.screen = screen
        self.button = pygame.Rect(604, 350, 50, 50)
        self.font = pygame.font.SysFont('hgseikaishotaipro', 40)
        self.text = self.font.render("特", True, (0, 0,  0))

    def draw(self):  # ボタン描画
        pygame.draw.rect(self.screen, SPECIALATTACK_COLOR, self.button)
        self.screen.blit(self.text, (609, 360))
