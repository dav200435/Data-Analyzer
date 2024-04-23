import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataframe = pd.read_csv('genshin.csv', sep=',', encoding='latin-1')
numeric_columns = dataframe.select_dtypes(include=['float64', 'int64'])
correlations = numeric_columns.corr()
print(correlations)
pd.plotting.scatter_matrix(correlations,figsize=(43,43),alpha=0.5)
plt.show()

tabla_recuentos = pd.pivot_table(dataframe, index='region', columns='vision', aggfunc='size', fill_value=0)
colores = {
    'Pyro': 'red',
    'Hydro': 'blue',
    'Anemo': 'lightgreen',
    'Electro': 'purple',
    'Geo': 'orange',
    'Cryo': 'lightblue',
    'Dendro': 'green'
}
grafico = tabla_recuentos.plot(kind='bar', stacked=True, figsize=(10, 6), color=[colores[col] for col in tabla_recuentos.columns])
plt.xlabel('Visión')
plt.ylabel('Recuento')
plt.title('Recuento de personajes con cada visión en cada región')
plt.legend(title='Región', bbox_to_anchor=(1, 1))
plt.show()

correlations=dataframe.corr()
sns.pairplot(correlations)
plt.show()