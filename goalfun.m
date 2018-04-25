function [ f ] = goalfun( x )
%目标函数
%   要求这个量最小，即中心距
i=18.85;
f=x(1)*x(3)*(1+x(5))/2/cos(x(6))+x(2)*x(4)*(1+i/x(5))/2/cos(x(7));
end

