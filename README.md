# reducer-mechanics 
但愿没有各大机械学院的学生发现这个文档吧...否则的话整个任务的工作量就只剩一半了（这课就废了）
机械设计课程设计任务，python的pyautocad包。使用时在主文件dataall里设置好前面算好的参数，然后直接运行即可。由于下周四就要交作业了，还没画完，改用手画了。
完全放弃代码效率，只为了实现自动化。而且对于个人而言能把它画完就已经很要命了。代码工程量大约一百小时左右，两三周有空就在画。pyautocad调用了cad的原码库但是我找不到，所以只使用了画线画圆画点的功能。为了增加圆角和样条曲线而添加了文档arc和spl，运行主程序结束后点开复制到命令行即可画出圆弧。
因为没有线面操作，所以线性调整，剖面线等工作记录在categoryone中，出图后逐条修改即可。
各文档说明
dataall：主文件，打开CAD后新建一张图，然后再开python运行这个文件就能画图。
d_l：画线
d_c：画圆
d_pointline：带端点的线
d_groove：有一个开口的矩形，以上都是为了画图方便，快一点
gear：画齿轮
d_bearing：轴承
d_sleeve：轴套
d_bcap：轴承盖
d_tank：箱体，包括正视图和俯视图
d_bolt：螺栓
d_key：画键
2018/4/22.wjc in zju
