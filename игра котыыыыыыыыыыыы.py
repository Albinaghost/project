import pygame as pg
import gif_pygame as gp

from random import randint 
pg.init()
#time=pg.time.Clock()
shipina=900
Bbicota=800
B=200
sh=400
win = pg.display.set_mode((shipina,Bbicota))
pg.display.set_caption('игракотики')

zombi=pg.image.load('зомби.png')
zombi=pg.transform.scale(zombi,(sh/2,B))

zombi2=pg.image.load('RIPзомби.png')
zombi2=pg.transform.scale(zombi2,(sh,B))
zombak=[zombi,zombi2]

cactys=pg.image.load('кактус.png')
cactys=pg.transform.scale(cactys,(sh,B))


cactys2=pg.image.load('суперкактус.png')
cactys2=pg.transform.scale(cactys2,(sh,B))

cactys3=pg.image.load('RIPкактус.png')
cactys3=pg.transform.scale(cactys3,(sh,B))

koluchka=[cactys,cactys2,cactys3]

opyn2=pg.image.load('орун.png')
opyn2=pg.transform.scale(opyn2,(sh/2,B))

opyn3=pg.image.load('суперорун.png')
opyn3=pg.transform.scale(opyn3,(sh/2,B))
opyn4=pg.image.load('зомбиорун.png')
opyn4=pg.transform.scale(opyn4,(sh/2,B))
op=[opyn2,opyn3,opyn4]


tish=gp.load('be.gif')
gp.transform.scale(tish,(shipina,Bbicota/2))
m1=gp.load('монета.gif')
gp.transform.scale(m1,(sh/2,B))
m2=gp.load('монета.gif')
gp.transform.scale(m2,(sh/2,B))

f=pg.image.load('fon.jpg')
f=pg.transform.scale(f,(shipina,Bbicota))
w=pg.image.load('win.png')
w=pg.transform.scale(w,(500,200))
l=pg.image.load('lose.png')
l=pg.transform.scale(l,(500,200))
d=pg.image.load('draw.png')
d=pg.transform.scale(d,(500,200))
x=(shipina-sh)/2
y=  10
class carrta:
    def __init__(self,car,istori,p,x,y,color,wcar,hcar):#карта кота его история победа
        
        self.car=car
        self.istori=istori
        self.p=p
        self.h=pg.font.SysFont('comic Sans MS',25)
        self.na=self.h.render(p,False,(0,0,0))
        self.x=x
        self.y=y
        print(self.x,self.y)
        self.color=color
        self.wfon=wcar
        self.hfon=hcar
        self.fon=pg.Surface((self.wfon,self.hfon))
        self.fon.fill(self.color)
        self.xcar=self.x+(self.wfon-self.car.get_size()[0])/2
        #надпись 
        self.cklag=[]
        self.xna=self.x+(self.wfon-self.na.get_size()[0])/2
        
        self.yna=y+self.car.get_size()[1]+self.na.get_size()[1]-30
        self.yistorrui=self.yna+self.na.get_size()[1]
        for istorrui in self.istori.split('\n'):
    
            self.istorrui=self.h.render(istorrui,False,(0,0,0))
            self.xistorrui=self.x+(self.wfon-self.istorrui.get_size()[0])/2

            self.cklag.append([self.istorrui,self.xistorrui,self.yistorrui])
            self.yistorrui+=self.istorrui.get_size()[1]
    def draw(self,display):
        display.blit(self.fon,[self.x,self.y])
        display.blit(self.car,[self.xcar,self.y])
        display.blit(self.na,[self.xna,self.yna])
        for i in range(len(self.cklag)):
            display.blit(self.cklag[i][0],[self.cklag[i][1],self.cklag[i][2]])
    def update(self,x,y):
  
        if x>=self.x and x<self.x+self.wfon :
            if y>=self.y and y<self.y+self.hfon:
                return True
        return False
class cat ():
    def __init__(self,x,y,tip,kostym,u):#~
        self.x=x
        self.y=y
        self.tip=tip
        self.k=kostym.copy()
        self.rect=self.k[0].get_rect(topleft=[self.x,self.y])
        self.t=0
        self.life=1
        self.u=u
        self.paint=True
    def draw (self,display):
        if self.paint:
            display.blit(self.k[self.t],self.rect)
    def reset(self):
        self.t=0
        self.life=1
        self.paint=True
        self.rect=self.k[self.t].get_rect(topleft=[self.x,self.y])
    def update(self,moloko):
        if moloko==1 :
            if self.tip!='зомби':
                self.t=1
            
            if self.tip!='кактус':
                if self.u==1:
                    self.rect.x+=1
                else:
                    self.rect.x-=1
                
                    
        elif moloko ==2:
            
            if self.tip=='зомби':
                self.t=1
                self.life=-1
            if self.tip=='кактус':
                self.t=2

class butBa():
    def __init__(self,ugrok,pobot,f):#~@
        self.ugrok=ugrok
        for i in range(len(ugrok.k)):
            self.ugrok.k[i]=pg.transform.flip(self.ugrok.k[i],True,False)    
        self.pobot=pobot
        self.f=f
        self.t=pg.time.get_ticks()
        self.B=4000
        self.ww=None
        self.w=winer(ugrok,pobot)
        self.starttime=pg.time.get_ticks()
        print(self.w)
    def draw (self,chto):
        chto.blit(f,(0,0))
        self.pobot.draw(chto)
        self.ugrok.draw(chto)
        time=pg.time.get_ticks()
        if 1000<= time-self.starttime<=2000:
            
            tish.render(chto,(0,Bbicota-tish.get_size()[1]))#взрыв-tish
        
    def update(self):
        time=pg.time.get_ticks()
        if self.ugrok.rect.colliderect(self.pobot.rect):
            if self.w==1:
                if self.ugrok.tip=='орун' and self.pobot.tip=='кактус':
                   self.pobot.paint=False
                
                
                if self.pobot.tip=='орун'and self.ugrok.tip=='зомби':
                    self.pobot.t=2
                self.pobot.life=-1
            else:
                if self.ugrok.tip=='кактус' and self.pobot.tip=='орун':
                   self.ugrok.paint=False 
                if self.ugrok.tip=='орун'and self.pobot.tip=='зомби':
                    self.ugrok.t=2
                self.ugrok.life=-1
        if self.w==1:
            self.pobot.update(2)
            self.ww=self.ugrok.k[0]
            self.ugrok.update(1)
            
        elif self.w==2:
            self.ww=self.pobot.k[0]
            self.pobot.update(1)
                   
            self.ugrok.update(2)
        else:
            self.pobot.update(0)
            self.ww=self.pobot.k[0]
            self.ugrok.update(0)
        if time-self.t>=self.B:
            
            if self.ugrok.life==-1 or self.pobot.life==-1 or self.w==0:
                return 1
        for i in pg.event.get():
        
            if i.type == pg.QUIT:
                
                return 1
        
        return 0
class popeda ():
    def __init__(self,g,lw):
        self.lw=lw
        self.cotofeu=g
        
    def draw (self,xolst):#o_o
        xolst.fill(0)
        xolst.blit(self.cotofeu,[(shipina-self.cotofeu.get_size()[0])/2,Bbicota/2])
        if self.lw==1:
            xolst.blit(w,[(shipina-w.get_size()[0])/2,w.get_size()[1]])
        elif self.lw==2:
            xolst.blit(l,[(shipina-l.get_size()[0])/2,l.get_size()[1]])
        else:
            xolst.blit(d,[(shipina-d.get_size()[0])/2,d.get_size()[1]])
        m1.render(xolst,(70,Bbicota/2))
        m2.render(xolst,(600,Bbicota/2))
    def update(self):       
        for i in pg.event.get():
        
            if i.type == pg.QUIT:
                
                return 1
        
        return 0
import random  
      
tory=carrta(cactys,'рожден на венере\n из-за того что укололся\n об радиоктивный кактус\n стал котокактусом',
            'побеждает зомбикота',

            x,y,(70, 242, 202),
            400,380)#кактус
miki=carrta(zombi,'рожден на юпитере\n из-за того что землю\n захватил зомбивирус\n стал зомбикотом'
            ,'побеждает oруна',10,400,(70, 242, 202),350,400)#зомби
niki=carrta(opyn2,'рожден на марсе\n из-за того что в лаборотории\n перепутали формуру\n стал котоморуном',
            'побеждает котокактуса',
            450,400,(70, 242, 202),440,395)#орун.
k=cat(shipina-sh-50,Bbicota-B*1.5,'кактус',koluchka,0)
z=cat(shipina-sh/2-50,Bbicota-B*1.5,'зомби',zombak,0)
o=cat(shipina-sh/2-50,Bbicota-B*1.5,'орун',op,0)
number=random.randint(1,3)
if number==1:
    pobot=k
if number==2:
    pobot=z
if number==3:
    pobot=o
def winer(x,y):
    if x.tip=='зомби' and y.tip=='зомби':
        return 0
    
    elif x.tip=='зомби' and y.tip=='кактус':
        return 2
    elif x.tip=='зомби' and y.tip=='орун':
        return 1
    elif x.tip=='орун' and y.tip=='орун':
        return 0
    elif x.tip=='орун' and y.tip=='кактус':
        return 1
    elif x.tip=='орун' and y.tip=='зомби':
        return 2
    elif x.tip=='кактус' and y.tip=='кактус':
        return 0
    elif x.tip=='кактус' and y.tip=='зомби':
        return 1
    elif x.tip=='кактус' and y.tip=='орун':
        return 2
t=False
m=False
n=False
x=0
y=0
run = True
fight=None
while run:
    
    for i in pg.event.get():
        if i.type==pg.MOUSEBUTTONDOWN:
            x=pg.mouse.get_pos()[0]
            y=pg.mouse.get_pos()[1]#^.^
                                  
        if i.type == pg.QUIT:
            run = False
    win.fill(0)
    tory.draw(win)
    miki.draw(win)
    niki.draw(win)
    t=tory.update(x,y)   
    m=miki.update(x,y)
    n=niki.update(x,y)
    
    if t==True:
        print('вы выбрали котокактуса')
        
        pobot.reset()
        fight=butBa(cat(50,Bbicota-B*1.5,'кактус',koluchka,1),pobot,f)
        
    if m==True:
        print('вы выбрали котозомби')
        
        pobot.reset()
        
        fight=butBa(cat(50,Bbicota-B*1.5,'зомби',zombak,1),pobot,f)
    if n==True:
        print('вы выбрали котооруна')
        pobot.reset()
        
        fight=butBa(cat(50,Bbicota-B*1.5,'орун',op,1),pobot,f)
    if fight!=None:
        
        starttime=pg.time.get_ticks()
        
        g=0
        while g==0 :
            fight.draw(win)
            pg.display.update()
            if pg.time.get_ticks()-starttime<1000:
                continue
            g=fight.update()
            
        if fight.ww!=None:
            g=0
            panda=popeda(fight.ugrok.k[fight.ugrok.t],fight.w)
            while g==0 :
                
                g=panda.update()
                panda.draw(win)
                pg.display.update()
        number=random.randint(1,3)
        if number==1:
            pobot=k
        if number==2:
            pobot=z
        if number==3:
            pobot=o
        fight=None
        t=False
        m=False
        n=False
        x=0
        y=0
    pg.display.update()
pg.quit()

'''
кот1=кактус
кот2 =зомби
кот3 =орун

орун>кактус
зомби<кактуса
орун<зомби'''
