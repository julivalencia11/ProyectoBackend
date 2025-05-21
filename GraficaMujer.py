import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Cargar el archivo CSV con separador correcto
df = pd.read_csv("Dataset3 (3).csv", sep=';')

# Seleccionar los primeros 10 países
top_countries = df[['Country', 'Women Entrepreneurship Index']].head(10)

# Preparar los datos
countries = top_countries['Country']
values = top_countries['Women Entrepreneurship Index']

# Crear figura y ejes
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(countries, [0]*len(values), color='purple')
ax.set_ylim(0, max(values) * 1.1)

# Configurar el gráfico
ax.set_title('Índice de Emprendimiento Femenino por País')
ax.set_xlabel('País')
ax.set_ylabel('Índice de Emprendimiento Femenino')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Función de animación
def animate(i):
    for j, b in enumerate(bars):
        if i >= j:
            b.set_height(values[j])

# Crear animación
ani = animation.FuncAnimation(fig, animate, frames=len(values)+2, repeat=False, interval=400)

plt.tight_layout()
ani.save('grafica_mujeres.gif', dpi=300)
plt.show()
