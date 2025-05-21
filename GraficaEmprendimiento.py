import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Cargar el archivo CSV
file_path = "US_FTRI_20230628035959 (1).csv"
df = pd.read_csv(file_path)

# Filtrar datos solo para Afganistán
afghanistan_df = df[df['Economy Label'] == 'Afghanistan']

# Obtener los años únicos ordenados
years = sorted(afghanistan_df['Year'].unique())

# Crear figura
fig, ax = plt.subplots(figsize=(8, 8))

def update(year):
    ax.clear()
    year_data = afghanistan_df[afghanistan_df['Year'] == year]
    ax.pie(
        year_data['Index'],
        labels=year_data['Category Label'],
        autopct='%1.1f%%',
        startangle=140
    )
    ax.set_title(f'Distribución del Índice FTRI por Categoría - Afganistán ({year})')
    ax.axis('equal')

# Crear la animación
ani = animation.FuncAnimation(fig, update, frames=years, interval=1500, repeat=False)

# Mostrar animación
plt.tight_layout()
ani.save('grafica_emprendimiento_femenino_afganistan.gif', dpi=300)
plt.show()
