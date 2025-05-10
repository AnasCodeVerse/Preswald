import pandas as pd
import plotly.express as px
import preswald

df = pd.read_csv('data/seattle-weather.csv')

fig = px.scatter(df, x='temp_min', y='temp_max', text='weather',
                 title='Temperature Min vs Max',
                 labels={'temp_min': 'Min Temperature', 'temp_max': 'Max Temperature'})

fig.update_traces(textposition='top center', marker=dict(size=12, color='lightblue'))
fig.update_layout(template='plotly_white')

preswald.text("# Seattle Weather Analysis - PressWorld App")
preswald.text("Weather app! 🎉")

preswald.plotly(fig)

preswald.text("## Weather Data Table")
preswald.table(df.head(10))