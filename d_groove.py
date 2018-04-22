from pyautocad import Autocad, APoint
from d_l import d_l

def d_groove(acad,flag,mx,my,rx,ry):
    ul=APoint(mx-rx,my+ry)
    ur=APoint(mx+rx,my+ry)
    dl=APoint(mx-rx,my-ry)
    dr=APoint(mx+rx,my-ry)
    if flag=='u':
        d_l(acad,ul,dl)
        d_l(acad,dl,dr)
        d_l(acad,dr,ur)

    elif flag=='d':
        d_l(acad,ul,dl)
        d_l(acad,dr,ur)
        d_l(acad,ur,ul)

    elif flag=='l':
        d_l(acad,dl,dr)
        d_l(acad,dr,ur)
        d_l(acad,ur,ul)

    elif flag=='r':
        d_l(acad,ul,dl)
        d_l(acad,dl,dr)
        d_l(acad,ur,ul)

    else:
        print("错误指定开口方向")

def d_groovea(acad,flag,up,down,left,right):
    ul=APoint(left,up)
    ur=APoint(right,up)
    dl=APoint(left,down)
    dr=APoint(right,down)
    if flag=='u':
        d_l(acad,ul,dl)
        d_l(acad,dl,dr)
        d_l(acad,dr,ur)

    elif flag=='d':
        d_l(acad,ul,dl)
        d_l(acad,dr,ur)
        d_l(acad,ur,ul)

    elif flag=='l':
        d_l(acad,dl,dr)
        d_l(acad,dr,ur)
        d_l(acad,ur,ul)

    elif flag=='r':
        d_l(acad,ul,dl)
        d_l(acad,dl,dr)
        d_l(acad,ur,ul)

    else:
        print("错误指定开口方向")
