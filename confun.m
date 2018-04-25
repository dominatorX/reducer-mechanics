function [ c,ceq ] = confun( x )
%约束条件
%   参考[1]25页例2-3，另外修正了里面错误的参数Y，直接查表了
i=18.85;
sigmah=500;
sigmaf1=530;
sigmaf3=530;
sigmaf2=360;
sigmaf4=360;
T1=22370;
kf=1.2;
ks=1.2;
l=50;
faid=1;
%法面模数取整
lnzv1=log(x(3)/cos(x(6))^3);
lnzv2=log(x(3)*x(5)/cos(x(6))^3);
lnzv3=log(x(4)/cos(x(7))^3);
lnzv4=log(x(4)*i/x(5)/cos(x(7))^3);
YFS1=4.7;%6.92425+5.201102*lnzv1-4.76945*lnzv1^2+1.08188*lnzv1^3-0.053827*lnzv1^4+0.015287*lnzv1^5-0.0074463*lnzv1^6;
YFS2=4.7;%6.92425+5.201102*lnzv2-4.76945*lnzv2^2+1.08188*lnzv2^3-0.053827*lnzv2^4+0.015287*lnzv2^5-0.0074463*lnzv2^6;
YFS3=4.7;%6.92425+5.201102*lnzv3-4.76945*lnzv3^2+1.08188*lnzv3^3-0.053827*lnzv3^4+0.015287*lnzv3^5-0.0074463*lnzv3^6;
YFS4=4.7;%6.92425+5.201102*lnzv4-4.76945*lnzv4^2+1.08188*lnzv4^3-0.053827*lnzv4^4+0.015287*lnzv4^5-0.0074463*lnzv4^6;
c=[590^2*(x(5)+1)*kf*T1*cos(x(6))^3-sigmah^2*x(5)*x(1)^3*x(3)^3*faid;
   590^2*(i+x(5))*ks*T1*0.97*x(5)*cos(x(7))^3-sigmah^2*i*x(2)^3*x(4)^3*faid;
   1.6*kf*T1*YFS1*cos(x(6))-x(1)^3*x(3)^2*faid*sigmaf1;
   1.6*kf*T1*YFS2*cos(x(6))-x(1)^3*x(3)^2*faid*sigmaf2;
   1.6*ks*T1*0.97*x(5)*YFS3*cos(x(7))-x(2)^3*x(4)^2*faid*sigmaf3;
   1.6*ks*T1*0.97*x(5)*YFS4*cos(x(7))-x(2)^3*x(4)^2*faid*sigmaf4;
   2*cos(x(6))*cos(x(7))*l*x(5)+x(1)*x(3)*x(5)^2*cos(x(7))+2*cos(x(7))*cos(x(6))*x(1)*x(5)-cos(x(6))*x(2)*x(4)*(x(5)+i);
   (x(1)*x(3)*x(5)^2*cos(x(7))-x(2)*x(4)*i*cos(x(6)))^2-x(5)^2*cos(x(6))^2*cos(x(7))^2;
   ];
ceq=[];

end

