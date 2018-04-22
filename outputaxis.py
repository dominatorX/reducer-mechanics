from math import cos
from pyautocad import Autocad, APoint
from d_l import d_l
from d_pointline import d_pointline
from d_groove import d_groove,d_groovea
from d_key import d_key
f=open('arc.txt','w')
f.close()
#三视图间距
pos_f=950
pos_l=900

acad=Autocad()
T=[22.3700 ,74.3671, 74.3671, 392.6536]#转矩
P=[3.3731 , 3.2555  , 3.1421]#功率
n=[1440  ,  418.0645 ,76.4204]#转速
mn=[4 ,4 ,6 ,6]#模数
z=[17 ,93,18 ,62]#齿数
beita=[0.1396, 0.1396, 0.1396 ,0.1396]#斜齿轮角
d=[20 ,30, 40]#轴最小直径
D=[]#齿轮直径
for i in range(len(z)):
    D.append(z[i]*mn[i]/cos(beita[i]))
b=[]#齿轮厚
b.append(75)
b.append(D[0])
b.append(115)
b.append(D[2])
broadth=240#左右轴承中心距
midarm=10#中央轴肩宽
topedge=22#轴承和齿轮间距
downedge=broadth-midarm-topedge-b[2]-(b[0]+b[1])/2#和下端间距
A1=downedge+b[0]/2
B1=broadth-A1
A2=A1
C2=topedge+b[2]/2
B2=broadth-A2-C2
C3=C2
B3=broadth-C3#每根轴三段
#轴承系数
bearin=[25 ,35 ,45]
bearout=[52 ,72 ,85]
bearb=[15 ,17 ,19]
#长度间距
afx=(D[0]+D[1])/2
asx=(D[2]+D[3])/2
short=2.5#轴小于齿轮长度




#第三根轴
#中心线
top=APoint(afx+asx,broadth+60)
bot=APoint(afx+asx,-60)
d_l(acad,top,bot)
#中心轴肩
mx=afx+asx
my=B3-0.5*b[3]-0.5*midarm
rx=(d[2]+5+5+5)/2
ry=midarm/2
ul=APoint(mx-rx,my+ry)
ur=APoint(mx+rx,my+ry)
d_groove(acad,'u',mx,my,rx,ry)
d_l(acad,ul,ur)

#齿轮四
mx=afx+asx
my=B3-short/2
rx=(d[2]+5+5)/2
ry=(b[3]-short)/2
d_groove(acad,'d',mx,my,rx,ry)
#键P219
d_key(acad,mx,my,b[3]-20,14)

#上轴承
left=afx+asx-(bearin[2])/2
right=afx+asx+(bearin[2])/2
up=B3+C3+bearb[2]/2
down=B3+b[3]/2-short
d_groovea(acad,'d',up,down,left,right)


#下轴承
mx=afx+asx
my=0
rx=(bearin[2])/2
ry=bearb[2]/2
d_groove(acad,'u',mx,my,rx,ry)

#下轴承轴肩
left=afx+asx-(d[2]+5+3)/2
right=afx+asx+(d[2]+5+3)/2
up=B3-b[3]/2-midarm
down=bearb[2]/2
d_groovea(acad,'u',up,down,left,right)

#伸出端
[ul,dl]=d_pointline(acad,afx+asx-(d[2]/2+1.25),-bearb[2]/2,afx+asx-(d[2]/2+1.25),-(bearb[2]/2+60))
[ur,dr]=d_pointline(acad,afx+asx+(d[2]/2+1.25),-bearb[2]/2,afx+asx+(d[2]/2+1.25),-(bearb[2]/2+60))
d_l(acad,dl,dr)

#联轴
[ul,dl]=d_pointline(acad,afx+asx-(d[2]/2),-(bearb[2]/2+60),afx+asx-(d[2]/2),-(bearb[2]/2+120))
[ur,dr]=d_pointline(acad,afx+asx+(d[2]/2),-(bearb[2]/2+60),afx+asx+(d[2]/2),-(bearb[2]/2+120))
d_l(acad,dl,dr)
d_key(acad,(ul.x+ur.x)/2,(ul.y+dl.y)/2,(ul.y-dl.y)-20,12)
