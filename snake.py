import time
from keyboard import read_key
from os import system
from threading import Thread as thrd
from random import randint
w=40
h=20
swt=[True]
fruit='$'
tx='#'
grid=[]
for i in range(h):
    grid.append([])
    for j in range(w):
        if((i==0 or i==h-1) and (j==0 or j==w-1)):
            temp='+'
        elif(j==0 or j==w-1):
            temp='|'
        elif(i==0 or i==h-1):
            temp='-'
        else:
            temp=' '
        grid[i].append(temp)
       
       
def creategrid(y,x,k=0):
    for i in range(y):
        arr.append([])
        for j in range(x):
            arr[i].append(k)
    return arr
       
def printgrid():
    global grid,w,h
    for y in range(h):
        arr=[]
        for x in range(w):
            arr.append(str(grid[y][x]))
        print(''.join(arr))
        

def isbounded(y,x):
    global w,h
    if(y>0 and x>0 and (y<h-1) and (x<w-1)):
        return True
    else:
        return False
        
class snake:
    def __init__(self):
        global w,h,fruit,tx,grid
        temp=w//4
        t2=h//2
        self.lastlength=3
        self.queue=[(t2,temp-3),(t2,temp-2),(t2,temp-1),(t2,temp)]
        for y,x in self.queue:
            grid[y][x]=tx
        self.w=w
        self.h=h
        self.length=4
        self.dir=0
        self.fruit=fruit
        #self.gd=creategrid(h,w,[0,0])
        ##
        
    
    
    def changedir(self,c):
        if(type(c)==type(1)):
            self.dir=c
        else:
            self.dir=['r','u','l''d'].index(c)
    def food(self):
        if(len(self.queue)>self.lastlength):
            while(True):
                x=randint(1,w-2)
                y=randint(1,h-2)
                if((y,x) not in self.queue):
                    break
            grid[y][x]=self.fruit
            self.lastlength=len(self.queue)
        
    def move(self):
        y,x=self.queue[-1]
        dx=[1,0,-1,0]
        dy=[0,-1,0,1]
        xx=x+dx[self.dir]
        yy=y+dy[self.dir]
        
        if(isbounded(yy,xx) and ((yy,xx) not in self.queue)):
            if(grid[yy][xx]==fruit):
                self.queue.append([yy,xx])
                self.length+=1
                grid[yy][xx]=tx
            else:
                self.queue.append([yy,xx])
                grid[yy][xx]=tx
                yp,xp=self.queue.pop(0)
                grid[yp][xp]=' '
                
                
        else:
            swt[0]=False
            exit()
    
class game:
    def __init__(self):
        self.moveque=['right']
    def fun(self,arr,switch):
        while(switch[0]):
            arr.append(read_key())
    def fundest(self,arr,switch):
        while(switch[0]):
            if(len(arr)>4):
                arr.pop(0)
            else:
                time.sleep(1)
    def launch(self):
        keyboardThread=thrd(target=self.fun,args=(self.moveque,swt))
        dest=thrd(target=self.fundest,args=(self.moveque,swt))
        dest.start()
        s=snake()
        s.food()
        keyboardThread.start()
        
        while(True):
            system('CLS')
            printgrid()
            arr=['right','up','left','down']

            lastdir=self.moveque[-1]
            if(lastdir in arr):
                temp=arr.index(lastdir)
                s.changedir(temp)
            s.move()
            s.food()
            time.sleep(0.05)
g=game()
g.launch()