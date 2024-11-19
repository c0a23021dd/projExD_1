import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img=pg.image.load("fig/3.png")
    kk_img=pg.transform.flip(kk_img,True,False)
    tmr = 0
    a=300
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x=tmr%800

        screen.blit(bg_img, [-x, 0])  #screan　Surefaceに背景画像を張り付ける
        screen.blit(kk_img,[a,200])
        pg.display.update()
        tmr += 1   
        clock.tick(0)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()