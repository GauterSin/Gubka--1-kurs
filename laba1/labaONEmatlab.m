clc
clear
disp('Уравнение y = 3*x-A*exp**x')
a1=0
a=input('a=')
b=input('b=')
x=a:0.1:b
plot(x,f1(x),'r')
grid on;
hold on;
f=inline('3*x-A*exp**x');
disp('fzero')
y0=0
x0=fzero(@f1,0)
plot(x0,y0,'b.','Markersize',22)
disp('fsolve')
x1=fsolve(@f1,a)


disp('Метод касательных')
e=input('e=')
disp('Введите занчение между a и b')
c=input('c=')
if f1(a)*f3(c)>0
    xx=a
    disp(xx)
    while abs(f1(xx))>e 
        
        xx=xx-f1(xx)/f2(xx)
        disp(xx)
    end
end

if f1(b)*f3(c)>0
    xx=b
    disp(xx)
    while abs(f1(xx))>e
        
        xx=xx-f1(xx)/f2(xx)
        disp(xx)
    end
end

        
        