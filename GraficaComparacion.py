import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Cargar el archivo CSV
file_path = "antojitos-para-todos (2).csv"
df = pd.read_csv(file_path, encoding='latin1', sep=None, engine='python')

# Contar el número de entidades por localidad
localidad_counts = df['Localidad'].value_counts().sort_index()
localidades = localidad_counts.index.tolist()
valores = localidad_counts.values

# Preparar la figura
fig, ax = plt.subplots(figsize=(12, 6))

# Función de actualización para cada frame de la animación
def update(frame):
    ax.clear()
    ax.fill_between(range(frame + 1), valores[:frame + 1], color='skyblue', alpha=0.6)
    ax.plot(range(frame + 1), valores[:frame + 1], marker='o', color='blue')
    ax.set_xlim(0, len(localidades) - 1)
    ax.set_ylim(0, max(valores) + 5)
    ax.set_title('Cantidad de Entidades de Emprendimiento por Localidad (Animado)')
    ax.set_xlabel('Localidad')
    ax.set_ylabel('Cantidad de Entidades')
    ax.set_xticks(range(len(localidades)))
    ax.set_xticklabels(localidades, rotation=45, ha='right')
    ax.grid(True, linestyle='--', alpha=0.5)

# Crear la animación
ani = animation.FuncAnimation(
    fig, update,
    frames=len(localidades),
    interval=800,
    repeat=False
)

# Mostrar la animación
plt.tight_layout()
ani.save('grafico_localidades.gif', dpi=300)
plt.show()
