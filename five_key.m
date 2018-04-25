%转矩
T=[22.3700 74.3671 74.3671 392.6536]*1000;
%齿轮接触部分轴宽
d=([20,30,30,40]+10);

mn=[4 4 6 6];
z=[17 93 18 62];
beita=[0.1396 0.1396 0.1396 0.1396];
D=z.*mn./cos(beita);
%齿轮宽
broad(1)=75;
broad(2)=D(1);
broad(3)=115;
broad(4)=D(3);
L=broad-10;
b=[10 12 12 14];
h=[8 8 8 9];
Lc=L-b;
sigma=2*T./d./Lc./h*2;
sprintf('应力为%d,%d,%d,%dMPa',sigma(1),sigma(2),sigma(3),sigma(4))

