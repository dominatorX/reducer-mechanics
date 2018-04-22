'''
画样条曲线
    一发不可收拾系列
'''
def d_spl(points):
    f=open('spl.txt','a')
    f.write('SPL\n')
    for i in range(0,len(points),2):
        f.write('{},{}\n'.format(points[i],points[1+i]))
    f.write('\n\n')
    f.close()
