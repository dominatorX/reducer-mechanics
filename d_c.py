from pyautocad import Autocad, APoint
def d_c(acad,a,r,midline=0):
    acad.model.AddCircle(a, r)
    if midline:
        r1=2+r
        b=APoint(a.x-r1,a.y)
        c=APoint(a.x+r1,a.y)
        acad.model.AddLine(b,c)
        d=APoint(a.x,a.y+r1)
        e=APoint(a.x,a.y-r1)
        acad.model.AddLine(d,e)
