# pygameライブラリをインポート
import pygame


# 定数群
PLAYER_VY = 20  # プレイヤーのy方向の速度
PLAYER_HP = 800  # プレイヤーのHP


# プレイヤーのクラス


class Player(pygame.sprite.Sprite):  # Sprite継承
    def __init__(self, screen, x, y):  # コンストラクタ
        super().__init__()  # ←この一行
        self.screen = screen
        self.vy = PLAYER_VY
        self.hp = PLAYER_HP
        self.rect = pygame.Rect(x, y, 85, 98)
        self.image = pygame.image.load("player.png")  # プレイヤーの画像を読み込む
        self.image = self.image.convert()  # 画像を変換する
        self.d_y = 0

    def update(self):  # 描画位置を移動させる
        self.rect.move_ip(0, self.d_y)
        self.d_y = 0

    def up(self):  # プレイヤーに↑を押したときの処理
        y = self.rect.y
        if y >= 20:
            self.d_y -= self.vy

    def down(self):  # プレイヤーに↓を押したときの処理
        y = self.rect.y+98
        if y <= 380:
            self.d_y += self.vy
