import pygame as pg
import random 
from tkinter import *
from tkinter import messagebox
Tk().wm_withdraw()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED =  (250, 117, 87)
val = []
for i in range(4):
  row = []
  for j in range(4):   
    row.append(0)
  val.append(row)
val[1][2]=2
def getRandPos():
    temp=random.randint(0,3)
    return temp

def restart():
    for i in range(4):
        for j in range(4):
            val[i][j]=0

def initSq():
    l=0
    i=0
    while i<=330:
        j=0
        m=0
        while j<=330:
            text = font.render(str(val[l][m]),True,BLACK)
            pg.draw.rect(screen, RED, [i, j, 100, 100])
            screen.blit(text, [i+40, j+40])
            j+=110
            m+=1
        i+=110
        l+=1


def gen2Or4():
    k=0
    for i in range(4):
        for j in range(4):
            if val[i][j]==2048:
                messagebox.showinfo("2048","Congrats!! Game Won")

            if val[i][j]==0:
                k=1
                break
        if k==1:
            break

    
    if k==1:
        i=getRandPos()
        j=getRandPos()
        while val[i][j] != 0:
            i=getRandPos()
            j=getRandPos()
        v=random.randint(1,10)
        if v<=8:
            v=2
        else:
            v=4
        val[i][j]=v
    elif k==0:
        messagebox.showinfo("2048","Game Over")
        restart()


pg.init()
font = pg.font.SysFont('Calibri', 25, True, False)


size = (700, 500)
screen = pg.display.set_mode(size)
 
pg.display.set_caption("2048")
 
done = False
 
clock = pg.time.Clock()
i=0
while not done:

    for event in pg.event.get():
        
        if event.type == pg.QUIT:
            done = True
        if event.type == pg.KEYDOWN:
            temp=val
            if event.key == pg.K_UP:
                for i in range(4):
                    for j in range(3):
                        if val[i][j]==0:
                            k=j
                            while k<4:
                                if val[i][k]!=0:
                                    val[i][j]=val[i][k] 
                                    val[i][k]=0
                                    break
                                k+=1

                for i in range(4):
                    for j in range(3):
                        if val[i][j]==val[i][j+1]:
                            val[i][j]+=val[i][j]
                            val[i][j+1]=0
                            k=j+1
                            while k<3:
                                val[i][k]=val[i][k+1]
                                
                                k+=1
                            val[i][3]=0
                            break
                            
            if event.key == pg.K_DOWN:
                i=3
                j=3
                for i in range(3,-1,-1):
                    for j in range(3,-1,-1):
                        # val[i][j]=val[i][j-1]
                        # val[i][j-1]=0
                        if val[i][j]==0:
                            k=j
                            while k>=0:
                                if val[i][k] !=0:
                                    val[i][j]=val[i][k]
                                    val[i][k]=0
                                    break 
                                k-=1
                for i in range(3,-1,-1):
                    for j in range(3,-1,-1):
                        if val[i][j]==val[i][j-1]:
                            val[i][j]+=val[i][j]
                            val[i][j-1]=0
                            k=j-1
                            while k>0:
                                val[i][k]=val[i][k-1]
                                k-=1

            if event.key==pg.K_RIGHT:
                for i in range(3,-1,-1):
                    for j in range(4):
                        if val[i][j]==0:
                            k=i-1
                            while k>=0:
                                if val[k][j] !=0:
                                    val[i][j]=val[k][j]
                                    val[k][j]=0
                                k-=1
                for i in range(3,-1,-1):
                    for j in range(4):
                        if val[i][j]==val[i-1][j]:
                            val[i][j]+=val[i][j]
                            k=i-1
                            while k>0:
                                val[k][j]=val[k-1][j]
                                k-=1
                            val[0][j]=0

            if event.key==pg.K_LEFT:
                for i in range(4):
                    for j in range(4):
                        if val[i][j]==0:
                            k=i+1
                            while k<4:
                                if val[k][j] !=0:
                                    val[i][j]=val[k][j]
                                    val[k][j]=0
                                k+=1

                for i in range(3):
                    for j in range(4):
                        if val[i][j]==val[i+1][j]:
                            val[i][j]+=val[i][j]
                            k=i+1
                            while k<3:
                                val[k][j]=val[k+1][j]
                                k+=1
                            val[3][i]=0                

            gen2Or4()
            


            
    initSq()
   
    


    pg.display.flip()
    screen.fill(WHITE)
 
    clock.tick(60)
 
pg.quit()