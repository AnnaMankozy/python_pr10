import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 10, 50)
y = x**np.sin(10*x)

plt.plot(x, y, label='x^(sin(10x))', color='green', linewidth=3)

plt.title('Графік функції Y(x) = x^sin(10x)', fontsize=15)

plt.xlabel('x', fontsize=12, color='blue')
plt.ylabel('y', fontsize=12, color='blue')

plt.legend()
plt.grid(True)

plt.show()
