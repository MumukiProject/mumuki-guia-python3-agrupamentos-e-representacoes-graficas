¡Pero aún hay más! 🍿 También es posible hacer gráficos sobre `Series`, usando, nuevamente, `.plot`. Y como los resultados del groupby son `Series`... ¡podemos hacer cosas como ésta!:


```python
# barh es una variación del gráfico de barras que ya vimos,
# que presenta disposición horizontal
ム cines.groupby("sector")["screens"].sum().plot.barh()
```

<img src="https://raw.githubusercontent.com/MumukiProject/mumuki-guia-python3-agrupaciones-y-graficaciones/master/assets/cinemas_sector_barh_1663908367802.png" alt="cinemas_sector_barh_1663908367802.png" width="auto" height="auto">

> Probá los siguientes gráficos en tu cuaderno:
>
> * `cines.groupby("sector")["screens"].sum().plot.pie()`
> * `cines.groupby("sector")["screens"].sum().sort_values().plot.pie() `
> * `cines.groupby("sector")["seats"].sum().sort_values().plot.pie()`
> * `cines.value_counts("sector").sort_values().plot.pie()`
>
> ¿Qué conclusiones podés sacar?
