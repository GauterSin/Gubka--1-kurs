clc
syms z(v)
sym v
x = 0:pi/70:pi/2;
y = exp(2*x).*cos(x)
plot(x,y)
trap = trapz(x,y)
a= 0
b = pi/2
quads = quad(@f,a,b)
z(v) = exp(2*v).*cos(v)
intu =(int(z))


n = 35
h = pi/70
suma = 0
x1 = 0 
suma1 = 0
suma2 = 0
suma3 = 0
for i=1:35
    x1 = x1+h
    if i == 0
        sum3 = f(x1) + f(x1+h*n)
    else
        if mod(i,2) == 0
            suma1 = suma1+f(x1)
        else
            suma2 = suma2 + f(x1)
        end
    end
end

PogU = (1/5).*(-2+exp([pi]))
trapA = abs(trap - PogU)
trapO = abs(trap/PogU)
quadsA = abs(quads-PogU)
quadsO = abs(quads/PogU)

clc
disp(['trapz: Интеграл равен ' num2str(trap) '; Абс. погреш. = ' num2str(trapA) '; Отн. погреш. = ' num2str(trapO)]);
disp(['quad: Интеграл равен ' num2str(quads) '; Абс. погреш. = ' num2str(quadsA) '; Отн. погреш. = ' num2str(quadsO)]);
