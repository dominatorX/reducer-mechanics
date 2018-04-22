from math import cos
from pyautocad import Autocad, APoint
from d_l import d_l
from d_c import d_c
from d_pointline import d_pointline
from d_groove import d_groove,d_groovea
from gear import gear
from d_bearing import d_bearing
from d_sleeve import d_sleeve
from d_bcap import b_cap,b_cap_f
from d_tank import d_tank_u,d_tank_f
from d_bolt import d_bolt_bear_u,d_bolt_bear_f
from d_key import d_key

#清空圆角样条曲线存储文档
f=open('arc.txt','w')
f.close()
f=open('spl.txt','w')
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

#第一根轴
#中心线
top=APoint(0,broadth+60)
bot=APoint(0,-60)
d_l(acad,top,bot)
#中心轴肩
mx=0
my=A1+0.5*b[0]+0.5*midarm
rx=(d[0]+5+5+5)/2
ry=midarm/2
ul=APoint(mx-rx,my+ry)
ur=APoint(mx+rx,my+ry)
d_groove(acad,'u',mx,my,rx,ry)
d_l(acad,ul,ur)

#齿轮一
mx=0
my=A1+short/2
rx=(d[0]+5+5)/2
ry=(b[0]-short)/2
d_groove(acad,'u',mx,my,rx,ry)
#键P219
d_key(acad,mx,my,b[0]-20,10)

#下轴承
left=-(bearin[0])/2
right=(bearin[0])/2
up=A1-b[0]/2+short
down=-bearb[0]/2
d_groovea(acad,'u',up,down,left,right)


#上轴承
mx=0
my=A1+B1
rx=(bearin[0])/2
ry=bearb[0]/2
d_groove(acad,'d',mx,my,rx,ry)

#上轴承轴肩
left=-(d[0]+5+3)/2
right=(d[0]+5+3)/2
up=A1+B1-bearb[0]/2
down=A1+b[0]/2+midarm
d_groovea(acad,'d',up,down,left,right)

#伸出端
[dl,ul]=d_pointline(acad,0-(d[0]/2+1.25),broadth+bearb[0]/2,0-(d[0]/2+1.25),broadth+bearb[0]/2+60)
[dr,ur]=d_pointline(acad,0+(d[0]/2+1.25),broadth+bearb[0]/2,0+(d[0]/2+1.25),broadth+bearb[0]/2+60)
d_l(acad,ul,ur)


#联轴
[dl,ul]=d_pointline(acad,0-(d[0]/2),broadth+bearb[0]/2+60,0-(d[0]/2),broadth+bearb[0]/2+120)
[dr,ur]=d_pointline(acad,0+(d[0]/2),broadth+bearb[0]/2+60,0+(d[0]/2),broadth+bearb[0]/2+120)
d_l(acad,ul,ur)
d_key(acad,(dl.x+dr.x)/2,(ul.y+dl.y)/2,(ul.y-dl.y)-20,6)


#第二根轴
#中心线
top=APoint(afx,broadth+60)
bot=APoint(afx,-60)
d_l(acad,top,bot)
#中心轴肩
left=afx-(d[1]+5+5+5)/2
right=afx+(d[1]+5+5+5)/2
up=A2+B2-b[2]/2
down=A2+b[1]/2
ul=APoint(left,up)
ur=APoint(right,up)
d_groovea(acad,'u',up,down,left,right)
d_l(acad,ul,ur)


#齿轮二
mx=afx
my=A2+short/2
rx=(d[1]+5+5)/2
ry=(b[1]-short)/2
d_groove(acad,'u',mx,my,rx,ry)
#键P219
d_key(acad,mx,my,b[1]-20,12)

#齿轮三
mx=afx
my=A2+B2-short/2
rx=(d[1]+5+5)/2
ry=(b[2]-short)/2
d_groove(acad,'d',mx,my,rx,ry)
d_key(acad,mx,my,b[2]-20,12)

#下轴承
left=afx-(bearin[1])/2
right=afx+(bearin[1])/2
up=A2-b[1]/2+short
down=-bearb[1]/2
d_groovea(acad,'u',up,down,left,right)


#上轴承
left=afx-(bearin[1])/2
right=afx+(bearin[1])/2
up=A2+B2+C2+bearb[1]/2
down=A2+B2+b[2]/2-short
d_groovea(acad,'d',up,down,left,right)

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


#齿轮
#齿轮1
gear(acad,d[0]+5+5,D[0],b[0],0,A1,mn[0],0)
#齿轮2
gear(acad,d[1]+5+5,D[1],b[1],afx,A2,mn[1],1)
#齿轮3
gear(acad,d[1]+5+5,D[2],b[2],afx,A2+B2,mn[2],0)
#齿轮4
gear(acad,d[2]+5+5,D[3],b[3],afx+asx,B3,mn[3],1)

#轴承
d_bearing(acad,0,0,broadth,bearin[0],bearout[0],bearb[0])
d_bearing(acad,afx,0,broadth,bearin[1],bearout[1],bearb[1])
d_bearing(acad,afx+asx,0,broadth,bearin[2],bearout[2],bearb[2])

#套筒
d_sleeve(acad,0,A1-b[0]/2,bearb[0]/2,d[0]+5,d[0]+5+5+10,d[0]+5+(bearout[0]-bearin[0])/4,'d')
d_sleeve(acad,afx,A2-b[1]/2,bearb[1]/2,d[1]+5,d[1]+5+5+10,d[1]+5+(bearout[1]-bearin[1])/4,'d')
d_sleeve(acad,afx,broadth-bearb[1]/2,A2+B2+b[2]/2,d[1]+5,d[1]+5+5+10,d[1]+5+(bearout[1]-bearin[1])/4,'u')
d_sleeve(acad,afx+asx,broadth-bearb[2]/2,B3+b[3]/2,d[2]+5,d[2]+5+5+10,d[2]+5+(bearout[2]-bearin[2])/4,'u')

#箱体壁厚delta
delta=10
#箱盖壁厚delta1
delta1=8.5
#箱座箱盖箱座底凸缘厚度
bo=1.5*delta
bo1=1.5*delta1
bo2=2.5*delta
#地脚螺栓直径及数目
ndf=6
df=20
#轴承旁连接螺栓直径15
ds1=0.75*df
#箱盖箱座连接螺栓直径12 螺栓间距150-200
ds2=0.6*df
S2=200
#轴承端盖螺钉直径4个
ds3=[8,10,10]
#检查孔盖螺钉直径
ds4=8
#dsf ds1 ds2至箱外壁距离26 22 18 ; dsf ds2至凸缘边缘距离24 16
c1=[26,22,18]
c2=[24,20,16]
#轴承座外径 92 122 135
D2=[]
for i in range(len(bearout)):D2.append(bearout[i]+5*ds3[i])
#轴承旁联接螺栓距离
S=D2
#轴承旁凸台半径
R1=c2
#箱外壁至轴承座端面距离
L1=[c1[0]+c2[0]+6,c1[1]+c2[1]+6,c1[2]+c2[2]+6]
#箱盖m1箱座m肋厚
m1=8
m=8.5
#大齿轮顶圆与箱内壁间距离
delt1=1.2*delta
#齿轮端面与箱内壁距离
delt2=delta
# 飞溅润滑 轴承与箱内壁距离
delta3=[5,4,3]
#左端箱体小齿轮距离
delta4=3*delta

#轴承盖
#轴承盖高度
bearcaphigh=[]
for i in range(len(bearb)):bearcaphigh.append(L1[1]-bearb[i]-delta3[i]+1.2*ds3[i]+delta)
xs=[0,afx,afx+asx]
ys=[0-bearb[0]/2,broadth+bearb[0]/2,0-bearb[1]/2,broadth+bearb[1]/2,0-bearb[2]/2,broadth+bearb[2]/2]
updown=['d','u','d','u','d','u']
oc=['c','o','c','c','o','c']
boil=5
hoil=5
b_cap(acad,xs,ys,bearcaphigh,d,bearout,ds3,boil,hoil,updown,oc)
dcap=[]
for i in range(len(bearout)):
    dcap.append(bearout[i]+2.5*ds3[i])

#六角螺栓P206
bolts=[13,16,16]
boltk=[5.3,6.4,6.4]
bolte=[14.4,17.8,17.8]
ysbolt=[]
for i in range(len(bearb)):
    ysbolt.append(0-(-bearb[i]/2-delta3[i]+L1[1]+1.2*ds3[i]+boltk[i]+delta))
    ysbolt.append(broadth+(-bearb[i]/2-delta3[i]+L1[1]+1.2*ds3[i]+boltk[i]+delta))
#盖上螺帽
d_bolt_bear_u(acad,xs,ysbolt,dcap,bolte,boltk)

#销钉
pinb=6
pina=0.8
pinl=28
pind=pinb+1

#箱体
d_tank_u(acad,broadth-(bearb[0]/2+delta3[0]),0+(bearb[0]/2+delta3[0]),0-(D[0]/2+delta4),afx+asx+(D[3]/2+delt1),xs,c1,c2,bearout,S,ds1,ds2,pind,L1,S2,delta)

#------------------------------------------------------------------------------------------------------------------------
##主视图

#轴承盖
ocs=[0,0,1]
b_cap_f(acad,xs,pos_f,d,bearout,ds3,ocs)

#盖上螺帽
d_bolt_bear_f(acad,xs,pos_f,dcap,bolte)

#箱体
hs=[]
for i in range(len(S)):hs.append((S[i]**2/4-(S[i]/2-13.5)**2)**0.5)
h=max(hs)
#13.4为8-60中M16的六角大小

ribb=0.85*delta
inoil=50
d_tank_f(acad,xs,pos_f,S,h,ribb,D[3]+inoil,c1,c2,bo,bo1,bo2,D,delta4,delt1,delta,mn[3],ndf,df)

#油标在低速级P82
