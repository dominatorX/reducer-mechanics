'''
画圆弧
    好了我也不知道我怎么这么变态真的把这个写出来了
'''
def d_arc(arc):
    f=open('arc.txt','a')
    for i in range(0,len(arc),6):
        f.write('ARC\n{},{}\n{},{}\n{},{}\n\n'.format(arc[0+i],arc[1+i],arc[2+i],arc[3+i],arc[4+i],arc[5+i]))
    f.close()

def d_arc_c(arc):
    #该方法由于CAD致命的智障命令流用不了
    f=open('arc.txt','a')
    for i in range(0,len(arc),5):
        f.write('ARC\nC\n{},{}\n{},{}\nA\n{}\n\n'.format(arc[0+i],arc[1+i],arc[2+i],arc[3+i],arc[4+i]))
    f.close()

