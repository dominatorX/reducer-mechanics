from pyautocad import Autocad, APoint
from d_pointline import d_pointline
from d_oil_gauge import d_oil_gauge
from part_bar import assemble,title
import xlrd

#明细栏
data = xlrd.open_workbook('E:\\作业\\大三下\\鸡舍射击\\零件.xlsx')
table = data.sheets()[0]
mess=[table.row_values(i) for i in range(table.nrows)]
k = table.nrows
acad=Autocad()
assemble(acad,1475+300,-90+35,k,mess)

#标题栏
title(acad,1475+300,-90,'两级斜齿圆柱齿轮减速器')
