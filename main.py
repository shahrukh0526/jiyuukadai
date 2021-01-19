# pygameライブラリをインポート
import pygame
# Gameクラスをインポート
from game import Game


# メインプログラム
if __name__ == "__main__":
    game = Game()  # インスタンス生成
    game.set()       # ゲームの初期設定
    game.animate()   # アニメーション
    pygame.quit()  # 画面を閉じる
