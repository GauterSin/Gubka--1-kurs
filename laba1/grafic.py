import matplotlib.pyplot as plt
import math
import numpy as np

e = math.exp(1)
x = np.linspace(0, 10, 50)
y = 3*x - e**x
plt.title("Линейная зависимость y = x") # заголовок
plt.xlabel("x") # ось абсцисс
plt.ylabel("y") # ось ординат
plt.grid()      # включение отображение сетки
plt.plot(x, y)  # построение графика

plt.show()
