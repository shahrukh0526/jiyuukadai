# pygameライブラリをインポート
import pygame
# timeモジュールインポート
import time
# randomモジュールインポート
import random

# 定数群(ゲームに関する)
FPS = 20     # Frame per Second 毎秒のフレーム数
BOX_WIDTH = 500        # ゲーム領域の幅
BOX_HEIGHT = 400       # ゲーム領域の高さ
PLAYER_X = 0  # プレイヤーのx方向の位置
PLAYER_VY = 20  # プレイヤーのy方向の速度
PLAYER_HP = 500  # プレイヤーのHP
KIDAN_VX = -10  # 気弾の速さ
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
ENEMY_SCORE1 = 100  # 強さが1の敵を倒したときのスコア
ENEMY_SCORE2 = 300  # 強さが2の敵を倒したときのスコア
ENEMY_SCORE3 = 500  # 強さが3の敵を倒したときのスコア
ATTACK_COLOR = (255, 0, 0)  # 攻撃力UPのボタンの色
HITPOINT_COLOR = (0, 0, 255)　  # 体力UPのボタンの色
SPECIALATTACK_COLOR = (255, 255, 0)  # 特殊攻撃のボタンの色

# プレイヤーのクラス


class Player(pygame.sprite.Sprite):  # Sprite継承
    def __init__(self, screen, x, y):  # コンストラクタ
        super().__init__()  # ←この一行
        self.screen = screen
        self.vy = PLAYER_VY
        self.hp = PLAYER_HP
        self.rect = pygame.Rect(x, y, 130, 150)
        self.image = pygame.image.load("player.png")  # プレイヤーの画像を読み込む
        self.image = self.image.convert()  # 画像を変換する
        self.d_y = 0

    def update(self):  # 描画位置を移動させる
        self.rect.move_ip(0, self.d_y)
        self.d_y = 0

    def up(self):  # プレイヤーに↑を押したときの処理
        y = self.rect.y-self.d_y
        if y >= 0:
            self.d_y -= self.vy

    def down(self):  # プレイヤーに↓を押したときの処理
        self.d_y += self.vy

# 敵のクラス


class Enemy(pygame.sprite.Sprite):  # Sprite継承
    def __init__(self, screen, x, y, strength):  # コンストラクタ
        super().__init__()  # ←この一行
        self.screen = screen
        if strength == 1:  # 強さが1の時
            self.vx = ENEMY_VX1
            self.hp = ENEMY_HP1
            self.power = ENEMY_POWER1
            self.score = ENEMY_SCORE1
            self.rect = pygame.Rect(x, y, 86, 86)
            self.image = pygame.image.load("zonbi.jpg")  # 強さ１の敵の画像を読み込む
            self.image = self.image.convert()  # 画像を変換する
        if strength == 2:  # 強さが2の時
            self.vx = ENEMY_VX2
            self.hp = ENEMY_HP2
            self.power = ENEMY_POWER2
            self.score = ENEMY_SCORE2
            self.rect = pygame.Rect(x, y, 86, 86)
            self.image = pygame.image.load("reaper.jpg")  # 強さ2の敵の画像を読み込む
            self.image = self.image.convert()  # 画像を変換する
        if strength == 3:  # 強さが3の時
            self.vx = ENEMY_VX3
            self.hp = ENEMY_HP3
            self.power = ENEMY_POWER3
            self.score = ENEMY_SCORE3
            self.rect = pygame.Rect(x, y, 86, 86)
            self.image = pygame.image.load("doragon.jpg")  # 強さ3の敵の画像を読み込む
            self.image = self.image.convert()  # 画像を変換する

    def update(self):  # 描画位置を移動させる
        self.rect.move_ip(self.vx, 0)

# 気弾のクラス


class Kidan(pygame.sprite.Sprite):  # Sprite継承
    def __init__(self, screen, x, y):  # コンストラクタ
        super().__init__()
        self.screen = screen
        self.vx = KIDAN_VX
        self.power = KIDAN_POWER
        self.rect = pygame.Rect(x, y, 100, 66)
        self.image = pygame.image.load("kidan.jpg")  # 気弾の画像を読み込む
        self.image = self.image.convert()  # 画像を変換する

    def update(self):  # 描画位置を移動させる
        self.rect.move_ip(self.vx, 0)

# 攻撃力UPのクラス


class Attack:
    def __init__(self, screen):  # コンストラクタ
        self.screen = screen
        self.button = pygame.Rect(500, 350, 50, 50)
        self.font = pygame.font.SysFont("hg明朝ehgp明朝ehgs明朝e", 12)
        self.text = self.font.render("攻", True, (0, 0,  0))

    def draw(self):  # ボタン描画
        pygame.draw.rect(self.screen, (255, 0, 0), button)
        self.screen.blit(text, (510, 360))
# 体力UPのクラス


class HitPoint:
    def __init__(self, screen):  # コンストラクタ
        self.screen = screen
        self.rect = pygame.Rect(552, 350, 50, 50)

# 特殊攻撃のクラス


class SpecialAttack:
    def __init__(self, screen):  # コンストラクタ
        self.screen = screen
        self.rect = pygame.Rect(604, 350, 50, 50)

# スコアのクラス


class Score:
    def __init__(self, screen, score):
        self.screen = screen
        self.font = pygame.font.SysFont("hg明朝ehgp明朝ehgs明朝e", 12)
        self.text = self.font.render(
            'Your Score:'+score, True, (255, 255,  255))

    def draw(self):
        self.screen.blit(self.text, (10, 10))

# ゲームを制御するクラス


class Game:
    def __init__(self, w, h):  # コンストラクタ
        self.width = w
        self.height = h
        self.player = None
        self.enemys = pygame.sprite.Group()  # Groupクラス
        self.kidans = pygame.sprite.Group()  # Groupクラス
        self.attack = None
        self.hitpoint = None
        self.special = None
        self.count = 0

    def set(self):   # 初期設定を一括して行う
        screen = pygame.display.set_mode((660, 400))  # pygameのディスプレイ生成
        self.screen = screen
        self.player = Player(screen, 500, 100)  # プレイヤーオブジェクト

    def kidan_s(self):  # 気弾を生成
        self.kidans.add(Kidan(self.screen, self.player.rect.x,
                              self.player.rect.y))  # addメソッド

    def gen_enemys(self, strength):  # 気弾を生成
        self.enemys.add(
            Enemy(self.screen, -10, random.randint(0, 300)), strength)  # addメソッド

    def animate(self):
        LOOP = True
        while LOOP:  # メインループ
            for event in pygame.event.get():
                # 「閉じる」ボタンを処理する
                if event.type == pygame.QUIT:
                    LOOP = False
            self.clock.tick(FPS)
            self.player.update()
            self.kidans.update()
            self.enemys.update()
            pressed_keys = pygame.key.get_pressed()  # キー情報を取得
            collided1 = pygame.sprite.spritecollideany(
                self.player, self.enemys)
            collided2 = pygame.sprite.spritecollideany(
                self.kidans, self.enemys)
            if pressed_keys[pygame.K_s]:    # sが押されたら
                self.kidan_s()
            if self.count <= 10:
                time.sleep(1)
                self.gen_enemys(1)
            if self.count <= 20:
                time.sleep(1)
                self.gen_enemys(2)
            if self.count > 20:
                time.sleep(1)
                self.gen_enemys(3)
            if collided1:  # 衝突したら
                self.enemys.remove()

            self.screen.blit(self.player.image, self.player.rect)
            self.kidans.draw(self.screen)
            self.enemys.draw(self.screen)

            if self.count > 50:  # 命中回数が50を超えたら
                self.target1.update()
                self.screen.blit(self.target1.image,
                                 self.target1.rect)  # 新しい標的表示
            if collided and self.count > 50:  # 命中回数が50を超え、標的と弾丸が衝突したら
                self.screen.blit(self.spear.image, (30, 100))  # 槍表示
            pygame.display.flip()
            self.screen.fill((0, 0, 0))


# ----------------------------------
# メインルーチン
box = Box(BOX_WIDTH, BOX_HEIGHT)
box.set()       # ゲームの初期設定
box.animate()   # アニメーション
pygame.quit()  # 画面を閉じる
