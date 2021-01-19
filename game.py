# pygameライブラリをインポート
import pygame
# timeモジュールインポート
import time
# randomモジュールインポート
import random
# Playerクラスインポート
from player import Player
# Kidanクラスインポート
from kidan import Kidan, SpecialKidan
# Enemyクラスインポート
from enemy import Enemy
# Playerクラスインポート
from player import Player
# オプションのクラスインポート
from option import Attack, HitPoint, SpecialAttack
# Scoreクラスインポート
from score import Score
# Hpクラスインポート
from hp import Hp

# 定数群(ゲームに関する)
FPS = 20     # Frame per Second 毎秒のフレーム数
BOX_WIDTH = 660        # ゲーム領域の幅
BOX_HEIGHT = 400       # ゲーム領域の高さ
PLAYER_X = 560  # プレイヤーのx方向の初期位置
SPECIAL_SCORE = 1000  # 特殊攻撃で敵を倒した時のスコア


# ゲームを制御するクラス


class Game:
    def __init__(self):  # コンストラクタ
        self.player = None
        self.enemys = []
        self.kidans = []
        self.specialkidan = None
        self.attack = None
        self.hitpoint = None
        self.special = None
        self.score = 0  # スコア
        self.count = 0  # 敵を倒した数

    def set(self):   # 初期設定を一括して行う
        pygame.init()
        screen = pygame.display.set_mode(
            (BOX_WIDTH, BOX_HEIGHT))  # pygameのディスプレイ生成
        self.screen = screen
        self.clock = pygame.time.Clock()     # 時計オブジェクト
        self.player = Player(screen, PLAYER_X, 100)  # プレイヤーオブジェクト
        self.i = 0

    def kidan_s(self):  # 気弾を生成
        self.kidans.append(Kidan(self.screen, self.player.rect.x,
                                 self.player.rect.y))  # addメソッド

    def gen_enemys(self, strength):  # 敵を生成
        self.enemys.append(
            Enemy(self.screen, -10, random.randint(0, 300), strength))

    def animate(self):
        font = pygame.font.SysFont(None, 40)
        text = font.render(
            "PLEASE PRESS SPACE TO START", True, (255, 255,  255))
        self.screen.blit(text, (110, BOX_HEIGHT/2-10))
        pygame.display.flip()
        start = None
        while not start:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    start = True
        pygame.display.flip()
        loop = True
        while loop:  # メインループ
            for event in pygame.event.get():
                # 「閉じる」ボタンを処理する
                if event.type == pygame.QUIT:
                    loop = False
            self.clock.tick(FPS)  # FPSのフレーム毎にClockオブジェクト更新
            pressed_keys = pygame.key.get_pressed()  # キー情報を取得
            if pressed_keys[pygame.K_s]:    # sが押されたら
                self.kidan_s()
            if pressed_keys[pygame.K_UP]:    # 上が押されたら
                self.player.up()  # y 座標を小さく
            if pressed_keys[pygame.K_DOWN]:  # 下が押されたら
                self.player.down()     # y 座標を大きく
            if self.i % 25 == 0:  # iが25の倍数の時
                self.gen_enemys(random.randint(1, 3))
            self.i += 1

            for enemy in self.enemys:  # 配列enemysのなかのすべてのenemy（敵）オブジェクトで
                if enemy.rect.x > self.player.rect.x+85:  # 敵がプレイヤーを通り過ぎたら
                    if self.player.hp < enemy.power:  # プレイヤーのhpが敵のパワーより低ければ
                        font = pygame.font.SysFont(None, 40)
                        text = font.render(
                            "GAME OVER", True, (255, 255,  255))
                        self.screen.blit(text, (230, BOX_HEIGHT/2-10))
                        pygame.display.flip()
                        time.sleep(2)
                        loop = False
                    self.player.hp -= enemy.power  # プレイヤーのhp減らす
                    try:
                        self.enemys.remove(enemy)  # 敵をenemysから削除
                    except:
                        continue
                if pygame.sprite.collide_rect(enemy, self.player):  # 敵とプレイヤーが衝突したら
                    if self.player.hp < enemy.power:  # プレイヤーのhpが敵のパワーより低ければ
                        font = pygame.font.SysFont(None, 40)
                        text = font.render(
                            "GAME OVER", True, (255, 255,  255))
                        self.screen.blit(text, (230, BOX_HEIGHT/2-10))
                        pygame.display.flip()
                        time.sleep(2)
                        loop = False
                    self.player.hp -= enemy.power  # プレイヤーのhp減らす
                    try:
                        self.enemys.remove(enemy)  # 敵をenemysから削除
                    except:
                        continue
                for kidan in self.kidans:  # 配列kidansのなかのすべてのkidan（気弾）オブジェクトで
                    if pygame.sprite.collide_rect(enemy, kidan):  # 敵と気弾が衝突したら
                        self.kidans.remove(kidan)
                        if enemy.hp < kidan.power:  # 敵のhpが気弾のパワーより低ければ
                            self.enemys.remove(enemy)  # 敵をenemysから削除
                            self.count += 1
                            self.score += enemy.score
                        enemy.hp -= kidan.power  # 敵のhp減らす
            if self.count >= 6:  # 敵を倒した数が６を超えていたら
                self.attack = Attack(self.screen)
            if self.count >= 6:  # 敵を倒した数が６を超えていたら
                self.hitpoint = HitPoint(self.screen)
            if self.count >= 12:  # 敵を倒した数が12を超えていたら
                self.special = SpecialAttack(self.screen)
            for event in pygame.event.get():  # イベント情報取得
                if event.type == pygame.MOUSEBUTTONDOWN:  # マウスボタンが押されていたら
                    if self.attack:
                            # 攻撃力UPのオブジェクトが押されたら
                        if self.attack.button.collidepoint(event.pos):
                            kidan.power += 30
                            self.count = 0
                            self.attack = None
                            self.hitpoint = None
                    if self.hitpoint:
                        # 体力UPのオブジェクトが押されたら
                        if self.hitpoint.button.collidepoint(event.pos):
                            self.player.hp += 300
                            self.count = 0
                            self.hitpoint = None
                            self.attack = None
                    if self.special:
                        # 特殊攻撃のオブジェクトが押されたら
                        if self.special.button.collidepoint(event.pos):
                            self.specialkidan = SpecialKidan(self.screen, self.player.rect.x,
                                                             self.player.rect.y)
                            self.count = 0
                            self.special = None
                            self.hitpoint = None
                            self.attack = None
            for enemy in self.enemys:  # 配列enemysのなかのすべてのenemy（敵）オブジェクトで
                if self.specialkidan:  # 特殊攻撃の気弾が生成されていたら
                    # 敵と特殊攻撃の気弾が衝突したら
                    if pygame.sprite.collide_rect(enemy, self.specialkidan):
                        self.enemys.clear()  # 敵をenemysからすべて削除
                        self.score += SPECIAL_SCORE
                        self.count += len(self.enemys)
                        break
            if not loop:  # loopがFalseの時
                break
            Score(self.screen, self.score).draw()  # スコアを描画
            Hp(self.screen, self.player.hp).draw()  # プレイヤーのHPを描画
            self.player.update()  # プレイヤーを更新
            if self.specialkidan:  # 特殊攻撃の気弾が生成されていたら
                self.specialkidan.update()
            self.screen.blit(self.player.image, self.player.rect)  # プレイヤーを表示
            if self.specialkidan:  # 特殊攻撃の気弾が生成されていたら
                self.screen.blit(self.specialkidan.image,
                                 self.specialkidan.rect)  # 特殊攻撃の気弾を描画
            for kidan in self.kidans:  # kidansの中のすべての気弾オブジェクトで
                kidan.update()
                self.screen.blit(kidan.image, kidan.rect)
            for enemy in self.enemys:  # enemysの中のすべての敵オブジェクトで
                enemy.update()
                self.screen.blit(enemy.image, enemy.rect)
            if self.attack:  # 攻撃力UPのオブジェクトが生成されていたら
                self.attack.draw()
            if self.hitpoint:  # 体力UPのオブジェクトが生成されていたら
                self.hitpoint.draw()
            if self.special:  # 特殊攻撃のオブジェクトが生成されていたら
                self.special.draw()
            pygame.display.flip()  # 画面更新
            self.screen.fill((0, 0, 0))  # 黒に塗りつぶす
