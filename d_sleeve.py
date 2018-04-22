from math import cos
from pyautocad import Autocad, APoint
from d_l import d_l

'''
垫圈
'''
def d_sleeve(acad,x,up,down,d,Dg,Db,flag):
    if flag=='d':
        l1=APoint(x-d/2,up)
        l2=APoint(x-Dg/2,up)
        l3=APoint(x-Dg/2,up*2/3+down/3)
        l4=APoint(x-Db/2,up*2/3+down/3)
        l5=APoint(x-Db/2,down)
        d_l(acad,l1,l2)
        d_l(acad,l2,l3)
        d_l(acad,l3,l4)
        d_l(acad,l4,l5)

        r1=APoint(x+d/2,up)
        r2=APoint(x+Dg/2,up)
        r3=APoint(x+Dg/2,up*2/3+down/3)
        r4=APoint(x+Db/2,up*2/3+down/3)
        r5=APoint(x+Db/2,down)
        d_l(acad,r1,r2)
        d_l(acad,r2,r3)
        d_l(acad,r3,r4)
        d_l(acad,r4,r5)

    elif flag=='u':

        l1=APoint(x-d/2,down)
        l2=APoint(x-Dg/2,down)
        l3=APoint(x-Dg/2,down*2/3+up/3)
        l4=APoint(x-Db/2,down*2/3+up/3)
        l5=APoint(x-Db/2,up)
        d_l(acad,l1,l2)
        d_l(acad,l2,l3)
        d_l(acad,l3,l4)
        d_l(acad,l4,l5)

        r1=APoint(x+d/2,down)
        r2=APoint(x+Dg/2,down)
        r3=APoint(x+Dg/2,down*2/3+up/3)
        r4=APoint(x+Db/2,down*2/3+up/3)
        r5=APoint(x+Db/2,up)
        d_l(acad,r1,r2)
        d_l(acad,r2,r3)
        d_l(acad,r3,r4)
        d_l(acad,r4,r5)
