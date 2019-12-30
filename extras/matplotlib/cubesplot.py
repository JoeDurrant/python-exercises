import matplotlib.pyplot as plt

input = [x for x in range(1,5001)]
cubes = [x ** 3 for x in range(1,5001)]

plt.plot(input, cubes, linewidth=5)

plt.title("Cube numbers", fontsize=24)

plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)

plt.show()