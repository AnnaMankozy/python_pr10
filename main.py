import matplotlib.pyplot as plt  
import numpy as np

# Задаємо діапазон [1; 10] для функції x^sin(10x)
x = np.linspace(1, 10, 500) # Беремо більше точок для плавності складної функції
y = x**np.sin(10*x)          # Функція Y(x) = x^sin(10x)

# Побудова графіка зі стилем з вашого першого прикладу:
plt.plot(x, y, label='x^sin(10x)', color="red", linewidth=5)

# Назви та оформлення, як у першому прикладі
plt.title('Графік функції Y(x)=x^sin(10x)', fontsize=15)   
plt.xlabel('x', fontsize=12, color='blue') 
plt.ylabel('y', fontsize=12, color='blue')  

# Вивід легенди та сітки
plt.legend(loc='upper left')
plt.grid(True)

# Змінюємо розмір фігури, щоб коливання не були сильно стиснуті (як ми обговорювали)
plt.figure(figsize=(12, 5)) 

plt.show()