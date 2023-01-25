:sos: Gerar um CSV? Como fazemos isso? Socorro, pandas!

:arrows_counterclockwise: É possível converter `DataFrames` e `Series` em CSVs usando `to_csv`, como segue:

```python
uma_coluna_ou_tabela.to_csv()
```

Isso irá gerar uma string com o conteúdo do CSV, que para maior clareza podemos imprimir usando `print`:

```python
print(uma_coluna_ou_tabela.to_csv())
```

⚠️ Tem que ter cuidado com o índice, pois por padrão o `to_csv` vai adicionar uma coluna com seus valores, que dependendo do caso pode ou não ser útil. Por exemplo, se não especificarmos `as_index=False` ao fazer agrupamentos, tudo funcionará perfeitamente :tada:...

```python
ム print(cinemas.groupby("province")["seats"].sum().to_csv())
province,seats
Buenos Aires,93112
Catamarca,3200
Chaco,2469
Chubut,2682
Ciudad Autónoma de Buenos Aires,31386
Corrientes,3370
Córdoba,20799
...
```

...mas se usarmos `as_index=False` em vez disso, teremos uma coluna demais :expressionless::

```python
ム print(cinemas.groupby("province", as_index=False)["seats"].sum().to_csv())
,province,seats # observe que agora há mais uma coluna, sem nome
0,Buenos Aires,93112
1,Catamarca,3200
2,Chaco,2469
3,Chubut,2682
4,Ciudad Autónoma de Buenos Aires,31386
5,Corrientes,3370
6,Córdoba,20799
...
```

Portanto, neste caso queremos excluir explicitamente o índice, usando `index=False`:

```python
ム print(cinemas.groupby("province", as_index=False)["seats"].sum().to_csv(index=False))
province,seats
Buenos Aires,93112
Catamarca,3200
Chaco,2469
Chubut,2682
Ciudad Autónoma de Buenos Aires,31386
Corrientes,3370
Córdoba,20799
...
```