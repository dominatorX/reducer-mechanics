itemall=['轴','齿轮','轴上配件','轴承','配件']
zhou=['轴','倒角：P155.8-5','键槽','中心线']
gear=['齿轮','剖线']

tabone=['轴上配件','轴承透盖','密封圈','剖线','螺栓','螺钉中心线','调整垫片','轴承闷盖']
bearing=['轴承','剖线','配合','中心线','圆角']

stuffs=['配件','排油螺栓','封油垫','杆式油垫','起盖螺钉','螺栓','螺母','垫圈','箱盖','箱座','圆锥销','检查孔盖','通气器']

done=[]
for i in done:
    if i in zhou:
        zhou.remove(i)
    if i in gear:
        gear.remove(i)
    if i in tabone:
        tabone.remove(i)
    if i in bearing:
        bearing.remove(i)
    if i in stuffs:
        stuffs.remove(i)
if len(zhou)==1:
    itemall.remove(zhou[0])
else:
    print(zhou[0]+'中还有'+str(zhou[1:])+'没画呢，菜鸡')
if len(gear)==1:
    itemall.remove(gear[0])
else:
    print(gear[0]+'中还有'+str(gear[1:])+'没画呢，菜鸡')
if len(tabone)==1:
    itemall.remove(tabone[0])
else:
    print(tabone[0]+'中还有'+str(tabone[1:])+'没画呢，菜鸡')
if len(bearing)==1:
    itemall.remove(bearing[0])
else:
    print(bearing[0]+'中还有'+str(bearing[1:])+'没画呢，菜鸡')
if len(stuffs)==1:
    itemall.remove(stuffs[0])
else:
    print(stuffs[0]+'中还有'+str(stuffs[1:])+'没画呢，菜鸡')
print('还剩'+str(itemall))

