clc 
t1=@(x,y) x+tan(x*y);
ezplot(t1)
grid on
hold on
t2=@(x,y) (y*y-7.5)^2+log(x);
ezplot(t2)
[x,y]=solve('x+tan(x*y)','(y*y-7.5)^2+log(x)')
plot (x,y,'*r','MarkerSize',5)


clc
disp('x=')
fprintf('%.5f\n',x);
disp('y=')
fprintf('%.5f\n',y);
