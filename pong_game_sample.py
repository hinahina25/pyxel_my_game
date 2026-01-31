import pyxel
import random

# 画面サイズ
W = 160
H = 120

# プレイヤー（パドル）の位置と大きさ
pad_x = 70
pad_y = 110
pad_w = 40
pad_h = 5

# ボールの位置と速さ
ball_x = 80
ball_y = 60
vx = 1
vy = 1



pad_count=0
ball_color=10
pad_color=7
score=0
def update():
    global pad_x, ball_x, ball_y, vx, vy,pad_count,ball_color,pad_color,score

    # --- パドルの操作 ---
    if pyxel.btn(pyxel.KEY_LEFT):
        pad_x -= 8
    if pyxel.btn(pyxel.KEY_RIGHT):
        pad_x += 8

    # --- ボールの移動 ---
    if vx >0:
        ball_x += vx +(pad_count//3)
    else:
        ball_x += vx -(pad_count//3)
    if vy >0:
        ball_y += vy +(pad_count//3)
    else:
        ball_y += vy -(pad_count//3)


    # --- 壁との反射 ---
    if ball_x < 0 or ball_x > W - 3:
        vx = -vx
        ball_color=random.randint(1,15)
    if ball_y < 0:
        vy = -vy
        ball_color=random.randint(1,15)
    # --- パドルとの当たり判定 ---    
    if ((pad_x <= ball_x and ball_x <= pad_x + pad_w) and
        (pad_y - 3 <= ball_y and ball_y <= pad_y)):
        vy = -vy
        pad_count+=1
        ball_color=random.randint(1,15)
        pad_color=random.randint(1,15)
        score+=2

    # --- 下に落ちたらリセット ---
    if ball_y > H:
        # 初期位置にもどす
        ball_x = 80
        ball_y = 60
        vx = 1
        vy = 1
        pad_count=0


def draw():
    pyxel.cls(0)

    # パドル
    pyxel.rect(pad_x, pad_y, pad_w, pad_h, pad_color)

    # ボール
    pyxel.rect(ball_x, ball_y, 3, 3, ball_color)
    #スコア
    pyxel.text(65, 10, f"SCORE:{score}", 3)


pyxel.init(W, H, title="PONG Sample")
pyxel.run(update, draw)