import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """宇宙船を管理するクラス"""

    def __init__(self, ai_game):
        """宇宙船を初期化し、開始時の位置を設定する"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # 宇宙船の画像を読み込み、サイズを取得する
        self.image = pygame.image.load('images/spaceship.jpg')
        # 右に向こうのように90度に回転する
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()

        """"# 新しい宇宙船を画面下部の中央に配置する"""
        # self.rect.midbottom = self.screen_rect.midbottom

        # 新しい宇宙船を画面左部の中央に配置する
        self.rect.midleft = self.screen_rect.midleft

        # 宇宙船の水平位置の浮動小数点数を格納する
        # self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # 移動フラグ
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """左右の移動フラグによって宇宙船の位置を更新する"""
        # 宇宙船のxの値を更新する(rectではない)
        # if self.moving_right and self.rect.right < self.screen_rect.right:
        # self.x += self.settings.ship_speed
        # if self.moving_left and self.rect.left > 0:
        # self.x -= self.settings.ship_speed

        # self.xからrectオブジェクトの位置を更新する
        # self.rect.x = self.x

        """上下の移動フラグによって宇宙船の位置を更新する"""
        # 宇宙船のyの値を更新する(rectではない)
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # self.yからrectオブジェクトの位置を更新する
        self.rect.y = self.y

    def blitme(self):
        # 宇宙船の現在位置を描画する
        self.screen.blit(self.image, self.rect)

    def init_ship_pos(self):
        """宇宙船を画面の左に配置する"""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
