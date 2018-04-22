from math import cos,sin
from pyautocad import Autocad, APoint
from d_l import d_l
from d_c import d_c
from d_pointline import d_pointline

'''
螺栓
'''

def d_bolt_u(acad,x,y,e,k,dire,all=0):
    oc=1.5
    if dire=='u':
        [b1,u1]=d_pointline(acad,x-e/2,y,x-e/2,y+(k-oc))
        [b2,u2]=d_pointline(acad,x-e/4,y,x-e/4,y+(k-oc))
        [b3,u3]=d_pointline(acad,x+e/4,y,x+e/4,y+(k-oc))
        [b4,u4]=d_pointline(acad,x+e/2,y,x+e/2,y+(k-oc))
        [c1,c2]=d_pointline(acad,x-(e/2-oc),y+k,x+(e/2-oc),y+k)
        d_l(acad,b1,b4)
        d_l(acad,u1,u4)
        d_l(acad,c1,u1)
        d_l(acad,c2,u4)
    if dire=='d':
        [b1,u1]=d_pointline(acad,x-e/2,y,x-e/2,y-(k-oc))
        [b2,u2]=d_pointline(acad,x-e/4,y,x-e/4,y-(k-oc))
        [b3,u3]=d_pointline(acad,x+e/4,y,x+e/4,y-(k-oc))
        [b4,u4]=d_pointline(acad,x+e/2,y,x+e/2,y-(k-oc))
        [c1,c2]=d_pointline(acad,x-(e/2-oc),y-k,x+(e/2-oc),y-k)
        d_l(acad,b1,b4)
        d_l(acad,u1,u4)
        d_l(acad,c1,u1)
        d_l(acad,c2,u4)
    if all:
        pass

def d_bolt_bear_u(acad,xs,ys,dcaps,es,ks):
    dire=['u','d','u','d','u','d']
    for i in range(len(xs)):
        x=xs[i]
        e=es[i]
        k=ks[i]
        dcap=dcaps[i]
        d_bolt_u(acad,x-dcap/2,ys[2*i],e,k,dire[2*i])
        d_bolt_u(acad,x+dcap/2,ys[2*i],e,k,dire[2*i])
        d_bolt_u(acad,x-dcap/2,ys[2*i+1],e,k,dire[2*i+1])
        d_bolt_u(acad,x+dcap/2,ys[2*i+1],e,k,dire[2*i+1])

def d_bolt_f(acad,x,y,dcap,e,num):
    for i in range(num):
        d_bolt_f_solo(acad,x+cos((i/num+1/8)*(2*3.14159265))*dcap/2,y+sin((i/num+1/8)*(2*3.14159265))*dcap/2,e)

def d_bolt_f_solo(acad,x,y,e):
    h=3**0.5/4*e
    [b1,b2]=d_pointline(acad,x-e/2,y,x-e/4,y+h)
    [b3,b4]=d_pointline(acad,x+e/4,y+h,x+e/2,y)
    [b5,b6]=d_pointline(acad,x+e/4,y-h,x-e/4,y-h)
    d_l(acad,b2,b3)
    d_l(acad,b4,b5)
    d_l(acad,b6,b1)

    #辅助线
    [s1,s2]=d_pointline(acad,x-(e/2+2),y,x+(e/2+2),y)
    [s3,s4]=d_pointline(acad,x,y+h+2,x,y-(h+2))

def d_bolt_bear_f(acad,xs,y,dcaps,es):
    #螺钉数
    nums=[4,4,4]
    for i in range(len(xs)):
        x=xs[i]
        dcap=dcaps[i]
        e=es[i]
        num=nums[i]
        d_bolt_f(acad,x,y,dcap,e,num)

