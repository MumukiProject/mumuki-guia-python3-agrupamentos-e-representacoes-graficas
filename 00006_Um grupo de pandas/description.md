E como criamos agrupamentos com `pandas`? Para isso temos o `groupby` (literalmente, _agrupar de acordo_) em inglês, uma operação de `DataFrame`s que é usada assim:

```python
tabela.groupby(coluna_de_acordo_a_qual_agrupar)[coluna_a_agrupar].agregação()
```

Por exemplo, se tivéssemos nossa hipotética tabela de multas e quiséssemos _agrupar de acordo com as placas e calcular a soma das infrações_, escreveríamos assim:    


```python
ム multas.groupby("placa")["infração"].sum()
placa
ab16    500
hz15    100
mm12    150
xy40    350
Name: infração, dtype: int64
```

Da mesma forma, é assim que ficariam as outras agregações que mencionamos:

```python
ム multas.groupby("placa")["infração"].mean()
placa
ab16    166.666667
hz15    100.000000
mm12    150.000000
xy40    175.000000
Name: infração, dtype: float64
ム multas.groupby("placa")["infração"].median()
placa
ab16    200.0
hz15    100.0
mm12    150.0
xy40    175.0
Name: infração, dtype: float64
ム multas.groupby("placa")["infração"].count()
placa
ab16    3
hz15    1
mm12    1
xy40    2
Name: infração, dtype: int64
```


> 🔙  Vamos fazer um _flashback_ e voltar aos nossos cinemas :movie_camera:. Escreva em seu caderno uma expressão que calcule a soma de telas pelo tipo de gestão e atribua a `telas_por_setor`.
