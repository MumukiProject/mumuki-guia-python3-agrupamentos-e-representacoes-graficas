Como podemos ver, agora temos um gráfico de barras, no qual a informação é mostrada de forma _discreta_, ou seja, dando saltos de ano em ano ao invés de uni-las por meio de linhas _contínuas_.

<img src="https://raw.githubusercontent.com/MumukiProject/mumuki-guia-python3-agrupaciones-y-graficaciones/master/assets/employment_gender_plot_bar_1663775871814.png" alt="employment_gender_plot_bar_1663775871814.png" width="auto" height="auto">

Por outro lado, nem sempre os dados serão discriminados em séries múltiplas. Por exemplo, se tivéssemos apenas uma tabela com as informações totais de emprego...

```python
emprego_total = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vRSa9oM9fC-QlT7VOeGhZQtrWnlNSTsk3U8DWGTOXUWtPH6u9o5O5eZ0kTg8mFTwAn9vMdGRK7o2SPB/pub?gid=1194930839&single=true&output=csv")
emprego_total.head(5)
```

....poderíamos especificar uma única série no eixo y:

||year|employment_rate|
|---|---|---|
|0|2003|54.3|
|1|2004|56.7|
|2|2005|58.3|
|3|2006|58.4|
|4|2007|59.1|
|(...)|


```python
emprego_total.plot.line(x="year", y="employment_rate")
```

<img src="https://raw.githubusercontent.com/MumukiProject/mumuki-guia-python3-agrupaciones-y-graficaciones/master/assets/employment_rate_plot_line_1663776537522.png" alt="employment_rate_plot_line_1663776537522.png" width="auto" height="auto">
