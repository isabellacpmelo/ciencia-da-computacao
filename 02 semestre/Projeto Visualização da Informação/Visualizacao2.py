import pandas as pd
import matplotlib.pyplot as plt

file_url = 'dataset.csv'
dataset = pd.read_csv(file_url)
dataset = pd.DataFrame(dataset)

topic = 'Deaths - Drug use disorders - Sex: Both - Age: All Ages (Number)'
deaths_df = dataset.loc[dataset['Entity'] == 'World', ['Entity','Year', topic]]
numbers = list(pd.Series(deaths_df[topic]))
years = list(pd.Series(deaths_df.Year))

deaths_df = [years, numbers]

plt.plot(years, numbers)
plt.title('Mortes Devido ao Uso de Drogas')
plt.ylabel('Mortes (em milhões)')

plt.show()