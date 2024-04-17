import pandas as pd  # Importar la biblioteca pandas procesar datos
import plotly.express as px # Importar la biblioteca plotly para visualizaciones graficar

# Cargar datos
df = pd.read_csv('sales_data.csv')

# Crear una visualización de las tendencias de ventas
fig = px.line(df, x='Fecha', y='Ventas', color='Producto')

# Guardar el gráfico como un archivo HTML
fig.write_html('sales_trends.html')
