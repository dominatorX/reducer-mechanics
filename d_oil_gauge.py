from math import cos,sin
from pyautocad import Autocad, APoint
from d_l import d_l
from d_c import d_c
from d_pointline import d_pointline
from d_arc import d_arc

'''
油标
    获得点并旋转坐标系，再打印在合理的地方
'''
#编号从1-14左右对称布置
def d_oil_gauge(acad,xm,ym,xita=-3.1415926535/4):
    d=20
    d2=20
    d3=8
    h=42
    a=15
    b=10
    c=6
    D=32
    D1=26
    sl=1
    ups=20
    inoil=20
    bot=30
    x=[-(D-sl)/2,(D-sl)/2,
       -(D)/2,(D)/2,
       -(D)/2,(D)/2,
       -(D-sl)/2,(D-sl)/2,
       -(D1)/2,(D1)/2,
       -(D1)/2,(D1)/2,
       -(d-sl)/2,(d-sl)/2,
       -(d-sl)/2,(d-sl)/2,
       -(d)/2,(d)/2,
       -(d)/2,(d)/2,
       -d3/2,d3/2,
       -d3/2,d3/2,
       -d3/2,d3/2,
       -d3/2,d3/2]
    y=[h,h,
       h-sl,h-sl,
       h-b+sl,h-b+sl,
       h-b,h-b,
       a+c,a+c,
       a,a,
       a,a,
       a-sl,a-sl,
       a-sl,a-sl,
       (d-d3)/2,(d-d3)/2,
       0,0,
       -ups,-ups,
       -(inoil+ups),-(inoil+ups),
       -(inoil+ups+bot),-(inoil+ups+bot)]
    #辅助线
    x.append(0)
    x.append(0)
    y.append(-(inoil+ups+bot+2))
    y.append(h+2)

    #坐标变换
    #旋转角度并移动位置

    xnew=[]
    ynew=[]
    for i in range(len(x)):
        xnew.append(x[i]*cos(xita)-y[i]*sin(xita)+xm)
        ynew.append(x[i]*sin(xita)+y[i]*cos(xita)+ym)


    for i in range(0,len(xnew)-2,2):
        d_pointline(acad,xnew[i],ynew[i],xnew[i+1],ynew[i+1])
        if i==6 or i==10 or i==14 or i==26:
            pass
        else:
            d_pointline(acad,xnew[i],ynew[i],xnew[i+2],ynew[i+2])
            d_pointline(acad,xnew[i+1],ynew[i+1],xnew[i+3],ynew[i+3])
    d_pointline(acad,xnew[28],ynew[28],xnew[29],ynew[29])

    #画圆弧，命令导出到log文件

    arc=[-D1/2,a+c,-d2/2,(h-(b+c+a-sl))/2+a+c,-(D-sl)/2,h-b,
          D1/2,a+c,d2/2,(h-(b+c+a-sl))/2+a+c,(D-sl)/2,h-b]
    arcnew=[]
    for i in range(len(arc)//2):
        arcnew.append(arc[i*2]*cos(xita)-arc[i*2+1]*sin(xita)+xm)
        arcnew.append(arc[i*2]*sin(xita)+arc[i*2+1]*cos(xita)+ym)

    d_arc(arcnew)


