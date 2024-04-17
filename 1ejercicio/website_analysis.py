import pandas as pd
import plotly.express as px
import plotly.io as pio



# Carga de datos
data = pd.read_json('user_navigation_data.json')

# Análisis simple: Duración promedio en cada página
avg_duration_per_page = data.groupby('page')['duration'].mean().reset_index()

# Visualización con Plotly
fig = px.bar(avg_duration_per_page, x='page', y='duration', title='Average Duration per Page')
fig.show()


# Guardar la figura en un archivo HTML
pio.write_html(fig, 'website_analysis.html')

