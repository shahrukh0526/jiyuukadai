# pygameライブラリをインポート
import pygame
# timeモジュールインポート
import time
# randomモジュールインポート
import random

# 定数群(ゲームに関する)
FPS = 20     # Frame per Second 毎秒のフレーム数
BOX_WIDTH = 660        # ゲーム領域の幅
BOX_HEIGHT = 400       # ゲーム領域の高さ
PLAYER_X = 0  # プレイヤーのx方向の位置
PLAYER_VY = 20  # プレイヤーのy方向の速度
PLAYER_HP = 500  # プレイヤーのHP
KIDAN_VX = -30  # 気弾の速さ
KIDAN_POWER = 50  # 気弾のパワー
ENEMY_HP1 = 100  # 強さが1の敵のHP
ENEMY_HP2 = 200  # 強さが2の敵のHP
ENEMY_HP3 = 350  # 強さが3の敵のHP
ENEMY_VX1 = 10  # 強さが1の敵の速さ
ENEMY_VX2 = 15  # 強さが2の敵の速さ
ENEMY_VX3 = 16  # 強さが3の敵の速さ
ENEMY_POWER1 = 100  # 強さが1の敵のパワー
ENEMY_POWER2 = 200  # 強さが2の敵のパワー
ENEMY_POWER3 = 300  # 強さが3の敵のパワー
ENEMY_SCORE1 = 100  # 強さが1の敵を倒したときのスコア
ENEMY_SCORE2 = 300  # 強さが2の敵を倒したときのスコア
ENEMY_SCORE3 = 500  # 強さが3の敵を倒したときのスコア
SPECIAL_SCORE = 1000  # 特殊攻撃で敵を倒した時のスコア
ATTACK_COLOR = (255, 0, 0)  # 攻撃力UPのボタンの色
HITPOINT_COLOR = (0, 0, 255)  # 体力UPのボタンの色
SPECIALATTACK_COLOR = (255, 255, 0)  # 特殊攻撃のボタンの色
GAME_START = False

# プレイヤーのクラス


class Player(pygame.sprite.Sprite):  # Sprite継承
    def __init__(self, screen, x, y):  # コンストラクタ
        super().__init__()  # ←この一行
        self.screen = screen
        self.vy = PLAYER_VY
        self.hp = PLAYER_HP
        self.power = KIDAN_POWER
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
        self.vx = -80
        self.rect = pygame.Rect(x, y, 100, 75)
        self.image = pygame.image.load("special.png")  # 気弾の画像を読み込む
        self.image = self.image.convert()  # 画像を変換する

    def update(self):  # 描画位置を移動させる
        self.rect.move_ip(self.vx, 0)

# 攻撃力UPのクラス


class Attack:
    def __init__(self, screen):  # コンストラクタ
        self.screen = screen
        self.button = pygame.Rect(500, 350, 50, 50)
        self.font = pygame.font.SysFont('hgseikaishotaipro', 40)
        self.text = self.font.render("攻", True, (0, 0,  0))

    def draw(self):  # ボタン描画
        pygame.draw.rect(self.screen, (255, 0, 0), self.button)
        self.screen.blit(self.text, (505, 360))
# 体力UPのクラス


class HitPoint:
    def __init__(self, screen):  # コンストラクタ
        self.screen = screen
        self.button = pygame.Rect(552, 350, 50, 50)
        self.font = pygame.font.SysFont('hgseikaishotaipro', 40)
        self.text = self.font.render("体", True, (0, 0,  0))

    def draw(self):  # ボタン描画
        pygame.draw.rect(self.screen, (170, 202, 222), self.button)
        self.screen.blit(self.text, (557, 360))

# 特殊攻撃のクラス


class SpecialAttack:
    def __init__(self, screen):  # コンストラクタ
        self.screen = screen
        self.button = pygame.Rect(604, 350, 50, 50)
        self.font = pygame.font.SysFont('hgseikaishotaipro', 40)
        self.text = self.font.render("特", True, (0, 0,  0))

    def draw(self):  # ボタン描画
        pygame.draw.rect(self.screen, (255, 255, 0), self.button)
        self.screen.blit(self.text, (609, 360))


# スコアのクラス


class Score:
    def __init__(self, screen, score):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 25)
        self.text = self.font.render(
            'Your Score:'+str(score), True, (255, 255,  255))

    def draw(self):
        self.screen.blit(self.text, (10, 10))

# ゲームを制御するクラス


class Game:
    def __init__(self, w, h):  # コンストラクタ
        self.width = w
        self.height = h
        self.player = None
        self.enemys = []
        self.kidans = []
        self.specialkidan = None
        self.attack = None
        self.hitpoint = None
        self.special = None
        self.score = 0
        self.count = 0

    def set(self):   # 初期設定を一括して行う
        pygame.init()
        screen = pygame.display.set_mode((660, 400))  # pygameのディスプレイ生成
        self.screen = screen
        self.clock = pygame.time.Clock()     # 時計オブジェクト
        self.player = Player(screen, 560, 100)  # プレイヤーオブジェクト
        self.i = 0

    def kidan_s(self):  # 気弾を生成
        self.kidans.append(Kidan(self.screen, self.player.rect.x,
                                 self.player.rect.y))  # addメソッド

    def gen_enemys(self, strength):  # 敵を生成
        self.enemys.append(
            Enemy(self.screen, -10, random.randint(0, 300), strength))

    def animate(self):
        LOOP = True
        while LOOP:  # メインループ
            for event in pygame.event.get():
                # 「閉じる」ボタンを処理する
                if event.type == pygame.QUIT:
                    LOOP = False
            self.clock.tick(FPS)
            pressed_keys = pygame.key.get_pressed()  # キー情報を取得
            if pressed_keys[pygame.K_s]:    # sが押されたら
                self.kidan_s()
            if pressed_keys[pygame.K_UP]:    # 上が押されたら
                self.player.up()  # y 座標を小さく
            if pressed_keys[pygame.K_DOWN]:  # 下が押されたら
                self.player.down()     # y 座標を大きく
            if self.i % 20 == 0:
                self.gen_enemys(random.randint(1, 3))
            self.i += 1

            for enemy in self.enemys:
                if pygame.sprite.collide_rect(enemy, self.player):  # 衝突判定
                    if self.player.hp < enemy.power:
                        font = pygame.font.SysFont(None, 40)
                        text = font.render(
                            "GAME OVER", True, (255, 255,  255))
                        self.screen.blit(text, (230, BOX_HEIGHT/2-10))
                        pygame.display.flip()
                        time.sleep(2)
                        self.screen.fill((0, 0, 0))
                        LOOP = False
                    self.player.hp -= enemy.power
                    self.enemys.remove(enemy)
                for kidan in self.kidans:
                    if pygame.sprite.collide_rect(enemy, kidan):
                        self.kidans.remove(kidan)
                        if enemy.hp < self.player.power:
                            self.enemys.remove(enemy)
                            self.count += 1
                            self.score += enemy.score
                        enemy.hp -= self.player.power
                if self.specialkidan:
                    if pygame.sprite.collide_rect(enemy, self.specialkidan):  # 衝突判定
                        self.enemys.clear()
                        self.score += SPECIAL_SCORE
                        break
            if self.count >= 6:
                self.attack = Attack(self.screen)
            if self.count >= 6:
                self.hitpoint = HitPoint(self.screen)
            if self.count >= 12:
                self.special = SpecialAttack(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.attack.button.collidepoint(event.pos):
                        self.player.power += 30
                        self.count = 0
                        self.attack = None
                    if self.hitpoint.button.collidepoint(event.pos):
                        self.player.hp += 100
                        self.count = 0
                        self.hitpoint = None
                    if self.special.button.collidepoint(event.pos):
                        self.specialkidan = SpecialKidan(self.screen, self.player.rect.x,
                                                         self.player.rect.y)
                        self.count = 0
                        self.special = None

            Score(self.screen, self.score).draw()
            self.player.update()
            if self.specialkidan:
                self.specialkidan.update()
            self.screen.blit(self.player.image, self.player.rect)
            if self.specialkidan:
                self.screen.blit(self.specialkidan.image,
                                 self.specialkidan.rect)
            for kidan in self.kidans:
                kidan.update()
                self.screen.blit(kidan.image, kidan.rect)
            for enemy in self.enemys:
                enemy.update()
                self.screen.blit(enemy.image, enemy.rect)
            if self.attack:
                self.attack.draw()
            if self.hitpoint:
                self.hitpoint.draw()
            if self.special:
                self.special.draw()
            pygame.display.flip()
            self.screen.fill((0, 0, 0))


# ----------------------------------
# メインルーチン
game = Game(BOX_WIDTH, BOX_HEIGHT)
game.set()       # ゲームの初期設定
game.animate()   # アニメーション
pygame.quit()  # 画面を閉じる
