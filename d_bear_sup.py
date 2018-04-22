from pyautocad import Autocad, APoint
from d_l import d_l
from d_c import d_c
from d_pointline import d_pointline

def d_bear_sup(acad,x,y,c1,c2,L,d,D2,d2,a,b,delta,updown):

    if updown=='d':
        [l1,l2]=d_pointline(acad,x-d/2,y,x-d/2,y-L)
        [r1,r2]=d_pointline(acad,x+d/2,y,x+d/2,y-L)
        [l3,l4]=d_pointline(acad,x-D2/2,y-c1-c2-delta,x-D2/2,y-L)
        [r3,r4]=d_pointline(acad,x+D2/2,y-c1-c2-delta,x+D2/2,y-L)
        d_l(acad,l1,r1)
        d_l(acad,l4,r4)
        Cl=APoint(x-D2/2,y-c1-delta)
        d_c(acad,Cl,d2/2,1)
        Cr=APoint(x+D2/2,y-c1-delta)
        d_c(acad,Cr,d2/2,1)
        ol1=APoint(x-d/2,y-a)
        [ol2,ol3]=d_pointline(acad,x-d/2,y-(c1+3+delta),x-(d/2+b),y-(c1+3+delta))
        ol4=APoint(x-(d/2+b),y-(a+b))
        d_l(acad,ol3,ol4)
        or1=APoint(x+d/2,y-a)
        [or2,or3]=d_pointline(acad,x+d/2,y-(c1+3+delta),x+(d/2+b),y-(c1+3+delta))
        or4=APoint(x+(d/2+b),y-(a+b))
        d_l(acad,or3,or4)
    if updown=='u':
        [l1,l2]=d_pointline(acad,x-d/2,y,x-d/2,y+L)
        [r1,r2]=d_pointline(acad,x+d/2,y,x+d/2,y+L)
        [l3,l4]=d_pointline(acad,x-D2/2,y+c1+c2+delta,x-D2/2,y+L)
        [r3,r4]=d_pointline(acad,x+D2/2,y+c1+c2+delta,x+D2/2,y+L)
        d_l(acad,l1,r1)
        d_l(acad,l4,r4)
        Cl=APoint(x-D2/2,y+c1+delta)
        d_c(acad,Cl,d2/2,1)
        Cr=APoint(x+D2/2,y+c1+delta)
        d_c(acad,Cr,d2/2,1)
        ol1=APoint(x-d/2,y+a)
        [ol2,ol3]=d_pointline(acad,x-d/2,y+(c1+3+delta),x-(d/2+b),y+(c1+3+delta))
        ol4=APoint(x-(d/2+b),y+(a+b))
        d_l(acad,ol3,ol4)
        or1=APoint(x+d/2,y+a)
        [or2,or3]=d_pointline(acad,x+d/2,y+(c1+3+delta),x+(d/2+b),y+(c1+3+delta))
        or4=APoint(x+(d/2+b),y+(a+b))
        d_l(acad,or3,or4)
    return l1,r1,l3,r3,ol1,or1,ol4,or4
