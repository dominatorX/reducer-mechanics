from pyautocad import Autocad,APoint
from d_arc import d_arc
from d_l import d_l
'''
键
'''


def d_key(acad,x,y,L,b):
    ul=APoint(x-b/2,y+(L-b)/2)
    ur=APoint(x+b/2,y+(L-b)/2)
    dl=APoint(x-b/2,y-(L-b)/2)
    dr=APoint(x+b/2,y-(L-b)/2)
    d_l(acad,ul,dl)
    d_l(acad,ur,dr)
    d_arc([x-b/2,y+(L-b)/2,x,y+(L)/2,x+b/2,y+(L-b)/2])
    d_arc([x-b/2,y-(L-b)/2,x,y-(L)/2,x+b/2,y-(L-b)/2])
