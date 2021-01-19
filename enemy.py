# pygameライブラリをインポート
import pygame

# 定数群
ENEMY_HP1 = 100  # 強さが1の敵のHP
ENEMY_HP2 = 200  # 強さが2の敵のHP
ENEMY_HP3 = 350  # 強さが3の敵のHP
ENEMY_VX1 = 10  # 強さが1の敵の速さ
ENEMY_VX2 = 13  # 強さが2の敵の速さ
ENEMY_VX3 = 15  # 強さが3の敵の速さ
ENEMY_POWER1 = 100  # 強さが1の敵のパワー
ENEMY_POWER2 = 200  # 強さが2の敵のパワー
ENEMY_POWER3 = 300  # 強さが3の敵のパワー
ENEMY_SCORE1 = 100  # 強さが1の敵を倒したときのスコア
ENEMY_SCORE2 = 300  # 強さが2の敵を倒したときのスコア
ENEMY_SCORE3 = 500  # 強さが3の敵を倒したときのスコア


# 敵のクラス


class Enemy(pygame.sprite.Sprite):  # Sprite継承
    def __init__(self, screen, x, y, strength):  # コンストラクタ
        super().__init__()  # ←この一行
        self.screen = screen
        if strength == 1:  # 強さが1の時
            self.x = x
            self.vx = ENEMY_VX1
            self.hp = ENEMY_HP1
            self.power = ENEMY_POWER1
            self.score = ENEMY_SCORE1
            self.rect = pygame.Rect(x, y, 86, 86)
            self.image = pygame.image.load("zonbi.jpg")  # 強さ１の敵の画像を読み込む
            self.image = self.image.convert()  # 画像を変換する
        if strength == 2:  # 強さが2の時
            self.x = x
            self.vx = ENEMY_VX2
            self.hp = ENEMY_HP2
            self.power = ENEMY_POWER2
            self.score = ENEMY_SCORE2
            self.rect = pygame.Rect(x, y, 86, 86)
            self.image = pygame.image.load("reaper.jpg")  # 強さ2の敵の画像を読み込む
            self.image = self.image.convert()  # 画像を変換する
        if strength == 3:  # 強さが3の時
            self.x = x
            self.vx = ENEMY_VX3
            self.hp = ENEMY_HP3
            self.power = ENEMY_POWER3
            self.score = ENEMY_SCORE3
            self.rect = pygame.Rect(x, y, 86, 86)
            self.image = pygame.image.load("doragon.jpg")  # 強さ3の敵の画像を読み込む
            self.image = self.image.convert()  # 画像を変換する

    def update(self):  # 描画位置を移動させる
        self.rect.move_ip(self.vx, 0)
