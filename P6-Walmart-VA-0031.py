import matplotlib.pyplot as plt
import numpy as np
#Arevalo Rafael NC:0031 Fecha:27/10/26

cant_productos=[100,150,200,300,500]
precio = [4000, 7000, 9000, 12000, 18000]

plt.plot(cant_productos, precio)
plt.show()

# Personalizar grafica
plt.figure(figsize=(4,3)) # Tamaño de la figura
plt.plot(cant_productos, precio, color="green",marker="o",linestyle="dashed", linewidth=2, markersize=12)
plt.title("Ventas Walmart")
plt.xlabel("cant prod")
plt.ylabel("presio")
plt.show()

print("--- Arevalo Rafael NC:0031")
