from pyautocad import Autocad, APoint
from d_pointline import d_pointline
from d_l import d_l

def assemble(acad,x,y,k,mess):
    xall=[]
    xall.append(x)
    xall.append(xall[0]-25)
    xall.append(xall[1]-40)
    xall.append(xall[2]-20)
    xall.append(xall[3]-10)
    xall.append(xall[4]-45)
    xall.append(xall[5]-10)

    for i in range(k+2):
        d_pointline(acad,xall[0],y+i*7,xall[-1],y+i*7)
    for i in range(7):
        d_pointline(acad,xall[i],y,xall[i],y+(k+1)*7)

    item=['序号','名称','数量','材料','标准','备注']
    for i in range(6):
        a=APoint((xall[6-i]+xall[5-i])/2-3.5,y+2.25)
        acad.model.AddText(item[i], a, 2.5)

    for i in range(k):
        for j in range(6):
            if j==1:
                left=1.7*len(mess[i][j])
            else:
                if type(mess[i][j])==float:
                    left=0.7*len(str(mess[i][j]))-1.4
                else:
                    left=1*len(mess[i][j])

            a=APoint((xall[6-j]+xall[5-j])/2-left,y+2.25+i*7+7)
            acad.model.AddText(mess[i][j], a, 2.5)

def title(acad,x,y,name,type='assemble'):

    if type=='assemble':
        xall=[]
        xall.append(x)
        xall.append(xall[0]-40)
        xall.append(xall[1]-40)
        xall.append(xall[2]-20)
        xall.append(xall[3]-35)
        xall.append(xall[4]-15)

        xall.append(xall[0]-25)
        xall.append(xall[6]-40)
    elif type=='part':
        xall=[]
        xall.append(x)
        xall.append(xall[0]-45)
        xall.append(xall[1]-40)
        xall.append(xall[2]-15)
        xall.append(xall[3]-35)
        xall.append(xall[4]-15)

        xall.append(xall[0]-15)
        xall.append(xall[6]-15)
        xall.append(xall[7]-15)
        xall.append(xall[8]-25)
        xall.append(xall[9]-15)

    else:
        print('error type')
        return None

    [dr,dl]=d_pointline(acad,xall[0],y,xall[5],y)
    [ur,ul]=d_pointline(acad,xall[0],y+35,xall[5],y+35)
    d_l(acad,dr,ur)
    d_l(acad,dl,ul)
    d_pointline(acad,xall[5],y+7,xall[2],y+7)
    d_pointline(acad,xall[5],y+14,xall[2],y+14)
    d_pointline(acad,xall[5],y+21,xall[0],y+21)
    d_pointline(acad,xall[2],y+28,xall[0],y+28)
    d_pointline(acad,xall[1],y,xall[1],y+21)
    d_pointline(acad,xall[2],y,xall[2],y+35)
    d_pointline(acad,xall[3],y,xall[3],y+21)
    d_pointline(acad,xall[4],y,xall[4],y+21)
    d_pointline(acad,xall[6],y+21,xall[6],y+35)
    d_pointline(acad,xall[7],y+21,xall[7],y+35)
    if type=='part':

        d_pointline(acad,xall[8],y+21,xall[8],y+35)
        d_pointline(acad,xall[9],y+21,xall[9],y+35)

    text='浙江大学 机电1503班'
    a=APoint((xall[0]+xall[1])/2-1.7*len(text)+2,y+2.25+7)
    acad.model.AddText(text, a, 2.5)

    text='机械设计课程设计'
    a=APoint((xall[2]+xall[1])/2-1.7*len(text),y+2.25+7)
    acad.model.AddText(text, a, 2.5)

    text='审阅'
    a=APoint((xall[4]+xall[5])/2-1.7*len(text),y+2.25)
    acad.model.AddText(text, a, 2.5)

    text='绘图'
    a=APoint((xall[4]+xall[5])/2-1.7*len(text),y+2.25+7)
    acad.model.AddText(text, a, 2.5)

    text='设计'
    a=APoint((xall[4]+xall[5])/2-1.7*len(text),y+2.25+14)
    acad.model.AddText(text, a, 2.5)

    text='王嘉川'
    a=APoint((xall[4]+xall[3])/2-1.7*len(text),y+2.25+14)
    acad.model.AddText(text, a, 2.5)

    text='18/4/23'
    a=APoint((xall[2]+xall[3])/2-0.7*len(text),y+2.25+14)
    acad.model.AddText(text, a, 2.5)

    text=name
    a=APoint((xall[2]+xall[5])/2-1.7*len(text),y+2.25+24.5)
    acad.model.AddText(text, a, 2.5)

    if type=='assemble':
        text='图号'
        a=APoint((xall[2]+xall[7])/2-1.7*len(text),y+2.25+28)
        acad.model.AddText(text, a, 2.5)

        text='比例'
        a=APoint((xall[2]+xall[7])/2-1.7*len(text),y+2.25+21)
        acad.model.AddText(text, a, 2.5)

        text='第  张'
        a=APoint((xall[6]+xall[0])/2-1.2*len(text),y+2.25+28)
        acad.model.AddText(text, a, 2.5)

        text='共  张'
        a=APoint((xall[6]+xall[0])/2-1.2*len(text),y+2.25+21)
        acad.model.AddText(text, a, 2.5)

    if type=='part':
        text='图号'
        a=APoint((xall[9]+xall[10])/2-1.7*len(text),y+2.25+28)
        acad.model.AddText(text, a, 2.5)

        text='材料'
        a=APoint((xall[9]+xall[10])/2-1.7*len(text),y+2.25+21)
        acad.model.AddText(text, a, 2.5)

        text='比例'
        a=APoint((xall[8]+xall[7])/2-1.7*len(text),y+2.25+28)
        acad.model.AddText(text, a, 2.5)

        text='数量'
        a=APoint((xall[8]+xall[7])/2-1.7*len(text),y+2.25+21)
        acad.model.AddText(text, a, 2.5)

        text='第  张'
        a=APoint((xall[6]+xall[0])/2-1.2*len(text),y+2.25+28)
        acad.model.AddText(text, a, 2.5)

        text='共  张'
        a=APoint((xall[6]+xall[0])/2-1.2*len(text),y+2.25+21)
        acad.model.AddText(text, a, 2.5)
