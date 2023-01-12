🍿Mas ainda há mais! Também é possível fazer gráficos sobre `Series`, novamente usando `.plot`. E como os resultados do groupby são `Series`... podemos fazer coisas como essas!:

```python
# barh é uma variação do gráfico de barras que já vimos,
# que apresenta disposição horizontal
ム cinemas.groupby("sector")["screens"].sum().plot.barh()
```

<img src="https://raw.githubusercontent.com/MumukiProject/mumuki-guia-python3-agrupaciones-y-graficaciones/master/assets/cinemas_sector_barh_1663908367802.png" alt="cinemas_sector_barh_1663908367802.png" width="auto" height="auto">

> Tente os seguintes gráficos em seu caderno:
>
> * `cinemas.groupby("sector")["screens"].sum().plot.pie()`
> * `cinemas.groupby("sector")["screens"].sum().plot.sort_values().pie()`
> * `cinemas.groupby("sector")["seats"].sum().plot.sort_values().pie()`
> * `cinemas.value_counts("sector").plot.sort_values().pie()`
>
> Que conclusões você pode tirar?