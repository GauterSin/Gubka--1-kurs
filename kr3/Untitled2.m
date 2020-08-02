clc
x=0:0.12:0.96;
y = F1(x);
x1=[0 0.12 0.24 0.36 0.48 0.6 0.72 0.84 0.96];
y1=F1(x1);

disp('������� 2-� �������:');
polinom2=polyfit(x,y,2)
disp('���������� �� ������ �������� ������� � ������:');
f2=polyval(polinom2,x1);
table = [ abs(y1-f2)]
figure   
plot(x1,y1,x1,f2)


disp('������� 4-� �������:');
polinom4=polyfit(x,y,4)
disp('���������� �� ������ �������� ������� � ������:');
f4=polyval(polinom4,x1);
table = [ abs(y1-f4)]
figure
plot(x1,y1,x1,f4)



