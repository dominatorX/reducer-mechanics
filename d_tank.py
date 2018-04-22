from pyautocad import Autocad, APoint
from d_l import d_l
from d_c import d_c
from d_pointline import d_pointline
from d_bear_sup import d_bear_sup
from math import cos,sin
from d_oil_gauge import d_oil_gauge
from d_arc import d_arc
from d_spl import d_spl
import random

def d_tank_u(acad,up,down,left,right,xs,c1,c2,ds,Ss,d1,d2,pind,L,S2,delta):
    #箱体俯视图总
    a=7
    b=6
    ys=[up,down,up,down,up,down]
    updown=['u','d','u','d','u','d']
    dot=[[0 for i in range(8)] for k in range(len(updown))]
    for i in range(len(xs)):
        x=xs[i]
        d=ds[i]
        S=Ss[i]
        dot[i*2]=d_bear_sup(acad,x,ys[2*i],c1[1],c2[1],L[1]+delta,d,S,d1,a,b,delta,updown[2*i])
        dot[i*2+1]=d_bear_sup(acad,x,ys[2*i+1],c1[1],c2[1],L[1]+delta,d,S,d1,a,b,delta,updown[2*i+1])

    for i in range(len(updown)-2):
        d_l(acad,dot[i][1],dot[i+2][0])
        d_l(acad,dot[i][3],dot[i+2][2])
        d_l(acad,dot[i][5],dot[i+2][4])
        d_l(acad,dot[i][7],dot[i+2][6])

    [l1,l2]=d_pointline(acad,left,down,left,up)
    [l3,l4]=d_pointline(acad,left-(c1[2]+c2[2]+delta),down-(c1[1]+c2[1]+delta),left-(c1[2]+c2[2]+delta),up+(c1[1]+c2[1]+delta))
    [lo1,lo2]=d_pointline(acad,left-a,down-a,left-a,up+a)
    [lo3,lo4]=d_pointline(acad,left-(a+b),down-(a+b),left-(a+b),up+(a+b))
    d_l(acad,l4,dot[0][2])
    d_l(acad,l3,dot[1][2])
    d_l(acad,l2,dot[0][0])
    d_l(acad,l1,dot[1][0])
    d_l(acad,lo4,dot[0][6])
    d_l(acad,lo3,dot[1][6])
    d_l(acad,lo2,dot[0][4])
    d_l(acad,lo1,dot[1][4])

    mid=0.5*(up+down)
    l5=APoint(left-(c1[2]+delta),S2/2+mid)
    l6=APoint(left-(c1[2]+delta),-S2/2+mid)
    d_c(acad,l5,d2/2,1)
    d_c(acad,l6,d2/2,1)

    [r1,r2]=d_pointline(acad,right,down,right,up)
    [r3,r4]=d_pointline(acad,right+(c1[2]+c2[2]+delta),down-(c1[1]+c2[1]+delta),right+(c1[2]+c2[2]+delta),up+(c1[1]+c2[1]+delta))
    [ro1,ro2]=d_pointline(acad,right+a,down-a,right+a,up+a)
    [ro3,ro4]=d_pointline(acad,right+(a+b),down-(a+b),right+(a+b),up+(a+b))
    d_l(acad,r4,dot[len(updown)-2][3])
    d_l(acad,r3,dot[len(updown)-1][3])
    d_l(acad,r2,dot[len(updown)-2][1])
    d_l(acad,r1,dot[len(updown)-1][1])
    d_l(acad,ro4,dot[len(updown)-2][7])
    d_l(acad,ro3,dot[len(updown)-1][7])
    d_l(acad,ro2,dot[len(updown)-2][5])
    d_l(acad,ro1,dot[len(updown)-1][5])

    mid=0.5*(up+down)
    r5=APoint(right+c1[2]+delta,S2/2+mid)
    r6=APoint(right+c1[2]+delta,-S2/2+mid)
    d_c(acad,r5,d2/2,1)
    d_c(acad,r6,d2/2,1)

    #销钉
    p1=APoint(right+c1[2]+delta,down-(c1[1]+delta))
    d_c(acad,p1,pind/2,1)
    p2=APoint(left-(c1[2]+delta),up+c1[1]+delta)
    d_c(acad,p2,pind/2,1)

    #起盖螺钉
    upc=APoint(left-(c1[2]+delta),-S2/4+mid)
    d_c(acad,upc,d2/2,1)

def d_tank_f(acad,xs,y,Ss,h,ribb,H,c1,c2,bo0,bo1,bo2,D,delta4,delt1,delta,m,ndf,df):
    #箱体前视图总

    #与轴承盖接触圆
    dot=[[0 for i in range(6)] for k in range(len(xs))]
    for i in range(len(xs)):
        x=xs[i]
        S=Ss[i]
        dot[i]=d_tank_f_bearcap(acad,x,y,S,h,ribb,H-bo2)

    #凸台
    for i in range(len(xs)-1):
        d_l(acad,dot[i][1],dot[i+1][0])
        d_l(acad,dot[i][3],dot[i+1][2])

    [l1,l3]=d_pointline(acad,xs[0]-(Ss[0]/2+c2[1])-(h-bo0)/10,y+bo1,xs[0]-(Ss[0]/2+c2[1]),y+h)
    [l2,l4]=d_pointline(acad,xs[0]-(Ss[0]/2+c2[1])-(h-bo0)/10,y-bo0,xs[0]-(Ss[0]/2+c2[1]),y-h)
    d_l(acad,dot[0][0],l3)
    d_l(acad,dot[0][2],l4)

    [r1,r3]=d_pointline(acad,xs[2]+(Ss[2]/2+c2[1])+(h-bo0)/10,y+bo1,xs[2]+(Ss[2]/2+c2[1]),y+h)
    [r2,r4]=d_pointline(acad,xs[2]+(Ss[2]/2+c2[1])+(h-bo0)/10,y-bo0,xs[2]+(Ss[2]/2+c2[1]),y-h)
    d_l(acad,dot[len(xs)-1][1],r3)
    d_l(acad,dot[len(xs)-1][3],r4)

    left=xs[0]-D[0]/2-delta4-delta
    [l4,l5]=d_pointline(acad,xs[0]-(Ss[0]**2/4-bo1**2)**0.5,y+bo1,left-c1[2]-c2[2],y+bo1)
    [l6,l7]=d_pointline(acad,xs[0]-(Ss[0]**2/4-bo0**2)**0.5,y-bo0,left-c1[2]-c2[2],y-bo0)
    d_l(acad,l5,l7)

    right=xs[2]+D[3]/2+delt1+delta
    [r4,r5]=d_pointline(acad,xs[2]+(Ss[2]**2/4-bo1**2)**0.5,y+bo1,right+c1[2]+c2[2],y+bo1)
    [r6,r7]=d_pointline(acad,xs[2]+(Ss[2]**2/4-bo0**2)**0.5,y-bo0,right+c1[2]+c2[2],y-bo0)
    d_l(acad,r5,r7)

    for i in range(len(xs)-1):d_pointline(acad,xs[i]+Ss[i]/2,y,xs[i+1]-Ss[i+1]/2,y)
    d_pointline(acad,xs[0]-Ss[0]/2,y,left-c1[2]-c2[2],y)
    d_pointline(acad,xs[2]+Ss[2]/2,y,right+c1[2]+c2[2],y)

    #箱座
    #油箱油高度 坐标
    oilheight=50+2.25*m
    oilcord=-H+bo2+oilheight
    #游标插入位置
    xita=-3.1415926535/4
    xoilgauge=right-delta-15*sin(xita)
    yoilgauge=y+oilcord+cos(xita)*30
    d_oil_gauge(acad,xoilgauge,yoilgauge,xita)

    Din=30
    Dind=20
    #插入口
    xopen=[-33+10/cos(xita),33-10/cos(xita),
       -Din/2,Din/2,
       -Din/2,Din/2,
       -Dind/2,Dind/2,
       -Dind/2,Dind/2,
       33-10/cos(xita)]
    yopen=[15+3,15+3,
       15+3,15+3,
       15,15,
       15,15,
       -5,-25,
       18-2*(33-10/cos(xita))]
    xopennew=[]
    yopennew=[]
    for i in range(len(xopen)):
        xopennew.append(xopen[i]*cos(xita)-yopen[i]*sin(xita)+xoilgauge)
        yopennew.append(xopen[i]*sin(xita)+yopen[i]*cos(xita)+yoilgauge)
    d_pointline(acad,xopennew[0],yopennew[0],xopennew[1],yopennew[1])
    d_pointline(acad,xopennew[2],yopennew[2],xopennew[4],yopennew[4])
    d_pointline(acad,xopennew[3],yopennew[3],xopennew[5],yopennew[5])
    d_pointline(acad,xopennew[4],yopennew[4],xopennew[5],yopennew[5])
    d_pointline(acad,xopennew[6],yopennew[6],xopennew[8],yopennew[8])
    d_pointline(acad,xopennew[7],yopennew[7],xopennew[9],yopennew[9])
    d_pointline(acad,xopennew[8],yopennew[8],xopennew[9],yopennew[9])
    d_pointline(acad,xopennew[1],yopennew[1],xopennew[10],yopennew[10])

    #排油孔
    #p85
    [ur,ul,dlog2,dout1,dout2]=d_tank_f_oil_exit(acad,right-delta,-H+12-1+bo2+y,delta,bo2)

    #连接
    d_pointline(acad,ul.x,ul.y,xopennew[-2],yopennew[-2])
    d_pointline(acad,ur.x,ur.y,xopennew[-1],yopennew[-1])

    #现在上面的剖面线端点为
    sul=APoint(xopennew[-3],yopennew[-3])
    sur=APoint(xopennew[0],yopennew[0])
    #油箱内壁、箱底壁、箱底
    #dlog2,dout1,dout2

    #玩蛇~
    spul=APoint(sul.x,sul.y+50+random.random()*10)
    spur=APoint(sur.x,sur.y+10+random.random()*10)
    spd1=APoint(dlog2.x-50-10*random.random(),dlog2.y)
    spd2=APoint(dout1.x-70-10*random.random(),dout1.y)
    spd3=APoint(dout2.x-70-10*random.random(),dout2.y)
    d_l(acad,spul,sul)
    d_l(acad,spur,sur)
    d_l(acad,spd1,dlog2)
    d_l(acad,spd2,dout1)
    d_l(acad,spd3,dout2)
    trans=APoint(spd2.x-10*random.random(),spul.y+10*random.random())
    d_spl([spur.x,spur.y,spul.x,spul.y,trans.x,trans.y,spd1.x,spd1.y,spd2.x,spd2.y,spd3.x,spd3.y,])

    #底座
    arc1=2
    dfS=100
    nd=ndf//2
    long=(right-left-dfS)/(nd-1)
    pdu=APoint(left+arc1,y-H+bo2)
    d_l(acad,pdu,spd1)
    [pdu2,pd1]=d_pointline(acad,left,y-H+bo2-arc1,left,y-H)
    pd=['' for i in range(4*nd)]
    arc2=bo2-delta
    for i in range(nd-1):
        [pd[i],pd[i+1]]=d_pointline(acad,left+i*long,y-H,left+i*long+dfS,y-H)
        [pd[i+2],pd[i+3]]=d_pointline(acad,left+i*long+dfS+bo2-delta,y-H+bo2-delta,left+(i+1)*long-(bo2-delta),y-H+bo2-delta)
        ca1=APoint(i*long+dfS+arc2+left,y-H)
        ca2=APoint((i+1)*long-arc2+left,y-H)
        d_arc([ca1.x-arc2,ca1.y,ca1.x-0.5**0.5*arc2,ca1.y+0.5**0.5*arc2,ca1.x,ca1.y+arc2,
              ca2.x+arc2,ca2.y,ca2.x+0.5**0.5*arc2,ca2.y+0.5**0.5*arc2,ca2.x,ca2.y+arc2])
        d_pointline(acad,left+dfS/2+i*long,y-H-2,left+dfS/2+i*long,y-H+2+bo2)
    d_pointline(acad,left+dfS/2+(nd-1)*long,y-H-2,left+dfS/2+(nd-1)*long,y-H+2+bo2)
    d_pointline(acad,spd3.x,spd3.y,right-dfS,y-H)
    ca1=APoint(pdu.x,pdu.y-arc1)
    d_arc([ca1.x-arc1,ca1.y,ca1.x-0.5**0.5*arc1,ca1.y+0.5**0.5*arc1,ca1.x,ca1.y+arc1])
    #螺栓
    d_pointline(acad,left+dfS/2+long-df/2,y-H,left+dfS/2+long-df/2,y-H+bo2-5)
    d_pointline(acad,left+dfS/2+long+df/2,y-H,left+dfS/2+long+df/2,y-H+bo2-5)
    [pdsul,pdsdl]=d_pointline(acad,left+dfS/2+long-df,y-H+bo2,left+dfS/2+long-df,y-H+bo2-5)
    [pdsur,pdsdr]=d_pointline(acad,left+dfS/2+long+df,y-H+bo2,left+dfS/2+long+df,y-H+bo2-5)
    d_l(acad,pdsdl,pdsdr)

def d_tank_f_oil_exit(acad,x,y,delta,bo2):
    #排油口
    d=24
    D0=34
    L=31
    l=16
    a=4
    D=25.4
    S=22
    d1=26
    H=2
    gear=2
    slot=3
    width=2*delta
    widtha=2*delta+L-l+H
    [u1,u2]=d_pointline(acad,widtha+x,D/2+y,width+a+H+x,D/2+y)
    d_pointline(acad,widtha+x,D/6+y,width+a+H+x,D/6+y)
    d_pointline(acad,widtha+x,-D/6+y,width+a+H+x,-D/6+y)
    [dn1,dn2]=d_pointline(acad,widtha+x,-D/2+y,width+a+H+x,-D/2+y)
    d_l(acad,u1,dn1)
    [u3,dn3]=d_pointline(acad,width+a+H+x,-D0/2+y,width+a+H+x,D0/2+y)
    [u4,dn4]=d_pointline(acad,width+H+x,-D0/2+y,width+H+x,D0/2+y)
    d_l(acad,u3,u4)
    d_l(acad,dn3,dn4)
    d_pointline(acad,width+H+x,(d-slot)/2+y,width+x,(d-slot)/2+y)
    d_pointline(acad,width+H+x,-(d-slot)/2+y,width+x,-(d-slot)/2+y)
    [u6,u9]=d_pointline(acad,width+x,(d-gear)/2+y,widtha+x-(L),(d-gear)/2+y)
    [dn6,dn9]=d_pointline(acad,width+x,-(d-gear)/2+y,widtha+x-(L),-(d-gear)/2+y)
    [u7,u8]=d_pointline(acad,width+x,(d)/2+y,widtha+x-(L-gear),(d)/2+y)
    [dn7,dn8]=d_pointline(acad,width+x,-(d)/2+y,widtha+x-(L-gear),-(d)/2+y)
    d_l(acad,u6,dn6)
    d_l(acad,u9,dn9)
    d_l(acad,u8,dn8)
    d_l(acad,u8,u9)
    d_l(acad,dn8,dn9)

    #垫片
    d_pointline(acad,width+H+x,(d1)/2+y,width+x,(d1)/2+y)
    d_pointline(acad,width+H+x,-(d1)/2+y,width+x,-(d1)/2+y)
    [u4,u5]=d_pointline(acad,width+H+x,(D0)/2+y,width+x,(D0)/2+y)
    [dn4,dn5]=d_pointline(acad,width+H+x,-(D0)/2+y,width+x,-(D0)/2+y)
    d_l(acad,u5,u6)
    d_l(acad,dn5,dn6)

    #螺纹孔
    u10=APoint(x+delta,y+D0/2+delta)
    d_arc([u10.x,u10.y,u10.x+(1-0.5**0.5)*delta,u10.y-(0.5**0.5)*delta,u10.x+delta,u10.y-delta])
    d_pointline(acad,x,(d-gear)/2+y,widtha+x-(L),(d-gear)/2+y)
    d_pointline(acad,x,-(d-gear)/2+y,widtha+x-(L),-(d-gear)/2+y)
    [u11,dn11]=d_pointline(acad,x,(d)/2+y,x,-(d)/2+y)
    d_l(acad,u11,u8)
    d_l(acad,dn11,dn8)
    arcr=2
    logbottom=10
    dlog1=APoint(x-logbottom,y-d/2)
    d_l(acad,dlog1,dn11)
    dlog2=APoint(x-arcr,y-(d-gear)/2)
    dout=APoint(x+width,y-D0/2)
    arcrb=delta+(d-gear)/2-D0/2
    [dout1,dout2]=d_pointline(acad,dout.x-arcrb,dout.y-arcrb,dout.x-arcrb,y-(d-gear)/2-bo2)
    arc=[dlog2.x,dlog2.y,dlog2.x+0.5**0.5*arcr,dlog2.y+(1-0.5**0.5)*arcr,dlog2.x+arcr,dlog2.y+arcr,
         dlog1.x,dlog1.y,dlog1.x-0.5**0.5*gear/2,dlog1.y+(1-0.5**0.5)*gear/2,dlog1.x-gear/2,dlog1.y+gear/2,
         dout.x,dout.y,dout.x-0.5**0.5*arcrb,dout.y-(1-0.5**0.5)*arcrb,dout.x-arcrb,dout.y-arcrb]
    d_arc(arc)
    return u10,u11,dlog2,dout1,dout2

def d_tank_f_bearcap(acad,x,y,S,h,ribb,H):
    #轴承盖
    sli=1
    [l1,l2]=d_pointline(acad,x-(ribb/2+2*sli),y-H,x-(ribb/2+sli),y-(H-sli))
    [r1,r2]=d_pointline(acad,x+(ribb/2+2*sli),y-H,x+(ribb/2+sli),y-(H-sli))
    [l3,l4]=d_pointline(acad,x-(ribb/2+sli),y-H,x-(ribb/2),y-(H-sli))
    [r3,r4]=d_pointline(acad,x+(ribb/2+sli),y-H,x+(ribb/2),y-(H-sli))
    l5=APoint(x-(ribb/2+sli),y-((S+sli)*(S+sli)/4-(ribb/2+sli)**2)**0.5)
    r5=APoint(x+(ribb/2+sli),y-((S+sli)*(S+sli)/4-(ribb/2+sli)**2)**0.5)
    l6=APoint(x-(ribb/2),y-((S)*(S)/4-(ribb/2)**2)**0.5)
    r6=APoint(x+(ribb/2),y-((S)*(S)/4-(ribb/2)**2)**0.5)
    supl1=APoint(x-(S**2/4-h**2)**0.5,y+h)
    supr1=APoint(x+(S**2/4-h**2)**0.5,y+h)
    supl2=APoint(x-(S**2/4-h**2)**0.5,y-h)
    supr2=APoint(x+(S**2/4-h**2)**0.5,y-h)
    d_l(acad,l2,l5)
    d_l(acad,r2,r5)
    d_l(acad,l4,l6)
    d_l(acad,r4,r6)
    c=APoint(x,y)
    d_c(acad,c,S/2)
    d_c(acad,c,(S+sli)/2)
    return supl1,supr1,supl2,supr2,l1,r1
