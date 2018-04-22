from math import cos
from pyautocad import Autocad, APoint
from d_l import d_l
from d_c import d_c
from d_pointline import d_pointline

'''
轴承端盖
'''
def cap_u(acad,x,y,H,d,D,d3,b,h,updown,oc):
    d1=d+3
    e=1.2*d3
    d0=d3+1
    D0=D+2.5*d3
    D2=D0+2.5*d3
    D4=D-10

    if updown=='u':

        [fl1,fr1]=d_pointline(acad,x-D2/2,y+H,x+D2/2,y+H)
        [fl2,fl3]=d_pointline(acad,x-D0/2-d0/2,y+H,x-D0/2-d0/2,y+H-e)
        [fr2,fr3]=d_pointline(acad,x+D0/2+d0/2,y+H,x+D0/2+d0/2,y+H-e)
        [fl4,fl5]=d_pointline(acad,x-D0/2+d0/2,y+H,x-D0/2+d0/2,y+H-e)
        [fr4,fr5]=d_pointline(acad,x+D0/2-d0/2,y+H,x+D0/2-d0/2,y+H-e)
        [fl6,fl7]=d_pointline(acad,x-D/2+1,y+H-e,x-D/2+1,y+H-e-1)
        [fr6,fr7]=d_pointline(acad,x+D/2-1,y+H-e,x+D/2-1,y+H-e-1)
        fl8=APoint(x-D2/2,y+H-e)
        fr8=APoint(x+D2/2,y+H-e)
        [fl9,fl10]=d_pointline(acad,x-D/2,y+h,x-D/2,y+H-e-1)
        [fr9,fr10]=d_pointline(acad,x+D/2,y+h,x+D/2,y+H-e-1)
        [fl11,fl12]=d_pointline(acad,x-(D*D-b*b)**0.5/2,y+h,x-(D*D-b*b)**0.5/2,y)
        [fr11,fr12]=d_pointline(acad,x+(D*D-b*b)**0.5/2,y+h,x+(D*D-b*b)**0.5/2,y)
        [fl13,fl14]=d_pointline(acad,x-(D4*D4-b*b)**0.5/2+h/10,y+h,x-(D4*D4-b*b)**0.5/2,y)
        [fr13,fr14]=d_pointline(acad,x+(D4*D4-b*b)**0.5/2-h/10,y+h,x+(D4*D4-b*b)**0.5/2,y)
        [fl15,fl16]=d_pointline(acad,x-D4/2+h/10,y+h,x-D4/2+H/10,y+H/2)
        [fr15,fr16]=d_pointline(acad,x+D4/2-h/10,y+h,x+D4/2-H/10,y+H/2)
        [fl17,fl18]=d_pointline(acad,x-b/2,y,x-b/2,y+h)
        [fr17,fr18]=d_pointline(acad,x+b/2,y,x+b/2,y+h)

        d_l(acad,fl1,fl8)
        d_l(acad,fr1,fr8)
        d_l(acad,fl6,fl8)
        d_l(acad,fr6,fr8)
        d_l(acad,fl10,fl7)
        d_l(acad,fr10,fr7)
        d_l(acad,fl12,fr12)
        d_l(acad,fl9,fl13)
        d_l(acad,fr9,fr13)
        d_l(acad,fl16,fr16)
        d_l(acad,fl18,fr18)
        #辅助线
        [fl6,fl7]=d_pointline(acad,x-D0/2,y+H+2,x-D0/2,y+H-e-2)
        [fr6,fr7]=d_pointline(acad,x+D0/2,y+H+2,x+D0/2,y+H-e-2)

        ol1=APoint(x-D/2,y+H)
        or1=APoint(x+D/2,y+H)
        [ol2,or2]=d_pointline(acad,x-(D/2-1),y+H-1,x+(D/2-1),y+H-1)
        d_l(acad,ol1,ol2)
        d_l(acad,or1,or2)
        if oc=='o':
            ol3=APoint(x-d1/2,y+H-1)
            or3=APoint(x+d1/2,y+H-1)
            [ol4,or4]=d_pointline(acad,x-d1/2,y+7*H/8,x+d1/2,y+7*H/8)
            [ol5,or5]=d_pointline(acad,x-d1/2-3,y+13*H/16,x+d1/2+3,y+13*H/16)
            [ol6,or6]=d_pointline(acad,x-d1/2-3,y+11*H/16,x+d1/2+3,y+11*H/16)
            [ol7,or7]=d_pointline(acad,x-d1/2,y+5*H/8,x+d1/2,y+5*H/8)
            ol8=APoint(x-d1/2,y+H/2)
            or8=APoint(x+d1/2,y+H/2)
            d_l(acad,ol3,ol4)
            d_l(acad,or3,or4)
            d_l(acad,ol4,ol5)
            d_l(acad,or4,or5)
            d_l(acad,ol5,ol6)
            d_l(acad,or5,or6)
            d_l(acad,ol6,ol7)
            d_l(acad,or6,or7)
            d_l(acad,ol7,ol8)
            d_l(acad,or7,or8)

    if updown=='d':

        [fl1,fr1]=d_pointline(acad,x-D2/2,y-H,x+D2/2,y-H)
        [fl2,fl3]=d_pointline(acad,x-D0/2-d0/2,y-H,x-D0/2-d0/2,y-H+e)
        [fr2,fr3]=d_pointline(acad,x+D0/2+d0/2,y-H,x+D0/2+d0/2,y-H+e)
        [fl4,fl5]=d_pointline(acad,x-D0/2+d0/2,y-H,x-D0/2+d0/2,y-H+e)
        [fr4,fr5]=d_pointline(acad,x+D0/2-d0/2,y-H,x+D0/2-d0/2,y-H+e)
        [fl6,fl7]=d_pointline(acad,x-D/2+1,y-H+e,x-D/2+1,y-H+e+1)
        [fr6,fr7]=d_pointline(acad,x+D/2-1,y-H+e,x+D/2-1,y-H+e+1)
        fl8=APoint(x-D2/2,y-H+e)
        fr8=APoint(x+D2/2,y-H+e)
        [fl9,fl10]=d_pointline(acad,x-D/2,y-h,x-D/2,y-H+e+1)
        [fr9,fr10]=d_pointline(acad,x+D/2,y-h,x+D/2,y-H+e+1)
        [fl11,fl12]=d_pointline(acad,x-(D*D-b*b)**0.5/2,y-h,x-(D*D-b*b)**0.5/2,y)
        [fr11,fr12]=d_pointline(acad,x+(D*D-b*b)**0.5/2,y-h,x+(D*D-b*b)**0.5/2,y)
        [fl13,fl14]=d_pointline(acad,x-(D4*D4-b*b)**0.5/2+h/10,y-h,x-(D4*D4-b*b)**0.5/2,y)
        [fr13,fr14]=d_pointline(acad,x+(D4*D4-b*b)**0.5/2-h/10,y-h,x+(D4*D4-b*b)**0.5/2,y)
        [fl15,fl16]=d_pointline(acad,x-D4/2+h/10,y-h,x-D4/2+H/10,y-H/2)
        [fr15,fr16]=d_pointline(acad,x+D4/2-h/10,y-h,x+D4/2-H/10,y-H/2)
        [fl17,fl18]=d_pointline(acad,x-b/2,y,x-b/2,y-h)
        [fr17,fr18]=d_pointline(acad,x+b/2,y,x+b/2,y-h)

        d_l(acad,fl1,fl8)
        d_l(acad,fr1,fr8)
        d_l(acad,fl6,fl8)
        d_l(acad,fr6,fr8)
        d_l(acad,fl10,fl7)
        d_l(acad,fr10,fr7)
        d_l(acad,fl12,fr12)
        d_l(acad,fl9,fl13)
        d_l(acad,fr9,fr13)
        d_l(acad,fl16,fr16)
        d_l(acad,fl18,fr18)
        #辅助线
        [fl6,fl7]=d_pointline(acad,x-D0/2,y-H-2,x-D0/2,y-(H-e-2))
        [fr6,fr7]=d_pointline(acad,x+D0/2,y-H-2,x+D0/2,y-(H-e-2))

        ol1=APoint(x-D/2,y-H)
        or1=APoint(x+D/2,y-H)
        [ol2,or2]=d_pointline(acad,x-(D/2-1),y-(H-1),x+(D/2-1),y-(H-1))
        d_l(acad,ol1,ol2)
        d_l(acad,or1,or2)
        if oc=='o':
            ol3=APoint(x-d1/2,y-(H-1))
            or3=APoint(x+d1/2,y-(H-1))
            [ol4,or4]=d_pointline(acad,x-d1/2,y-7*H/8,x+d1/2,y-7*H/8)
            [ol5,or5]=d_pointline(acad,x-d1/2-3,y-13*H/16,x+d1/2+3,y-13*H/16)
            [ol6,or6]=d_pointline(acad,x-d1/2-3,y-11*H/16,x+d1/2+3,y-11*H/16)
            [ol7,or7]=d_pointline(acad,x-d1/2,y-5*H/8,x+d1/2,y-5*H/8)
            ol8=APoint(x-d1/2,y-H/2)
            or8=APoint(x+d1/2,y-H/2)
            d_l(acad,ol3,ol4)
            d_l(acad,or3,or4)
            d_l(acad,ol4,ol5)
            d_l(acad,or4,or5)
            d_l(acad,ol5,ol6)
            d_l(acad,or5,or6)
            d_l(acad,ol6,ol7)
            d_l(acad,or6,or7)
            d_l(acad,ol7,ol8)
            d_l(acad,or7,or8)

def b_cap(acad,xs,ys,Hs,ds,Ds,d3s,b,h,updown,oc):
    for i in range(len(Ds)):
        D=Ds[i]
        d3=d3s[i]
        d=ds[i]
        x=xs[i]
        H=Hs[i]
        cap_u(acad,x,ys[2*i],H,d,D,d3,b,h,updown[2*i],oc[2*i])
        cap_u(acad,x,ys[2*i+1],H,d,D,d3,b,h,updown[2*i+1],oc[2*i+1])

def cap_f(acad,x,y,D,d3,d=0,oc=0):
    D0=D+2.5*d3
    D2=D0+2.5*d3
    c=APoint(x,y)
    d_c(acad,c,D2/2,1)
    d_c(acad,c,(D2-4)/2)
    d_c(acad,c,D/2)
    d_c(acad,c,D0/2)
    if oc:
        d_c(acad,c,d/2)
        d_c(acad,c,d/2+1)


def b_cap_f(acad,xs,y,ds,Ds,d3s,ocs):
    for i in range(len(xs)):
        x=xs[i]
        d=ds[i]
        D=Ds[i]
        oc=ocs[i]
        d3=d3s[i]
        if oc:
            cap_f(acad,x,y,D,d3,d,oc)
        else:
            cap_f(acad,x,y,D,d3)
