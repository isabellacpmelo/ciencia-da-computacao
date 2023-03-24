import plotly.express as px
import pandas as pd


dataset = pd.read_csv('dataset.csv')
dataset = pd.DataFrame(dataset)

deaths_df = dataset.loc[dataset['Year'] == 2017]
world_deaths = deaths_df.loc[deaths_df['Entity'] == 'World']
world_deaths = world_deaths.drop(['Entity', 'Code', 'Year'], axis=1)
world_deaths = world_deaths.sort_values(by = 6573, axis=1, ascending=False)

x_data = list(world_deaths.loc[6573])
y_data = list(world_deaths.columns)

fig = px.bar(x=x_data, y=y_data, orientation='h', labels={'y': '', 'x': 'Mortes (em milhões)', 'text':'Float'},
            title='Principais Causas de Morte no Mundo', text=x_data, range_y=[0, 10])

fig.show()