# pygameライブラリをインポート
import pygame

FPS = 20     # Frame per Second 毎秒のフレーム数

# 定数群
BOX_WIDTH = 500        # ゲーム領域の幅
BOX_HEIGHT = 400       # ゲーム領域の高さ
PLAYER_X = 0  # プレイヤーのx方向の位置
PLAYER_VY = 20  # プレイヤーのy方向の速度
PLAYER_HP = 500  # プレイヤーのHP
KIDAN_VX = 10  # 気弾の速さ
KIDAN_POWER = 50  # 気弾のパワー
ENEMY_HP1 = 100  # 強さが1の敵のHP
ENEMY_HP2 = 200  # 強さが2の敵のHP
ENEMY_HP3 = 500  # 強さが3の敵のHP
ENEMY_VX1 = 20  # 強さが1の敵の速さ
ENEMY_VX2 = 30  # 強さが2の敵の速さ
ENEMY_VX3 = 40  # 強さが3の敵の速さ
ENEMY_POWER1 = 100  # 強さが1の敵のパワー
ENEMY_POWER2 = 200  # 強さが2の敵のパワー
ENEMY_POWER3 = 300  # 強さが3の敵のパワー
SCORE1 = 100  # 強さが1の敵を倒したときのスコア
SCORE2 = 300  # 強さが2の敵を倒したときのスコア
SCORE3 = 500  # 強さが3の敵を倒したときのスコア

# プレイヤーのクラス


class Player(pygame.sprite.Sprite):  # Sprite継承
    def __init__(self, screen, x, y, vy):  # コンストラクタ
        super().__init__()  # ←この一行
        self.screen = screen
        self.vy = PLAYER_VY
        self.rect = pygame.Rect(x, y, 130, 150)
        self.image = pygame.image.load("player.png")  # プレイヤーの画像を読み込む
        self.image = self.image.convert()  # 画像を変換する
        self.d_y = 0

# 敵のクラス


class Enemy(pygame.sprite.Sprite):  # Sprite継承
    def __init__(self, screen, x, y, vx, strength):  # コンストラクタ
        super().__init__()  # ←この一行
        self.screen = screen
        if strength == 1:
            self.vx = ENEMY_VX1
            self.rect = pygame.Rect(x, y, 86, 86)
            self.image = pygame.image.load("zonbi.jpg")  # 強さ１の敵の画像を読み込む
            self.image = self.image.convert()  # 画像を変換する
        if strength == 2:
            self.vx = ENEMY_VX2
            self.rect = pygame.Rect(x, y, 86, 86)
            self.image = pygame.image.load("zonbi.jpg")  # 戦車の画像を読み込む
            self.image = self.image.convert()  # 画像を変換する
        if strength == 1:
            self.vx = ENEMY_VX1
            self.rect = pygame.Rect(x, y, 86, 86)
            self.image = pygame.image.load("zonbi.jpg")  # 戦車の画像を読み込む
            self.image = self.image.convert()  # 画像を変換する

# 気弾のクラス


class Kidan(pygame.sprite.Sprite):  # Sprite継承
    def __init__(self, screen, x, y, vx):  # コンストラクタ
        super().__init__()
        self.screen = screen
        self.vx = KIDAN_VX
        self.rect = pygame.Rect(x, y, 45, 26)
        self.image = pygame.image.load("bullet1.jpg")  # 弾丸の画像を読み込む
        self.image = self.image.convert()  # 画像を変換する

    def update(self):  # 描画位置を移動させる
        self.rect.move_ip(self.vx, 0)

# 攻撃力UPのクラス


class Attack:
    pass

# 体力UPのクラス


class HitPoint:
    pass

# 特殊攻撃のクラス


class SpecialAttack:
    pass

# ゲーム中心のクラス


class Game:
    def __init__(self, w, h):  # コンストラクタ
        self.width = w
        self.height = h
        self.player = None
        self.enemy = None
        self.kidans = pygame.sprite.Group()  # Groupクラス
