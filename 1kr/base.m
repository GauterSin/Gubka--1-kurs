clc
syms z(v)
sym v
x = 0:1/35:1;
y = log(x + sqrt(x.*x + 4))
plot(x,y)
trap = trapz(x,y)
a= 0
b = 1
quads = quad(@f,a,b)
z(v) = log(v + sqrt(v.*v + 4))
intu =(int(z))


n = 35
h = 1/n
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

PogU = 2 - sqrt(5) + log(1 + sqrt(5))
trapA = abs(trap - PogU)
trapO = abs(trap/PogU)
quadsA = abs(quads-PogU)
quadsO = abs(quads/PogU)

clc
disp(['trapz: Интеграл равен ' num2str(trap) '; Абс. погреш. = ' num2str(trapA) '; Отн. погреш. = ' num2str(trapO)]);
disp(['quad: Интеграл равен ' num2str(quads) '; Абс. погреш. = ' num2str(quadsA) '; Отн. погреш. = ' num2str(quadsO)]);
