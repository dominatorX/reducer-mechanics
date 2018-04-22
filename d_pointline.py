from math import cos
from pyautocad import Autocad, APoint
from d_l import d_l

def d_pointline(acad,x1,y1,x2,y2):
    a=APoint(x1,y1)
    b=APoint(x2,y2)
    d_l(acad,a,b)
    return a,b
