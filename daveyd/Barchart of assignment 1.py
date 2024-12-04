import matplotlib.pyplot as plt

food_stuffs = ['Mushroom', 'Pineapple', 'Prawns', 'Sausage', 'Spinach']
proportions = [0.175, 0.29, 0.065, 0.185, 0.3]

plt.barh(food_stuffs, proportions, color='blue')

plt.title('Bar Chart of food_stuffs')
plt.xlabel('Proportion of Total')

plt.show()