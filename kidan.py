# pygameライブラリをインポート
import pygame

# 定数群
KIDAN_VX = -30  # 気弾の速さ
KIDAN_POWER = 50  # 気弾のパワー
SPECIALKIDAN_VX = -80  # 特殊攻撃の気弾の速さ

# 気弾のクラス


class Kidan(pygame.sprite.Sprite):  # Sprite継承
    def __init__(self, screen, x, y):  # コンストラクタ
        super().__init__()
        self.screen = screen
        self.vx = KIDAN_VX
        self.power = KIDAN_POWER
        self.rect = pygame.Rect(x, y, 85, 55)
        self.image = pygame.image.load("kidan.jpg")  # 気弾の画像を読み込む
        self.image = self.image.convert()  # 画像を変換する

    def update(self):  # 描画位置を移動させる
        self.rect.move_ip(self.vx, 0)

# 特殊攻撃の気弾


class SpecialKidan(pygame.sprite.Sprite):  # Sprite継承
    def __init__(self, screen, x, y):  # コンストラクタ
        super().__init__()
        self.screen = screen
        self.vx = SPECIALKIDAN_VX
        self.rect = pygame.Rect(x, y, 100, 75)
        self.image = pygame.image.load("special.png")  # 気弾の画像を読み込む
        self.image = self.image.convert()  # 画像を変換する

    def update(self):  # 描画位置を移動させる
        self.rect.move_ip(self.vx, 0)
